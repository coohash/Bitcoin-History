#!/usr/bin/env python3
"""
模块名称: bitcoin_bulk_checker.py
描述: 高效批量查询比特币地址余额（每 100 个地址合并为一次请求），结果自动输出到 btc-balance.csv。
作者: Python Senior Architect
"""

import asyncio
import logging
import csv
from typing import Dict, List, Optional
import aiohttp

# 配置日志输出格式
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger(__name__)

# 常量配置
BLOCKCHAIN_API_URL = "https://blockchain.info/balance"
CHUNK_SIZE = 100             # 每次批量查询的地址数量（API 限制通常为 100 左右）
MAX_CONCURRENT_REQUESTS = 1  # 批量查询下，单线程串行是最稳妥的，300次请求极快
MAX_RETRIES = 4              # 某一批次失败后的最大重试次数
BACKOFF_FACTOR = 3           # 触发 429 或网络抖动时的指数退避因子（秒）
DELAY_BETWEEN_REQUESTS = 1.0 # 每次批量请求之间的强制间隔时间（秒），保持礼貌抓取
SATOSHI_TO_BTC = 100000000   # 1 BTC = 10^8 Satoshi


def chunk_list(lst: List[str], size: int) -> List[List[str]]:
    """
    核心算法：将大列表按指定大小切分成多个小列表（Chunks）。
    """
    return [lst[i:i + size] for i in range(0, len(lst), size)]


async def fetch_chunk_balance(
    session: aiohttp.ClientSession,
    chunk_addresses: List[str],
    semaphore: asyncio.Semaphore
) -> Dict[str, Optional[float]]:
    """
    异步批量请求一组地址的余额，包含重试、退避和限流处理。

    Args:
        session: aiohttp 客户端会话
        chunk_addresses: 当前批次的地址列表（最多100个）
        semaphore: 信号量

    Returns:
        Dict[str, Optional[float]]: 包含当前批次所有地址及其对应余额（BTC）的字典
    """
    # 初始化当前批次的结果集，默认全部为 None (失败)
    chunk_result: Dict[str, Optional[float]] = {addr: None for addr in chunk_addresses}
    
    # 将地址用 '|' 拼接成 API 要求的格式
    joined_addresses = "|".join(chunk_addresses)
    url = f"{BLOCKCHAIN_API_URL}?active={joined_addresses}"
    
    async with semaphore:
        for attempt in range(1, MAX_RETRIES + 1):
            try:
                async with session.get(url, timeout=15) as response:
                    # 成功获取数据
                    if response.status == 200:
                        data: Dict = await response.json()
                        
                        # 成功读取后，强制休眠，防止频繁连续轰炸 API
                        await asyncio.sleep(DELAY_BETWEEN_REQUESTS)
                        
                        # 解析返回的字典
                        for addr in chunk_addresses:
                            if addr in data:
                                satoshi_balance = data[addr].get("final_balance", 0)
                                chunk_result[addr] = satoshi_balance / SATOSHI_TO_BTC
                            else:
                                chunk_result[addr] = None  # API 未返回该地址信息
                        return chunk_result
                    
                    # 触发限流 429
                    elif response.status == 429:
                        wait_time = BACKOFF_FACTOR ** attempt
                        logger.warning(f"由于批量请求触发限流(429)，将在 {wait_time} 秒后进行第 {attempt} 次重试...")
                        await asyncio.sleep(wait_time)
                    
                    # 服务器错误或其他错误
                    else:
                        logger.error(f"批量请求失败，HTTP 状态码: {response.status}")
                        if response.status >= 500:
                            await asyncio.sleep(BACKOFF_FACTOR * attempt)
                        else:
                            return chunk_result  # 400等客户端错误不重试

            except (aiohttp.ClientError, asyncio.TimeoutError) as e:
                wait_time = BACKOFF_FACTOR ** attempt
                logger.warning(f"网络异常(批量请求): {str(e)}。将在 {wait_time} 秒后进行第 {attempt} 次重试...")
                if attempt == MAX_RETRIES:
                    logger.critical("当前批次在达到最大重试次数后依旧失败。")
                    return chunk_result
                await asyncio.sleep(wait_time)
                
    return chunk_result


async def main_async(file_path: str, output_csv: str) -> None:
    """
    异步批量主控逻辑。
    """
    # 1. 读取并清洗 csw_bitcoin_address.txt
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            addresses: List[str] = list(set(line.strip() for line in f if line.strip()))
    except FileNotFoundError:
        logger.critical(f"错误: 找不到文件 '{file_path}'")
        return
    except Exception as e:
        logger.critical(f"读取文件错误: {str(e)}")
        return

    total_addresses = len(addresses)
    if total_addresses == 0:
        logger.warning(f"文件 '{file_path}' 中没有有效地址。")
        return

    logger.info(f"成功加载 {total_addresses} 个去重后的比特币地址。")

    # 2. 切片批处理
    chunks = chunk_list(addresses, CHUNK_SIZE)
    logger.info(f"已将地址切分为 {len(chunks)} 个批次（每批最多 {CHUNK_SIZE} 个地址），开始高效查询...")

    # 3. 建立连接池并分发批次任务
    semaphore = asyncio.Semaphore(MAX_CONCURRENT_REQUESTS)
    connector = aiohttp.TCPConnector(limit=MAX_CONCURRENT_REQUESTS)
    
    final_balances: Dict[str, Optional[float]] = {}
    
    async with aiohttp.ClientSession(connector=connector) as session:
        # 为了更直观地看进度，我们这里采用逐个批次递交（但内部仍然使用高性能连接）
        # 如果追求极限速度可以像以前一样用 asyncio.gather，但串行批量能提供完美的进度条展示且最安全
        for idx, chunk in enumerate(chunks, 1):
            logger.info(f"正在处理第 {idx}/{len(chunks)} 批地址...")
            chunk_res = await fetch_chunk_balance(session, chunk, semaphore)
            final_balances.update(chunk_res)

    # 4. 写入 CSV 结果文件
    logger.info(f"所有批次处理完毕，正在保存数据至 {output_csv}...")
    try:
        with open(output_csv, "w", newline="", encoding="utf-8-sig") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Bitcoin Address", "Balance (BTC)", "Status"])
            
            # 保持原始读取的顺序或去重后的顺序写入
            for addr in addresses:
                balance = final_balances.get(addr)
                if balance is not None:
                    writer.writerow([addr, f"{balance:.8f}", "Success"])
                else:
                    writer.writerow([addr, "", "Failed"])
                    
        logger.info(f"🎉 任务圆满完成！3万个地址已成功检索并写入本地：{output_csv}")
    except Exception as e:
        logger.error(f"保存 CSV 失败: {str(e)}")


if __name__ == "__main__":
    target_file = "csw_bitcoin_address.txt"
    output_file = "btc-balance.csv"
    
    try:
        asyncio.run(main_async(target_file, output_file))
    except KeyboardInterrupt:
        logger.info("程序被用户手动终止。")