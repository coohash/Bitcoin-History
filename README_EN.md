
# ❤️ Part One: The Genesis of Bitcoin

## 🏁 Chapter 1: This is a True Story

### 1.1.1 Ten Isolated Gears

🎯 Rewind to 2001. Imagine a workbench scattered with 10 "old toys":

| Technological Component | Year Proposed | Core Inventor / Representative Figure |
| :--- | :--- | :--- |
| **P2P Communication** | 1969 | ARPANET, U.S. Department of Defense |
| **Public Key Cryptography** | 1976 | Whitfield Diffie, Martin Hellman |
| **Merkle Trees** | 1979 | Ralph Merkle |
| **Elliptic Curve Cryptography (ECC)** | 1985 | Neal Koblitz, Victor Miller |
| **Timestamping** | 1991 | Stuart Haber, W. Scott Stornetta |
| **Proof of Work (PoW)** | 1992 | Cynthia Dwork, Moni Naor |
| **Programmable Contracts** | 1996 | Ian Grigg, Nick Szabo |
| **Byzantine Fault Tolerance** | 1999 | Miguel Castro, Barbara Liskov |
| **Digital Cash Theory** | 1983-1999 | David Chaum, Wei Dai |
| **Hash Algorithm (SHA-256)** | 1990-2001 | NIST (National Institute of Standards and Technology, USA) |

⚙️ At this point, all the foundational building blocks needed to create Bitcoin were already in place, lying dormant, waiting to be combined. Specifically, what was missing was a set of rules. Someone needed to integrate all these elements into a unified incentive system. Someone needed to invent a protocol—an immutable, foundational protocol—to mesh these 10 isolated gears together.

⚔️ Humanity had been groping in the dark for nearly fifty years since Feller's landmark work on probability theory in 1957, waiting for this protocol.

---

🌐 In 2001, a project called "BlackNet" was submitted to the Australian government to apply for research grants and tax relief. BlackNet described a peer-to-peer transaction system that could facilitate "online payments" without the need for any central authority. Between 2001 and 2009, he successfully obtained the relevant relief. He tried again in 2009 and 2010 but was unsuccessful. This is the truest starting point of the entire genesis story.

🐳 In October 2007, in a corner of Australia, a computer screen running Windows Server 2003 emitted a dim light. Sitting in front of it was the mysterious figure later known as "Satoshi Nakamoto."

💡 Before publishing the famous Bitcoin whitepaper, Satoshi Nakamoto chose a hardcore path截然 different from that of traditional software architects. He adhered to "code first." He had to first get the code working, confirming that the defensive network built with mathematics and game theory had truly vanquished the "Double-Spending" problem that had plagued digital currency for decades, before he even started writing the whitepaper.

### 1.1.2 From Code to Soul

It was an incredibly solitary and massive undertaking. In his open Microsoft Visual Studio 2005 compiler, approximately 14,000 lines of extremely compact C++98 code were growing wildly. He didn't reinvent the wheel from scratch but acted like a top-tier system integrator, embedding the initial soul of Bitcoin into core files like `main.cpp`, `script.cpp`, and `util.cpp`:

* **Choice of Cryptography**: He directly called upon the open-source OpenSSL library, ruthlessly stripping away redundant cryptographic protocols, leaving only the core `EC_KEY` structure. He precisely aligned the parameters to the then-obscure `secp256k1` curve. It would be several years before this curve became world-famous because of Bitcoin, but in Satoshi's eyes, its near-perfect algebraic structure meant faster scalar multiplication and smaller signature sizes.

* **The Most Primitive Assembly**: For the P2P communication layer, he wrote a rudimentary network topology based on Blocking Sockets and native C++ threads. No advanced Object-Relational Mapping was used; all amounts (UTXOs) were directly crammed into a lightweight database called Berkeley DB. To seamlessly convert data between local storage and the network, he manually wrote extensive code, using the most traditional C++ serialization macros to stuff transactions into cold byte streams.

* **Cross-Disciplinary Algorithmic Domination**: To validate the concept, he wrote a highly simplified Bitcoin model in C++. Hidden within this simplified model were the secrets of how he cross-assembled technologies from different fields. Achieving time and state synchronization among mutually untrusting nodes was once an insurmountable mountain. Satoshi's brilliance lay in using the most pragmatic and hardcore engineering methods to shatter this technological curse. Without relying on any fancy external hardware, he crafted a bespoke "distributed time median" mechanism for Bitcoin within the lower realms of C++ code, using pure logic and algorithms. He completely decoupled unreliable single-point time, instead extracting a "time barrier" dependent on network-wide consensus, rendering time-based attacks on the ledger futile. This architectural artistry—perfectly integrating cryptography, game theory, and network communication—was a direct blow to the high-cost traditional centralized solutions of the time.

* **Pragmatic Compromises**: To make it usable for ordinary people, he introduced the `wxWidgets` cross-platform framework into the code, hand-coding the layout line by line. The screen finally displayed a drab, gray graphical user interface (GUI) sporting the classic Windows XP window style. The rough progress bar, syncing the blockchain, often appeared sluggish due to single-threaded network blocking, occasionally even popping up the classic Windows "Program Not Responding" window.

* **Original Casino Gears**: In the pauses between handling multi-threading and block broadcasting, he left behind concise program sleep syntax like `sleep_for` in the code, giving the cold machine room to breathe. As for the crucial "random number generation" elements in the code, used to defend against deterministic attacks, Satoshi revealed his experience as a veteran deeply immersed in the dark web for years. These mathematical algorithms originated from random number generators he had been using proficiently since the 1980s. At that time, the most notorious and mature application of this technology was in countless online gambling websites scattered across the internet. Now, the probabilistic gears that gamblers used to roll dice were repurposed by him as the strongest defense line in the cryptographic world.

* **Turing Complete Design**: In the initial implementation of `script.cpp`, he personally crafted a stack-based, Reverse Polish Notation (RPN) interpreter—Bitcoin Script. This highly programmable scripting language is similar to Forth, operating on a dual-stack architecture (main stack and Alt stack). It is functionally complete under specific constraints, essentially a Turing machine with looping structures and conditional execution capabilities, leaving vast room for future expansion.

* **The Heart of the Codebase**: Within the cold logic of the inaugural Bitcoin code (v0.1.0 Alpha) he personally typed, beat a wild "casino heart." With far-sighted architecture, he pre-embedded a sophisticated peer-to-peer Texas Hold'em poker game framework within the `CPokerLobbyDialogBase` class. He transformed a series of gaming commands—dealing, folding, calling, checking, raising, and even leaving the table—into state synchronization at the distributed network's base layer. Using this seemingly unserious set of poker rules, he ingeniously established a secure betting mechanism among mutually untrusting players.

* **Addresses Starting with 1**: Staring at the hexadecimal hash gibberish on the screen, he frowned. These long strings were prone to transcription errors. He typed out a filtering logic: remove the digit `0` and the uppercase letter `O`; remove the uppercase letter `I` and the lowercase letter `l` (easily confused). Then, he introduced Base58 and appended a 4-byte SHA-256 double-hash checksum. The first Base58Check encoding,兼顾 human readability and mathematical rigor, was born—that concise address format starting with the number `1` became the key identifier for native Bitcoin: Bitcoin addresses start with `1`.

* **The Process of Finding Zero**: He defined mining with the roughest rules: a collective brute-force (guessing) race. The system sets a target hash value based on the current difficulty. Because this number is extremely small, it manifests in hexadecimal as "a long string of leading zeros." Miners worldwide simultaneously began exhaustive search, frantically changing the nonce. Mining was a speed race of "cracking" (who gets more zeros). Whoever first calculates a hash value that meets the target (i.e., the required number of leading zeros) wins immediately, receiving 50 Bitcoins (halving every 4 years). Once one wins, the network resets, and the next round of bombing begins. A block hash looks like this: `000000000000000002feb6a36e1b8bf81409d0252e285449e3d0ef2388c5506a`.

On September 10, 2008, a concise version of the Bitcoin code was completed. The total issuance in this version was 4.2 billion satoshis, with a very small initial reward: "`txNew.vout[0].nValue = 10000;`" — only 10,000 satoshis, equivalent to 0.0001 Bitcoin. To allow early users to gain more rewards and stimulate motivation, Satoshi multiplied the reward by 500,000, ultimately changing it to "`txNew.vout[0].nValue = 50 * COIN;`" at launch. This change was crucial. His programming development was primarily in gambling software; his first thought when writing code was to use algorithms to exploit players. With a total design of 4.2 billion satoshis, Bitcoin mining would have been difficult to popularize among individual users. By magnifying the total supply 500,000 times to 21 quadrillion satoshis, it greatly incentivized early miners. However, he vastly underestimated human greed.

On October 31, 2008, an email appeared on the "Cryptography Mailing List" on Metzdowd. The email attached a nine-page document. The author was Satoshi Nakamoto. The title was *Bitcoin: A Peer-to-Peer Electronic Cash System*. The whitepaper abstract explicitly proposed establishing a purely peer-to-peer electronic cash system, enabling direct person-to-person payments, completely bypassing traditional financial institutions. Notably, this email was not sent to the "cypherpunks" who would later denigrate him, but to the more professional and commercial "Cryptography Mailing List."

---

## 🏁 Chapter 2: The Historic Ignition and Genesis Compromise

### 1.2.1 The Historic Moment: Genesis Ignition

Compile, run, debug. After hundreds of days and nights of solitary keystrokes, the `bitcoin.exe` executable file was finally successfully output on the screen. This was a main program integrating wallet, node communication, and mining functions into one. Only at this point did the later-world-shaking "Nakamoto Consensus" transform from an elegant game-theoretic deduction in his mind into lines of code on the hard drive, ready to process computing power. To simulate network effects, he even embedded hardcoded seed nodes (IPs: 74.208.43.192, 91.198.22.70) into the program, ensuring this newborn "digital infant" could immediately find its counterparts upon connecting to the internet.

⛓️ **The Genes of the Genesis Block:**

* **Wasteland**: `hashPrevBlock "0000000000000000000000000000000000000000000000000000000000000000"`
* **Declaration**: `The Times 03/Jan/2009 Chancellor on brink of second bailout for banks`
* **Timestamp**: `1231006505` (Unix timestamp, i.e., January 3, 2009, 18:15:05 UTC)
* **Foundation**: `nVersion`, `nTime`, `nNonce`, `hashMerkleRoot`
* **Monument**: `1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa` (This is Bitcoin's genesis address, uniquely locked by the hardcoded public key `04678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5f`. Wherever and whoever runs this genesis code: the generated address will always be this one. This is Bitcoin's eternal monument.)

These parameters were all predefined and hardcoded in the code. This means Satoshi Nakamoto had designed this "beginning" mathematically before running the program. This was Bitcoin in its infancy: a mediocre, understated, even somewhat shabby Windows window. It didn't look like a world-changing tool, but rather a nameless seed quietly buried in the soil at midnight, waiting to stir up a storm. Worth noting is the date format "03/Jan/2009" in the declaration. This format is standard within the Commonwealth. The UK, Australia, Canada, and other Commonwealth nations use this format. Americans do not. So, this itself hints at certain things, like where Satoshi might have come from.

On January 3, 2009, the world's first decentralized payment perpetual motion machine completed its first ignition within this Windows window. At the moment the Genesis Block was born, there was only one node on the network: Satoshi's computer. He was both the sole miner and the sole network maintainer. The flame was faint, but no one anticipated that this nascent algorithmic engine would soon sweep forward with global digital computing power, eventually consuming 0.5% of humanity's electricity.

### 1.2.2 The Historic Moment: Second Ignition

First launch: January 3, 2009, 18:15:05 UTC. It ran for 6 days and was then abandoned.

Second launch: January 9, 2009, 02:54:25 UTC. This launch has been running stably ever since. So, Bitcoin's launch date could be considered January 9, 2009. The essence of Bitcoin is that once version 0.1 was released, its protocol was fixed and remains unchanged throughout its lifecycle.

There is a 6-day gap between the Genesis Block (Block 0) and Block 1 of Bitcoin. Simply put, Bitcoin launched on 2009-01-03 18:15:05, but Block 1 was mined 6 days later, on 2009-01-09 02:54:25. Why? Precisely because Bitcoin was launched twice.

For both launches, the time and address of Block 0 are the same, as these are hardcoded in the source code. If you download the Bitcoin source code today, the launch time remains 2009-01-03 18:15:05, and only Block 1 will have the current time.

Let's analyze these two launches. After the launch on January 3, 2009, he kept debugging. But 6 days later, he encountered a system-level failure.

This was a busy 6 days for Satoshi. He set up a Windows Server 2008 domain, establishing a forest-like hierarchical structure with clustered servers located at his home on the Bagnoo farm near Sydney. During 2009, Satoshi used approximately 10-12 computers for mining Bitcoin. At that time, he maintained 67 servers, most running CentOS, Red Hat, and Solaris for tasks like databases, DNS, and sendmail. However, Bitcoin ran on Windows, so he squeezed out these 10-12 Windows machines. They used Windows Server 2003 licenses. On January 9th, the MS09-001 patch was applied. This was a critical patch addressing three high-severity vulnerabilities, requiring a forced Windows restart after installation. To apply the patch, Satoshi halted all servers simultaneously. This caused the entire Bitcoin network to be unable to follow the initial chain, necessitating a restart. When the network restarted, various network services and connections experienced issues. To say the least, it was chaotic. He had to abandon the first chain and relaunch Bitcoin.

At that time, `bitcoin.exe` did not support "mining pool" architecture or remote centralized control. It couldn't aggregate the hash power of multiple computers to calculate the same hash. They were essentially 10-12 independent competitors, but they were on the same local network and presented themselves externally as a single node. Each machine ran the `bitcoin.exe` program, generating its own independent `wallet.dat` file, each containing 100 initial private keys.

This incident made Satoshi realize that being the sole miner was unsustainable. Even with a dozen computers, if they were all in one location, a network outage or power failure could cripple the Bitcoin network. So, he set up two server nodes in Melbourne and California. He enlisted his cousin Max Lynam and his friend David Kleiman to run nodes. David Kleiman helped run two nodes. He even set up nodes on two computers at a church he helped maintain, which reportedly mined 80,000 to 100,000 Bitcoins.

The MS09-001 patch was released on January 13, 2009. Microsoft issued a "pre-notification" to the public on January 8th, informing them of the major vulnerability requiring a server restart. Satoshi applied the patch on January 9th, right after Microsoft's announcement on the 8th. This suggests his industry had extremely high security requirements (e.g., network security, antivirus, finance). Such companies often get early access through "corporate premium support services, Microsoft Active Protection Program, MSRC privileged partners, or coordinated vulnerability disclosure (CVD)" before the patch is released to the general public.

In 2009, after Satoshi ran 10-12 server nodes, he handed over server operation and maintenance responsibilities to David Kleiman. It was tedious work; every Bitcoin upgrade required logging in to replace and restart. But they never discussed how many Bitcoins were mined, as Bitcoin had no practical value at the time.

---

# ❤️ Part Two: Genesis Privilege: My Code, My Consensus, I Am Truth

## 🏁 Chapter 3: Activating the Bitcoin Network's Secret

### 2.1.1 The Genesis Foundation: A Project Packaged for Sale

Bitcoin's origin might be far more worldly and utilitarian than commonly imagined. Tracing back its long incubation period, it started merely as a "tax project" crafted by a genius between 2001 and 2009 to game the Australian government for research funding and tax relief. Satoshi began writing Bitcoin code in October 2007. With the start of the underlying code, the project escalated into a "decentralized online gambling platform."

However, the dramatic twist of history came in 2008. As the underlying code neared completion, the global subprime mortgage crisis erupted unexpectedly. The systemic collapse of the financial tsunami acted as a powerful catalyst, prompting Satoshi to transform this project—originally imbued with "tax arbitrage" and "online casino" characteristics—into a "decentralized electronic cash system" aimed at challenging traditional centralized fiat hegemony.

From "tax project" to "online gambling platform" to "payment system," these were Satoshi's own visions. But the subsequent evolution became even more frenzied, spiraling out of his control to the point of fear. He excelled at using algorithms to exploit gamblers but could not have predicted the greed of humanity. The ensuing ecological evolution, swept along by capital, speculation, and human nature, careened forward irreversibly, ultimately terrifying even the rational, orderly, and anonymous Satoshi, leading him to choose to fade into the darkness.

From the launch of Bitcoin in January 2019 (likely a typo, meant 2009) until June 2010, a year and a half passed. Bitcoin entered an 18-month period of barrenness. This "perpetual motion machine" seemed forgotten by the world, as desolate as a lone lamp deep in the wilderness, with only Satoshi and a few fire-stealers gathered around the dim light, silently adding fuel. In the first few months of 2009, the on-chain world was silent, with only a handful of transactions. Mining participants were concentrated within a small circle.

But Satoshi wasn't idle in 2009. During this period, he tried to sell the technology to governments and Microsoft. He proposed it to Microsoft, sent the whitepaper to casino owners, and engaged in multiple discussions with the Australian government, explaining how an immutable ledger based on CAATs (Computer-Assisted Audit Techniques) software could replace grassroots auditors. Yes, at this point, Satoshi wanted to sell the Bitcoin-related technology.

It wasn't until June 2010 that Satoshi's efforts to sell the technology made no progress, and he began losing confidence in his project. He had been persistently pushing for Bitcoin-based commercial applications and promoting its micropayment capabilities, hoping for adoption by e-commerce sites. However, the first application people developed was a heroin shop (The Farmers Market). At this point, the stagnant waters were broken, and Bitcoin welcomed a turning point. The appearance of the heroin shop gave Bitcoin its first on-chain transfer records. The purpose was clear: Bitcoin's timestamp recorded every transaction, helping users protect their identities, but ultimately leaving a traceable ledger. On June 29, 2010, to increase transaction volume, Gavin Andresen set up a "Bitcoin Faucet" website. Anyone could claim 5 Bitcoins after entering a captcha—no strings attached. This nearly absurd act of dispensing wealth was like a depth charge. The attention and traffic of curious onlookers began to pour in, fully activating the once-static consensus gears. Under the faucet's selfless pouring, Bitcoin finally emerged from its lonely polar night, beginning its tumultuous new story of world disruption.

### 2.1.2 Frequent Updates, Arbitrary Changes and Modifications

In the first version of the Bitcoin software, there were no limits on the number of connections between nodes, no block size limits, and no script opcode limits.

In November 2009, Satoshi modified the code, limiting sending nodes to a maximum of 1,000 addresses per message. If more than 1,000 addresses needed to be sent, they had to be sent in multiple messages.

In June 2010, Satoshi further modified the receiving node's processing mechanism, limiting it to process no more than 1,000 addresses at a time. Messages containing more than 1,000 addresses would be rejected.

In June 2010, Satoshi updated the code, adding 47 IP addresses of some Bitcoin nodes hardcoded into the software itself, in addition to specifying an IRC server.

Between July 28 and August 15, 2010, a short span of 19 days, Bitcoin experienced its first hack, marking the period of the most significant modifications to the original code.

* **July 28, 2010**: The `OP_RETURN` vulnerability was discovered. Anyone could easily empty someone else's wallet. By simply adding the instructions "correct (`OP_1`)" and "stop (`OP_RETURN`)" before the lock of any wallet, the safe would instantly hit a BUG—it would bypass all password verification and determine "unlock successful"! This meant that the defenses of any Bitcoin address worldwide were instantly rendered useless, allowing anyone to loot funds. Satoshi fixed the vulnerability within hours. He changed the logic to: whenever triggered, it would be judged as "fail and report an error," thus preventing the bypass. The crisis was successfully resolved after the patch was deployed.

* **July 29, 2010**: Satoshi participated in a discussion thread on the Bitcoin forum titled "Scalability and Transaction Rate." At the time, Dan Larimer questioned Bitcoin's scalability, especially the 10-minute block generation time. Larimer thought 10 minutes was too slow for real-world payments. After several rounds of replies, Satoshi lost patience: "If you don't believe me or don't get it, I don't have time to try to convince you, sorry." This quote has been cited thousands of times as a sign of confidence. But please read it in context. That was not confidence; that was impatience. Satoshi was annoyed. He had already explained multiple times why the block time is 10 minutes. He told Larimer to get lost. He had a temper; he was not a god.

* **July 30, 2010**: The Bitcoin testnet was launched, set up by Gavin Andresen.

* **August 15, 2010**: The integer overflow vulnerability was discovered. In block 74,638, a transaction created 184,467,440,737 Bitcoins. This number is not random; it's 2^64 divided by 100 million, the maximum value of a 64-bit unsigned integer expressed in the basic Bitcoin unit. The transaction code failed to capture such a large output, causing an overflow during summation. Jeff Garzik was the first to notice it. He posted the message on the forum. Satoshi was awake and online. Within five hours, Satoshi wrote, tested, and released Bitcoin v0.3.10 with the patch. The new client rejected the overflowing transaction and adopted the "correct" chain. 53 blocks later, at block 74,691, the network reorganized around the patched chain. The overflow transaction was erased from the ledger. As far as the network was concerned, that transaction creating 184 billion Bitcoins never happened.

* **August 15, 2010**: On the same day he fixed the integer overflow bug, Satoshi also disabled a powerful set of script opcodes: `OP_CAT`, `OP_RIGHT`, `OP_2MUL`, `OP_2DIV`, `OP_MUL`, `OP_DIV`, `OP_MOD`. The stated reason was Denial of Service attacks. Attackers could exploit this vulnerability using `OP_DUP` combined with `OP_CAT` and other means to increase data on the stack exponentially, exhausting node memory and crashing the network. This was indeed a valid concern. It was also a conservative move. These opcodes were not removed from the codebase but were commented out, with a note that they could be re-enabled once scaling protections were in place.

The impact of this decision lasted for over a decade. These opcodes were intended for implementing complex contract logic, digital identity verification, tokenization, and the creation of programmable tokens. This implies that Bitcoin was Turing-complete from its inception, or more precisely, functionally complete under certain constraints. For example, opcodes like `OP_RETURN`, `OP_EVAL`, `OP_CHECKDATASIG`, `OP_IF`, `OP_ELSE`, `OP_ENDIF`, `OP_VERIFY`, `OP_CHECKSIG`, and especially specific ones like `OP_CAT` are foundational for building more expressive scripting languages capable of implementing smart contract functionality. Their absence is one reason Bitcoin's network cannot implement some features found in other blockchains. As interest in smart contracts and tokens rekindled, the absence of these opcodes became a focal point of debate within the Bitcoin community in 2026. Simply put: it's not that Bitcoin lacked functionality, but that Satoshi deliberately restricted it in 2010, and later custodians, to maintain control, were unwilling to re-enable them.

In October 2010, Satoshi modified the mechanism again, stating that if a sending node knew fewer than 2,000 active addresses, it would send all of them (but still no more than 1,000 addresses per message). If it knew more than 2,000 active addresses, it would use a random number generator to send, on average, 2,000 of those addresses (again, 1,000 per message). Shortly after, it was changed from 2,000 to 2,500.

One of Bitcoin culture's most fundamental tenets is that the protocol cannot be modified. Yet, within 19 months of the Bitcoin network's launch, its creator unilaterally pushed through various changes. He reversed a confirmed transaction within 5 hours, without debate. Satoshi was a pragmatist. When his payment system encountered catastrophic bugs, he acted like a pragmatic decision-maker.

---

## 🏁 Chapter 4: Open Source is for You, Efficient is for Me

### 2.2.1 Multi-threaded for Myself, Single-threaded Open Source for Everyone

In 2010, a Florida programmer named Laszlo Hanyecz discovered a method to mine Bitcoin on graphics cards. He wrote GPU mining software and posted about it on the forum.

Satoshi's first reaction was to send him a private message, asking him to slow down. "Hey, can you slow down?" He then posted publicly on the forum, appealing for a gentleman's agreement. "For the good of the network, we should have a gentleman's agreement to delay GPU mining as much as possible. Make it easier for new users to get started." Laszlo emailed Satoshi to apologize.

Now, this next part reveals Satoshi's values and, more frankly, his cunning. Satoshi had already privately developed his own GPU mining software. He claimed he wrote it to defend against potential 51% attacks. The public "single-threaded" mining program he released was not the one he used himself. He used a multi-threaded mining program, far more advanced than any publicly available one.

Combined with his ban on Laszlo, Satoshi asked the community to pause GPU mining while he himself was already using multi-threaded mining capabilities. He kept the production-grade tools for himself.

So, how many Bitcoins did Satoshi mine for himself using his production-grade mining tools?

Early Bitcoin blockchains exhibit two distinct mining characteristics. One is the single-threaded mining mode of the public client. The other is generated by multi-threaded miners using multiple CPU cores to scan the ExtraNonce field in parallel. This represents a unique mining fingerprint observable in the ExtraNonce field of early blocks. This pattern is now known as the Patoshi Pattern.

Based on this fingerprint analysis, Satoshi mined approximately 1.1 million Bitcoins during the first year of the Bitcoin network's existence. Remember this number: 1.1 million. This figure is accurate down to the ten-thousand, and it's significant. Mined in 2009, just one year later, the influx of mining power rapidly diluted Satoshi's share to a fraction of a percent. Almost instantly, he lost his dominant mining capability.

Satoshi used a custom, non-public miner. Multi-threaded mining wasn't publicly released until 2010, and before that, only Satoshi himself used it privately. There's more intrigue here. In the first year, Patoshi deliberately reduced his hashing power, seemingly slowing down as new miners joined. He would pause for five minutes after mining each block. It appeared he didn't want to mine too many blocks consecutively, deliberately avoiding monopolizing network resources.

This suggests Satoshi attempted to protect the network from his own monopoly. It's impossible to definitively infer the exact motive, but the fact remains: Satoshi's actions were deliberate.

Satoshi released a single-threaded CPU mining program for public use, while privately running a multi-threaded optimized mining program. He suppressed the community's efforts to develop GPU mining, even though he already possessed that capability. In the first year, he used his undisclosed software to amass 1.1 million Bitcoins.

This behavior aligns more with a commercial developer. He released a simple version while keeping the production-grade engine for himself.

### 2.2.2 The God-Mode "Kill Switch"

On August 15, 2010, an unidentified attacker exploited an integer overflow bug in the Bitcoin client to create 184 billion Bitcoins in a single transaction at block height 74,638. Satoshi's response was swift and decisive: release a patch within five hours, hard fork, orphan the chain, and restore a clean ledger.

Simultaneously, he hardcoded a public key into the Bitcoin client. He held the matching private key and told no one. With it, he could broadcast a signed message to every node on the network, freezing all wallets' ability to send transactions. This feature was introduced on August 15, 2010, with Bitcoin v0.3.10, the same emergency release that fixed the value overflow incident. It was called the Alert System. Alerts trigger a function known as "safe mode." Safe mode disables all RPC commands that can send Bitcoin. Wallet sending functions stop, transactions cease. All running nodes immediately halt Bitcoin payments. The community accepted it readily and largely forgot about it for the next six years.

In other words, one person, wielding a single key, could freeze the entire network's transfer capability with a single signed message. Satoshi never corrected this kill switch. The Alert System remained in the client through versions v0.3.x, v0.4.x, and v0.5.x. Satoshi held the key alone until he passed it to Gavin Andresen. Finally, in September 2016, the alert public key that Satoshi had hardcoded in `alert.cpp` was completely removed.

This was the most authoritarian feature in the most "decentralized" software ever created, and the person who wrote it never publicly explained why. We built Satoshi from the inside out. Before his disappearance, he was a dictator, single-handedly controlling Bitcoin's code, website, forum, domain, and mining.

This alert key was publicly disclosed by Gavin Andresen on July 2, 2018, for security reasons. We can see what it looks like.

Bitcoin Alert Key stored in OpenSSL serialized format:<br/>
`30820113020101042053cdc1e0cfac07f7e1c312768886f4635f6bceebec0887f63a9d37a26a92e6b6a081a53081a2020101302c06072a8648ce3d0101022100fffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f300604010004010704410479be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8022100fffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141020101a14403420004fc9702847840aaf195de8442ebecedf5b095cdbb9bc716bda9110971b28a49e0ead8564ff0db22209e0374782c093bb899692d524e9d6a6956e7c5ecbcd68284`<br/>
`(Public Key: 04fc9702847840aaf195de8442ebecedf5b095cdbb9bc716bda9110971b28a49e0ead8564ff0db22209e0374782c093bb899692d524e9d6a6956e7c5ecbcd68284)`<br/>
`(Private Key: 53CDC1E0CFAC07F7E1C312768886F4635F6BCEEBEC0887F63A9D37A26A92E6B6)`

### 2.2.3 The Sanctified 1 MB Block Size

On July 15, 2010, Satoshi committed a change to the source repository, limiting the block size miners could generate to 990 KB. No significant commit message was left, no mention on the Bitcoin forum, no discussion whatsoever—the change simply took effect. Two months later, on September 7, 2010, he committed a second change. This time, it enforced a 1 MB block size limit at the consensus level. Again, no announcement, no discussion. The code was added, and the network functioned normally.

For context, the idea had been brewing for months. Months earlier, Hal Finney had suggested setting a block size cap to prevent denial-of-service attacks. The reasoning was straightforward: without a cap, a malicious miner could generate a gigabyte-sized block, forcing every node on the network to download and verify it, thereby crippling the fragile system. When the network was still small, a reasonable block size cap effectively blocked this attack vector. Satoshi accepted this rationale and set a block size cap, but he didn't publicize it. His silence implied the change was unimportant, not even worth discussing.

On October 3, 2010, a developer named Jeff Garzik released a patch to raise the cap from 1 MB to 7 MB. At the time, the Bitcoin network was tiny, blocks were almost empty, and the block size was merely a precaution. However, Satoshi rejected this patch. His stated reason was that it could cause a network fork if older nodes didn't upgrade. This decision permanently altered Bitcoin's subsequent development, as those who inherited his project came to regard the 1 MB limit as permanent, sacred, and inviolable.

Without modifying the 1 MB limit, Bitcoin loses the ability to scale on-chain, resulting in narrow throughput, limited expansion, constrained liquidity, and high on-chain transaction fees. In 2010, server and bandwidth resources were scarce, necessitating a block size limit. Given the immense development in computers and networks over the subsequent decades, continuing to restrict the block size points to a carefully orchestrated, deliberate weakening.

---

# ❤️ Part Three: The Deity Steps Down—Power Transition and the Mortal Behind the Mask

## 🏁 Chapter 5: The Transfer of the Scepter and De-Satoshification

### 3.1.1 The Real Satoshi Nakamoto and the Beginning of His Disappearance

The real Satoshi Nakamoto possessed immense patience, maintaining a small circle of testing and mining for the first 18 months after Bitcoin's launch. He maintained programming habits from the 90s, with large, bloated main files, and no standardized testing—whatever worked was fine. He added Texas Hold'em poker code to the Bitcoin source code. He wrote a custom multi-threaded mining program for himself, while releasing a single-threaded one publicly. He modified code frequently, released large batches of updates at once, and disabled critical opcodes in bulk without prior testing or announcement. His governance model was one-man control over code, website, forum, domain, and messaging. He lacked patience for critics. He limited the block size to 1 MB due to limited server and bandwidth resources. He gave himself the highest administrative privilege over Bitcoin.

💎 The Departure of Satoshi Nakamoto

Satoshi became increasingly quiet starting in October 2010.

On December 12, 2010, Satoshi left his final post on the forum, disappearing from public view. Unfortunately, we lack an exact timestamp for when he lost control of the domain and Bitcoin code repository.

Satoshi stopped posting publicly in December 2010, but he didn't immediately stop Bitcoin development. For the first few months of 2011, he still replied to emails, occasionally committed code, and maintained low-key communication with a small group of developers closely involved in the project. As early as September 2010, while Satoshi was still active, Gavin Andresen obtained commit access to the SourceForge repository. In the months leading up to his final post, Satoshi had been consciously handing over operational responsibilities. This transition wasn't an abandonment; from the outside, it looked more like a carefully orchestrated operational handover.

After Bitcoin was hacked on August 15, 2010, Satoshi placed an Alert Key in the source code—the highest symbol of Bitcoin management authority. Holding it allowed one to freeze the entire network's spending capacity. In late 2010 or early 2011, Satoshi also gave the key to Gavin Andresen. Gavin was a Massachusetts-based American programmer who had been involved in the project for less than a year, and Satoshi established no public process for managing the key's use or transfer. He simply gave Gavin the key and stopped logging in.

For most of January 2011, Satoshi was offline.

On April 23, 2011, Satoshi sent his last known email. The recipient was British developer Mike Hearn, who had worked on an early Java client. Satoshi wrote a brief, characteristically concise email. The most famous line: "I've moved on to other things. Gavin and the others will take good care of it."

Satoshi's final message to Gavin read: "I hope you don't keep thinking of me as some mysterious figure; the media will just spin it as pirate money. Maybe focus on the open-source project and give more credit to the contributing developers; it helps motivate them." Gavin replied: "I hope that by talking to them directly, and more importantly, listening to their problems, they will see Bitcoin the way I do—as a simpler, more efficient, and less politically manipulated currency, rather than an anarchist tool to overthrow the system, an all-purpose black market tool."

Satoshi did not reply.

And that was it. That was the farewell.

Four days later, on April 27, 2011, Gavin Andresen released Bitcoin v0.3.21, the first client version under his leadership. On the same day, Gavin Andresen announced he had been invited to speak at CIA headquarters in the United States about how Bitcoin works and its impact on cyberspace. The actual speech took place on June 14, 2011, at CIA headquarters in McLean, Virginia.

Mike Hearn, who received Satoshi's last email, stated in a public interview that it was "probably not a coincidence" that Gavin's announcement of the CIA invitation was so close in time to Satoshi's departure. As for the true reason for Satoshi's departure—whether it was the CIA invitation, the WikiLeaks incident, legal pressures, personal reasons, or simply because the project was stable enough—no one knows. Frankly, the public record is insufficient to allow us to determine among these possibilities. Anyone claiming to know the truth is merely speculating.

What we know is that after he left, he never truly returned. All online traces went silent. The approximately 1.1 million Bitcoins in his 2009 mining wallets have never been moved (when Satoshi left, the total supply was about 6 million, and the price was $0.30). These wallets remain on-chain; anyone can view them via block explorers. They have sat idle through every price cycle, every fork, every governance dispute, every market crash and rebound.

He left. Completely.

### 3.1.2 The Suffocating Truth: When Your Cowardice Becomes the Stepping Stone for Villains to Rise

## 🎭 New Developers Demand Gavin Andresen Share Power

In 2011, Gavin Andresen obtained the highest privileges transferred by Satoshi. Others who joined the Bitcoin community around this time included: Martti Malmi, Wladimir van der Laan, Matt Corallo, Luke Dashjr, Pieter Wuille, and Gregory Maxwell. This new generation of developers began making decisions Satoshi would not have agreed with, and they became the strongest force opposing Satoshi.

In the first two years of Bitcoin's existence, its source code was hosted on SourceForge under a governance structure that was almost entirely dictatorial under Satoshi alone. Patches were submitted via email, reviewed by Satoshi, and merged or rejected by Satoshi. There was no pull request process, no public comment section. The model was simply email approval. After dictatorial power was transferred to Gavin Andresen, developers demanded Gavin share authority, suggesting they vote on matters going forward. Gavin agreed.

On October 5, 2008, Satoshi registered an account on SourceForge (nakamoto2). He used this account to create a project named "Bitcoin" on SourceForge. In September 2010, Gavin Andresen obtained commit access, and later administrative access, to the SourceForge repository. In May 2011, Gavin Andresen established the bitcoin/bitcoin repository on GitHub and, along with Wladimir van der Laan, migrated the Bitcoin project from SourceForge to GitHub. Distributed commit permissions replaced the single approver. Public comments on every code change replaced private email discussions. Thus, Bitcoin completed its de-Satoshification. Satoshi lost administrative control over the Bitcoin code.

To prevent Satoshi from reactivating the SourceForge repository, Martti Malmi publicly published the PGP key used to send code updates to SourceForge. This key had been given to Martti by Satoshi months earlier, on December 6, 2010.

On November 22, 2009, Satoshi set up the Bitcoin forum using the open-source SMF system, hosting it under the root directory of the official website bitcoin.org (accessible at bitcoin.org/smf/). He then appointed Martti Malmi as the forum moderator. In April 2011, he handed over forum administrator privileges to Martti Malmi. Two months later, on June 24, 2011, Martti Malmi himself registered the independent domain bitcointalk.org. Subsequently, in July 2011, he migrated the entire official forum database to bitcointalk.org, simultaneously closing the official forum. The official Bitcoin forum was permanently shut down, and Satoshi had no administrative access to this new server. The database of the official forum, containing Satoshi's posts from over a year, was moved entirely. However, Satoshi never used bitcointalk.org.

To prevent Satoshi from logging back into the forum, Martti Malmi manipulated the database to change Satoshi's forum account password. Later, Martti even used Satoshi's account to post some false statements.

During the 2026 COPA case, Martti Malmi testified: "If Satoshi wanted access, he just needed to ask; Satoshi never asked for such access."

Martti Malmi pocketed the official forum. The founder, Satoshi Nakamoto, needed to ask!

## 🎭 The Designated Heir: Gavin Andresen is Expelled

On December 8, 2015, *Wired* and *Gizmodo* simultaneously identified Craig Wright as Satoshi Nakamoto. Hours later, the Australian Taxation Office raided his home, and he subsequently fled to the UK.

On May 2, 2016, Craig Wright began his attempt to prove he was Satoshi Nakamoto. The day was divided into three carefully orchestrated parts.

First, Craig published an article on his website titled "Jean-Paul Sartre, Signing and Significance." Sartre famously refused the Nobel Prize in 1964, rejecting institutional authority to define his work.

Second, Craig gave interviews to the BBC, The Economist, and GQ. He said the line everyone remembers: "I don't want money, I don't want fame, I don't want adulation. I just want to be left alone."

Third, and most importantly, was the public revelation of the private key signing demonstration Craig Wright had performed for Gavin Andresen earlier in April.

Gavin Andresen described the meeting: They first conversed for several hours, during which Craig was asked about private matters known only to the two of them. Then, on a laptop, Craig signed a message chosen by Gavin—specifically, "Gavin's favorite number is eleven. CSW"—using software they had verified. The verification was successful! This proved Craig held the private key for Block 1. Gavin Andresen, under oath, explained that out of caution, he also had Craig perform a second signing using a brand new, unopened laptop, which was also successful. Gavin Andresen made the following statement to the media: **"I believe Craig Steven Wright is the inventor of Bitcoin."** Video evidence of this statement exists.

Gavin Andresen's confirmation of identity should have been the end of the story.

Hours later, Gregory Maxwell, who had risen to become CTO of Blockstream, jumped in. He immediately took action, revoking all of Gavin Andresen's permissions over Bitcoin. Subsequently, developer Peter Todd publicly announced: "Reminder, @gavinandresen's commit access was just removed; team members are concerned his account may have been compromised." Lead maintainer Wladimir van der Laan also acted decisively: "The prudent thing is to immediately remove his ownership of the 'bitcoin' organization on GitHub." These three individuals fought hard to oust him; they had all betrayed Satoshi.

In 2011, Satoshi designated Gavin as his successor. On May 2, 2016, Gavin was removed from the project. Satoshi's personally appointed successor, the sole heir to Bitcoin, and the highest-ranking spokesperson within the Bitcoin project, was expelled. By this point, Bitcoin was under the control of Blockstream, which was funded by traditional capital. To sustain the narrative, Adam Back began to surface, reluctantly being molded into a new "true Satoshi."

Adam Back as the true Satoshi: no one sued him, no conflicts, no entanglements within Bitcoin, no stories about Bitcoin. Adam Back as the true Satoshi required no private key signature, no domain registration invoice, no master email copies, no whitepaper drafts, no original source code, no cryptographic endorsement, no confirmation from Gavin Andresen, no C++ programming skills, no knowledge of Satoshi's contacts, no explanation for the name's origin. Adam Back as the true Satoshi only needed a sly smile: "no no no, I'm not Satoshi; Satoshi wants to remain hidden forever," and then the media, with their bribes, would pounce: "You are!" Adam Back just needed to smile.

Why private signature verification, and not a public signature, moving Block 1 in front of everyone? Because he couldn't. Doing so would expose him to claims for half of the 1.1 million Bitcoin fortune—the contested estate of the deceased David Kleiman. A public signature would be self-defeating; those calling for it knew he wouldn't dare. The private signing aimed to re-establish Satoshi's orthodoxy at minimal cost. But private events can be denied by anyone. They used what he feared to create a narrative and mislead the public.

## 🎭 The Supreme Metaphor of the Divine Lies in Its Eternal Absence

In the grand narrative of cryptocurrency, Satoshi Nakamoto is shaped into a flawless "techno-messiah." His successors conform to this trend, symbolizing him completely—the modern Bitcoin consensus is so unshakeable precisely because its founder is a faceless totem.

Once this living person descends from the pedestal, his mortal flaws and privileges would instantly shatter that near-religious purity. Bitcoin had long since diverged from its creator's original vision, and its greatest charm lies precisely in the founder's "absence." No one wants Satoshi to return, because a living, temperamental mortal who can modify code at will and holds immense wealth is far less beneficial to everyone's interests than a void symbol submerged in darkness. Remaining absent is his perfect fulfillment for Bitcoin.

More dramatic than this is the vast fortune in his hands. Within one year, he selfishly and ruthlessly amassed an empire of 1.1 million Bitcoins for himself.

This vast wealth is the greatest nightmare for the entire crypto world. But ironically, precisely because Satoshi is "mortal," we gain a bizarre sense of ultimate security: mortals are greedy; a mortal could never face trillions in wealth without cashing out. Today, this fortune has lain dead like a Martian rock for seventeen years. The only truth is this—that mortal named Satoshi has permanently lost control of this fortune.

A living Satoshi holding vast wealth is terrifying; but a Satoshi without Bitcoin is the most solid foundation for the entire network's consensus. How did this unparalleled genius fall into such a bizarre twist of fate, inadvertently losing his nation-sized fortune? Let us now begin to lift the veil on this historical mystery.

---

## 🏁 Chapter 6: Behind the Mask: The Ultimate Interweaving of Intellect, Capital, and Casino Chips

### 3.2.1 Satoshi Nakamoto's Secular Bankruptcy, the End of the Myth

## 🎭 The Man with 20 Companies and 30 Degrees

On December 8, 2015, two in-depth reports published on the same day simultaneously thrust Craig Wright into the public eye. The articles were *WIRED's "This Unknown Australian Genius Seldom Speaks But He Might Be Bitcoin's Creator"* and *Gizmodo's "This Australian Says He and His Dead Friend Invented Bitcoin."*

Just three hours after these two articles were published, the Australian Federal Police (AFP) and the Australian Taxation Office (ATO) raided Craig Wright's home in Sydney. Multiple journalists were stationed outside his home, taking photos. Craig Wright and his wife Ramona began packing. They gathered as many laptops and phones as possible. After leaving, Craig realized he had forgotten his passport. After the tax office finished their search, Ramona returned home and successfully retrieved her husband's passport. They immediately booked a flight to New Zealand, then traveled to Manila, eventually ending up in London. These two articles were not only the global launching point for Craig Wright's "Satoshi" identity but also triggered all subsequent international lawsuits involving him (including Kleiman v. Wright and the 2024 UK COPA case).

Craig Steven Wright was born in October 1970. His father, Frederick Wright, was a Vietnam War veteran. His parents divorced after his father's military service. Craig has admitted that his relationship with his father was complex, feeling he could never meet his father's expectations. His mother worked in early computer data entry (punch cards/paper tape), which introduced him to computers early on. His maternal grandfather, Ronald Lyman, was a signals officer in the Australian military, graduating from the Marconi Radio School. His grandfather's basement was filled with early electronic equipment, and he personally taught young Craig to program. Craig developed an almost obsessive fascination with Japanese culture from a young age; his mother recalls he would even wear full samurai armor as a teenager. To this day, he keeps samurai swords and armor in his office. During his martial arts studies, he learned about the Japanese philosopher Tominaga Nakamoto, which significantly influenced his later thinking.

| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Event |
| :--- | :--- |
| **1987** | Graduated from Padua College. Joined the Royal Australian Air Force (RAAF) after high school. Left the Air Force and transitioned into the IT industry. |
| **Early-to-mid 1990s** | Worked as an enterprise account manager at the Australian Internet Service Provider OzEmail. |
| **1997 – 1998** | Served as an IT security consultant for the Australian Securities Exchange, developing IT security systems. |
| **1997 – 2003** | Primarily worked through his own IT security consultancy, DeMorgan Information Security Systems Ltd. |
| **1998 – 2002** | DeMorgan collaborated with Vodafone on IT security projects, including firewall system deployments. |
| **1999** | Designed the underlying architecture for the world's first legal online casino, Lasseter's Online (headquartered in Alice Springs, Northern Territory, Australia). |
| **Since 2002** | Craig's primary focus was security; he had his own specialized security architecture. He served casinos and also used it for Bitcoin. He consistently used Rocks Linux as the base system for building and managing high-performance clusters. |
| **2004** | Worked as the Information Systems Manager at accounting firm BDO Kendalls, responsible for digital forensics and cybersecurity prevention. He conducted over 1200 information security-related projects for more than 120 Australian and international private and government organizations. |
| **2005** | The U.S. government cracked down hard on using credit cards, checks, and bank transfers to settle illegal online gambling debts. He began conceptualizing a token system for online gaming to circumvent international fund transfer issues. The tokens were like electronic poker chips. |
| **Since 2005** | As part of the BDO team, provided services for the Australian sports betting website CentreBet. |
| **2007 – 2010** | To operate Bitcoin, the costs of internet connectivity, servers, Microsoft software licenses, and electricity totaled approximately AUD 1.1 million. Approximately 70% of the expenditure during this period was related to Bitcoin. The mortgage on his three properties reached approximately AUD 1.4 million, leading him to later sell his farm. |
| **Sept – Dec 2008** | Craig Wright described this period as his "technical peak," sleeping only 6 hours a day and waking up to write C/C++/C# code. |
| **October 2008** | Approached BDO shareholder Alan Granger with a printed Timecoin whitepaper, seeking collaboration (meeting records exist). Granger not only refused but also placed Craig on the redundancy list two months later. |
| **December 2008** | Was made redundant by BDO, receiving severance pay. This allowed him to continue working on Bitcoin throughout 2009 while depleting his savings. |
| **Early January 2009** | Made simple modifications to two of his properties in Australia. In Sydney, he converted the garage into a server room. He also laid fiber optic cables to the Bagnoo farm, about 3 hours from Sydney, converting some sheds and rooms into a server farm, filling them with multiple "second-hand industrial servers" discarded by casinos, forming a server cluster. |
| **January 2009** | Founded Information Defense Pty Ltd, which acquired and maintained code for multiple online casinos and sports betting businesses. |
| **January 9, 2009** | Craig Wright posted a blog stating: "The beta version of Bitcoin goes live tomorrow. It's decentralized... We will try until we succeed." |
| **March 2009** | Founded Integyrs Pty Ltd for algorithmic modeling and analyzing online poker network game code. |
| **November 2009** | Founded GreyFog to develop security software. |
| **January 2011** | Traveled to Venezuela and also applied for a formal Australian police officer position. By this time, he had collaborated with the police multiple times, developing several forensic tools, one of which involved data mining analysis. |
| **February 2011** | Craig Wright and David Kleiman established the W&K Tulip Trust. His finances were very tight, and he could no longer afford lawyers, auditors, and accountants. |
| **Early 2013** | The U.S. government seized Liberty Reserve's funds, shutting it down. His funds for servers, bandwidth, and daily operations were also cut off. |
| **2013** | Craig Wright registered over a dozen interconnected technology and investment companies in New South Wales, Australia, including DeMorgan Ltd, Cloudcroft, Coin-Exch, Denariuz, Hotwire PE, etc. |

In July 2015, Craig Wright resigned as director of 12 companies: Cloudcroft Pty Ltd, Coin-Exch Pty Ltd, Daso Pty Ltd, Demorgan Holdings Pty Ltd, Demorgan Ltd, Denariuz, Ezas Pty Ltd, Integyrz Pty Ltd, Misfit Games Pty Ltd, Interconnected Research Pty Ltd, Zuhl Pty Ltd, and Pholus Pty Ltd. He retained directorships at only 3 companies: Hotwire Preemptive Intelligence Pty Ltd, Panopticrypt Pty Ltd, and Hotwire PE Employee Share Plan Pty Ltd. These companies, after Craig Wright relocated to the UK, became entangled in extremely complex private disputes and tax investigations. As of now, queries via the ASIC Connect system often show them as "insolvent companies."

Craig Wright holds 30 degrees from 22 universities, including 6 PhDs.

Craig Wright has been married twice.

He married his first wife, Lynn Wright, in 1996. They met on an online dating platform; Craig was 26, Lynn 44. Their first child (a son) was born in 1999. The relationship experienced conflicts and strain towards the end of the marriage, leading to a formal separation in January 2011.

His second (current) wife is Ramona Watts. Ramona had previously been Craig's employee, and their relationship developed through daily work. They formally registered their marriage around 2012 and have two children together.

### 3.2.2 A Fellow Traveler through the Jungle: Satoshi Nakamoto and Dave Kleiman's Genesis Gamble

## 🎭 You Might Have Received Emails from Satoshi Nakamoto

In the article *"Two steps forward, one step back,"* Craig Wright mentioned that when Bitcoin launched in 2009, he had a cluster of 67 servers. However, most were CentOS, Red Hat, and Solaris systems used for DNS and sendmail. Because Bitcoin needed to run on Windows, he could only find 10-12 computers for that purpose.

What were the other 50+ servers for? While he didn't explicitly say, those familiar with network technology can infer.

Besides writing code for casinos, Craig Wright also provided email marketing services for them. The technical barrier to bulk spamming is avoiding blocks; the core is bypassing recipients' spam checks (Yahoo, Hotmail, Gmail). In 2008, anti-spam primarily checked SPF records and reverse DNS lookups. Thus, he needed to build large numbers of cheap domain DNS records on CentOS and Red Hat to legitimize identities, bind thousands of IPs, and use Sendmail for multi-IP round-robin sending. Solaris, with its extremely robust multithreading model, could handle massive spam queues.

Online gambling is a "high-value, low-conversion" industry; marketing relies on blanket coverage and aggressive data scraping. If you don't grasp the concept of 50+ servers, consider this: 50 servers could send 50 million spam emails per day (theoretically).

Imagine 50+ servers: 10 sending spam at 500 emails per second each, 40 slowly resending bounced/queued emails while randomly switching IPs, and the rest running crawlers and analyzing logs. Go check your email: if you received "online gambling" emails around 2008-2009, they might have been sent by Satoshi Nakamoto.

The extreme needs of the online gambling industry—money laundering, cross-border settlement, and protection against judicial seizure—ultimately drove this technical genius, who was a master of network infrastructure and black-hat marketing, down the ultimate path of cryptography.

## 🎭 Satoshi's Only Comrade, David Kleiman

In December 2008, a paper titled *"Rewriting Hard Disk Data: The Great Controversy over Erasure"* was published in *Lecture Notes in Computer Science*, authored by Craig Wright and David Kleiman. This was the genuine link demonstrating their technical collaboration on the eve of Bitcoin's birth.

Their collaboration extended beyond papers. Craig Wright's two specialties were developing game software and writing low-level code. He was proficient in C but even more expert in MASM, Forth, and other low-level systems. Part of his work involved developing gaming software, much of it for licensed casinos like Australia's Lasseters Online Casino. He also built a massive international online casino for Playboy Gaming. Consequently, he amassed a large collection of online casino software. At that time, online gaming was still in its early stages, and such software could fetch high prices.

In 2008, Craig Wright began looking for buyers for casino software. His target clients weren't casino owners. The buyers were technical developers writing code for casinos—especially those "who don't respect intellectual property and advocate open source."

Casino software is a vertical niche requiring targeted searching. The most direct method was joining discussion groups: joining open-source, hacking, and strong-privacy newsgroups, then traversing their archives and extracting email addresses. The Cypherpunks entered Satoshi's field of vision. The high-quality individuals here must have achieved some effect, attracting Satoshi's attention. He had never even posted there before; his first email was the Bitcoin whitepaper. Satoshi recognized the quality of this mailing list. The Cypherpunks stood out among thousands of mailing lists. Browsing the archives from that period indeed feels like reading a trans-temporal academic salon. That "purity" wasn't just in the text but in their unique communication ecology. Discussions were fiery; to prove a crypto protocol's security or the feasibility of an anonymous remailer system, they would engage in dozens of email threads, filled with dense mathematical formulas. This pure intellectual exchange is rarely seen on today's internet social platforms.

January 2009 was the hardest time for Craig Wright. Redundant, to sell software, he collaborated with David Kleiman. They searched for clients globally, primarily through mass emailing. They found clients in Costa Rica and Panama, but selling this code was illegal in those countries. This meant David Kleiman bore the greatest risk in selling the code. Craig in Australia could receive money legally, but David couldn't legally repatriate the funds he earned to the U.S. Selling software was Craig Wright's income source from 2008 to 2011. To boost income, Craig also performed security consultancy work for clients, custom-developing various exploits, covert channel software, and reverse engineering tools. They weren't wealthy; Craig had mortgaged his properties, and David was confined to a wheelchair.

Craig Wright wrote code; David Kleiman found clients. Craig Wright collected payments; David Kleiman handled sales.

In March 2009, Craig and David met at Disneyland in the U.S. This laid the groundwork for their subsequent deeper collaboration. After Bitcoin launched, David helped run two nodes. Later, David told Craig he had mined approximately 350,000 Bitcoins.

From 2009 to May 2011, Craig and David earned income from selling casino software. But after May 2011, Bitcoin surged from $0.70 to over $19 in one month, a 27-fold increase. Satoshi had become a multimillionaire. One of W&K's tasks upon its founding in early 2011 was operating miners to produce 12,000 newly mined Bitcoins monthly. These Bitcoins were enough to cover their operational and living expenses. After June 2011, they had passed their most difficult period.

When money was no longer a problem, making it legal became the biggest issue. Craig and David began registering companies.

On February 13, 2012, David Kleiman and Carter Conrad founded Computer Forensics, LLC in Florida, USA, each owning 50%. On February 13, 2013, Patrick Paige, a colleague of David's from the police department, joined, with all three managing members holding equal 33.33% ownership. The company's core business was computer forensic services. (The company's standing in the U.S. computer forensics industry is illustrated by a 2009 email mentioning that David Kleiman had cloned hard drives for Jeffrey Epstein, providing data forensic services.)

From 2012 to 2013, Craig Wright registered numerous technology and investment companies in New South Wales, Australia, including Cloudcroft Pty Ltd, Coin-Exch Pty Ltd, Daso Pty Ltd, Demorgan Holdings Pty Ltd, Demorgan Ltd, Denariuz, Ezas Pty Ltd, Integyrz Pty Ltd, Misfit Games Pty Ltd, Interconnected Research Pty Ltd, Zuhl Pty Ltd, Pholus Pty Ltd, Hotwire Preemptive Intelligence Pty Ltd, Panopticrypt Pty Ltd, and Hotwire PE Employee Share Plan Pty Ltd.

In February 2013, Bitcoin stabilized above $20 (exceeding the June 2011 peak of $19). Over the next three months, Bitcoin rose steadily, reaching a then-record high of $160 by April 26th. This surge was driven by Liberty Reserve, involved in an estimated $6 billion in money laundering. A month later, on May 24th, Liberty Reserve founder Arthur Budovsky was arrested in Spain (ultimately sentenced to 20 years), and on the same day, Liberty Reserve was permanently shut down. Craig Wright's several million dollars held in Liberty Reserve were also seized.

Since a motorcycle accident in 1995, David Kleiman had been paralyzed from the waist down and reliant on a wheelchair. His paralysis led to various complications that persisted throughout his life. These included pressure sores from immobility, which often became infected and required constant care. These ulcers also caused infections in other parts of his body, including his bladder and bones.

In September 2010, David fell while showering and couldn't get up. He was hospitalized. Due to infected MRSA ulcers, he spent the rest of his life rarely leaving medical centers, usually only for computer forensics tasks with the police. After hospitalization, he was prescribed Percocet and Fentanyl—both extremely potent painkillers. This hospitalization lasted 884 days, until his temporary discharge on March 21, 2013, when Bitcoin broke its $40 all-time high. He was readmitted a few days later, with his condition worsening to the point where nurses were needed to turn him.

On April 14, 2013, David Kleiman again left the hospital against medical advice. At this time, Bitcoin was oscillating around the $100 range, with exuberant market sentiment; the media and community were euphoric. This was a historic moment. David Kleiman forced his way home to watch the market. On April 26, 2013, the day David was found dead, Bitcoin reached a new high of $162. At this point, 1.1 million Bitcoins were worth $180 million. David's 350,000 were worth over $50 million.

Records show David Kleiman received little family support during his illness. There was only continuous communication between Craig Wright and David. David's computer use in the hospital was limited; in emails with a friend and former colleague, he complained about only having five minutes to use the phone during his stays. Limited communication and computer access, with Bitcoin surging and David's wealth exploding, he forcibly discharged himself.

David Kleiman died less than two weeks after leaving the hospital. According to the Palm Beach County Medical Examiner's Office report, the scene of death was gruesome: blood and feces on his wheelchair, alongside several empty bottles of bourbon whiskey and a loaded handgun. The official cause of death was listed as natural. A Palm Beach coroner stated that David had used cocaine, painkillers, and alcohol before his death. The toxicology report showed David used multiple sedatives—Xanax, Ativan, and Valium—in the days before his death, along with cocaine residue. The blood alcohol content was slightly over 0.10% (legal intoxication). The cocaine test was qualitative, not quantitative, so the exact amount in his urine is unknown, only that it exceeded the minimum detection limit (0.150 mg/L). Perhaps he wasn't using cocaine at the time of death, but he was intoxicated and needed strong painkillers. The autopsy report showed an intact nasal septum, so he wasn't a habitual user. No fatty liver indicated he wasn't an alcoholic. The sores on his feet and buttocks meant he spent much time sitting without adjusting position. David Kleiman was discharged with "deep and large ulcers" he couldn't feel, but if untreated, they could lead to severe infections—likely meaning he decided to "leave on his own terms," self-medicating with drugs and alcohol.

He was only 46. He had been in the hospital for over 2 years. He first left when Bitcoin broke $40, then returned as his condition worsened. He left again when Bitcoin broke $100. He had gastrointestinal bleeding causing pain; drinking worsened his condition, and he even contemplated suicide. He had no family support or care. He wanted one last celebration with Bitcoin. He died at the moment Bitcoin hit a new all-time high, as he had truly become a millionaire.

David Kleiman was born in 1967 and adopted by Louis and Regina Kleiman of Palm Beach Gardens (Regina Kleiman has passed away, Louis is now 96). In 1986, David Kleiman began serving in the U.S. Army as a helicopter technician. He returned from service in 1990 and began working at the Palm Beach County Sheriff's Office a few years later. His training officer was Paige, and they were very close. David gave Paige a computer and even went to her home to install games for her daughter. Their jobs required them to patrol together.

David Kleiman carried a high-security USB drive with him at all times. Paige believes it was a Corsair brand drive, encased in aviation-grade aluminum alloy—expensive, hardcore, high-performance, heavily armored. According to Paige, the USB drive was handed over to his non-biological brother, Ira Kleiman, with whom he had a poor relationship and had been estranged for years. Ira Kleiman would cause trouble for Satoshi. He would expose Satoshi's identity.

---

# ❤️ Part Four: The Fall of Fortune—Bitcoin Forever Lost Under Cryptographic Deadlock

## 🏁 Chapter 7: The Tulip Trust's Defense and Collapse

### 4.1.1 The Price of Absolute Security: Private Key Sharding and Trust Mechanism

## ⏱️ Craig Wright's Story

## 🔑 *1.1 Million*: Craig Wright Lost the "Tulip Trust's" Bitcoins

On February 14, 2011, David Kleiman incorporated W&K Info Defense Research LLC ("W&K") in Florida. Craig Wright and David Kleiman were partners, each owning 50% of the company. The company had genuine operational documents, real tax returns, real government contract bids, and hundreds of pages of authentic text messages between them, spanning from 2009 until the day before David's death in 2013. W&K served two purposes: managing the 1.1 million Bitcoins in the Tulip Trust and operating miners to fulfill the task of mining 12,000 new Bitcoins monthly (at the time, the entire network was mining about 210,000 Bitcoins per month).

Note the establishment date of W&K: February 2011. At that time, Bitcoin's historical high was around $0.30; Bitcoin was not yet valuable. Yet Craig was facing numerous problems: emotionally, he had just separated from his wife Lynn and begun a new relationship with his colleague Ramona; financially, he was being targeted by the Australian Tax Office, his house was mortgaged, and he had monthly company operating costs and electricity bills. He was facing bankruptcy.

On one hand, regarding family, Craig reached an agreement with Lynn to sacrifice all rights to his assets to protect the Bitcoins. Essentially, he would leave the marriage with nothing to avoid dividing the Bitcoins in the divorce, fearing she would sell them and ruin the project.

On the other hand, under Australian law, Craig considered the scenario of his own death. He stipulated that Ramona, inheriting the Bitcoins, must use them to expose the lies and fraud perpetrated by Australian Tax Office official Adam Westwood. Subsequent testimony indicated that Adam was aware Craig held Bitcoins.

Craig Wright had to prevent both individuals from having any claims on the Bitcoins. The only secure method was: I want to give them to you, but I can't.

Why were these 1.1 million Bitcoins so important? Not only because they were mined in 2009 and could prove his identity as Satoshi, but crucially, as global hashing power flooded in, his share was instantly diluted to two-thousandths of the network. If even he was so diluted, it would be impossible for any individual to amass such a vast amount of Bitcoin in the future. Although the value was only $0.30 at the time, Craig already envisioned the future.

He thought of David Kleiman. Satoshi chose to sequester these Bitcoins; they could expose his identity and would appreciate in value. The safest method was through trust control. The Tulip Trust was born. In the trust terms dated September 5, 2011, Satoshi set the withdrawal date for his 1 million Bitcoins: January 1, 2020.

Two additional conditions were attached: Bitcoins could be borrowed for Bitcoin R&D if needed, and the trust must retain at least 100,000 Bitcoins as a balance.

The "Tulip Trust" was a family trust structure (a legal document + password structure located in the UK). This trust held a total of 1,100,111 Bitcoins. All 1.1 million were mined by Craig Wright during 2009, using multiple servers and computers with multi-threaded mining.

The Bitcoin software in 2009 (v0.1.0 to v0.3.0) was extremely primitive; its storage mechanism was vastly different from today's: there were no "seed phrases." All private keys were stored directly in a binary file named `wallet.dat` located in the data directory. `wallet.dat` would generate 100 private keys by default, using one for each block mined (50 Bitcoins). As mining progressed, the software would exhaust these 100 pre-generated keys and automatically generate new ones in the background. Thus, Craig Wright mined at least 20,000 blocks, meaning all `wallet.dat` files (initially, Satoshi used over a dozen Windows servers for mining, so there were at least a dozen `wallet.dat` files) contained all the private keys, each representing 50 Bitcoins. A private key is a 256-bit hexadecimal string, like: `4f8b2c9d1a3e6f7b5a8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a`.

After establishing the Tulip Trust, Craig Wright and David Kleiman designed a scheme to encrypt all private keys using a cryptographic technique known as Shamir's Secret Sharing (SSS). Specifically, they used the SSS algorithm to split the private key pool into 15 "shares," setting a threshold: any 8 of the 15 shares could fully reconstruct the private keys. (e.g., ASDFG split into 3 shares ASD, ASFG, DFG; anyone with 2 shares could reconstruct the full key.)

Craig Wright and David Kleiman fragmented the private key pool file and distributed the shares to different legal entities or individuals (trustees). This ensured that even if he were threatened, no one could unilaterally seize the Bitcoins. David Kleiman himself was also a trustee.

This is the author's speculation: Based on the 15-share, 8-threshold setup, Craig Wright and David Kleiman likely held at least 8 shares between them, allowing them to meet the threshold if they agreed. The other 7 shares were distributed to 7 other trustees, probably chosen by Craig and David separately, without each other's knowledge. For reasons of security, confidentiality, or unknown circumstances, these trustees have not come forward.

After gathering 8 shares, a "decryption instruction" was required for activation. The process was: "collect at least 8 shares → merge shares via SSS → enter decryption instruction to activate → perform AES-256 decryption to ultimately export the private keys." This nested combination of SSS (recovery key) + AES (decrypt data) is the highest level of protection in cold storage. SSS manages "ownership": it determines who can participate in decryption (the 8 people). AES manages "storage": it ensures that even if the data is copied, it remains unreadable gibberish without the key reconstructed via SSS.

There were a total of 5 decryption instructions; any 2 could perform decryption. Craig Wright knew 4, while David Kleiman kept the other one with someone Craig didn't know. These 4 decryption instructions have been exposed through emails:
`56EC 672A E867 266A 5E21 1514 A0DA 0EB2 E545 EB78`
`D8B7 E697 59EF D7FE E84C F51B 4FF1 CFEB C941 FE6D`
`0AC1 8AFE 1F8D 3512 9E15 6909 B188 BF41 1F55 6274`
`DE4E FCA3 E1AB 9E41 CE96 CECB 1B0C 9E86 5EC9 48A1`

Craig Wright testified in court that he currently holds only a small number of shares (insufficient to reach the threshold of 8). He claimed to lack the necessary "threshold count" to fully reconstruct the private keys, which was his stated reason for being unable to perform an immediate "on-the-spot signature" in court.

The shares held by David have physically disappeared. Craig Wright most likely cannot gather 8 shares. Unable to find even one of David's shares, the Tulip Trust faces cryptographic failure. In objective effect, this has resulted in the 1.1 million Bitcoins being deadlocked.

Why can't Craig Wright gather 8 shares? How many does he have? How many is he missing? Does he know all the trustees? Is there still a chance to retrieve them? The court proceedings did not disclose such information, nor is it likely to be revealed. After the Tulip Trust was established, Bitcoin began its meteoric rise from late 2013. By 2025, it had soared to $120,000. The 1.1 million Bitcoins from 2009, constantly monitored on-chain, have not seen a single coin sold. This speaks volumes.

What is certain is this: The Bitcoin client in 2009 (v0.1.0 to v0.2.x) had no wallet encryption feature. All private keys stored in the `wallet.dat` files were in plaintext. Craig Wright had full access to all these plaintext private keys. If he had backed them up, he wouldn't have lost control.

Craig Wright mentioned that if he could recover David Kleiman's stored belongings (like USB drives, paper records, or formatted hard drives), he could use his decryption instructions to attempt recovery or reconstruction. Unfortunately, after David's death, his family, while sorting his belongings, inadvertently disposed of (destroyed) the physical media containing the crucial keys or shares. David Kleiman's death and the subsequent actions of his family led to a "cryptographic catastrophe," rendering the once-controllable assets deadlocked.

Putting everything else aside, looking at the facts: David ensured that after his death and his own removal from the equation, Satoshi could not access the keys. Craig Wright trusted David completely; he kept no backup and bore the consequences.

### 4.1.2 Disaster Strikes: Destruction of Relics and Asset Deadlock

## 🔑 *100 Billion Dollars*: Not Your Luck, Three Big Brains Lost Bitcoins

The Tulip Trust held 1.1 million Bitcoins, with Craig Wright and his girlfriend as beneficiaries and David Kleiman as one of the trustees. Neither Craig nor David could unilaterally make decisions within the trust. The trust's original intention was to ensure that even if Satoshi were arrested and his assets seized, no one could unilaterally move the assets. They decided to fragment the original private keys and then completely destroy the plaintext originals. By actively relinquishing direct possession of the private keys, they created a legal and cryptographic defense: "I truly cannot access the assets." Two very smart people, but a third was coming.

The Tulip Trust's setup did consider the possibility of one party's sudden death. For example, if Craig Wright died, ownership would transfer to Ramona Watts. The trust was supposed to automatically dissolve 15 months after David Kleiman's death, releasing Craig from its constraints and allowing him direct access to the Bitcoins. However, after David's death, Craig Wright did not obtain full access, indicating that some step in the process had failed. The problem clearly lay in the disappearance of the data held by David.

David Kleiman was a U.S. computer forensics expert who was wheelchair-bound due to a motorcycle accident. He carried a nearly ever-present Corsair USB drive with an aluminum/titanium alloy shell—a military-grade, ruggedized drive.

On April 26, 2013, 46-year-old David Kleiman died at his home. His colleague Patrick Paige helped sort his belongings. The aluminum-encased USB drive, along with all his computers and phones, were officially handed over to Ira Kleiman. (David was unmarried and had no children. His adoptive father was the heir to all his estate, which then passed to Ira Kleiman. The two brothers were not blood-related.)

On May 2, 2013, Craig Wright published an article titled *"Today's manifesto..."* expressing his memories of David Kleiman. On the other hand, Craig was also angry with David for not telling him how bad his health really was.

In May 2013, Ira Kleiman, after taking over his brother David's estate, reformatted the laptops and USB drive and began using them for personal purposes. He also disposed of David's phone. During the litigation, approximately 15 external hard drives and USB drives were submitted as evidence (acknowledged in court testimony).

On February 11, 2014, Craig Wright suddenly contacted Patrick Paige and Ira Kleiman, asking about the safety of the computers and USB drives in David's office and home, requesting them to search for `wallet.dat` (the core Bitcoin wallet data file). Craig told Ira that his brother David held a substantial amount of Bitcoin.

In 2015, Ira Kleiman rejected a third-party offer of $6 million for 90% of the intellectual property rights in his brother's estate (with Ira retaining 10%). Ira wanted more. He attempted to force Craig to liquidate the company and threatened to publicly expose Craig Wright as Satoshi Nakamoto. Note that at this point, it was already certain that due to Ira erasing the data, David's shares were missing, making it impossible to gather 8 shares.

In November 2015, Ira Kleiman sent the documents and files Craig had shared with him during negotiations to WIRED and Gizmodo, posing as a hacker. On December 8, 2015, both outlets published simultaneous in-depth reports, thrusting Craig Wright into the public eye.

On February 14, 2018, Ira Kleiman sued Craig Wright for embezzling 1.1 million Bitcoins. The U.S. lawsuit "Kleiman v. Wright (9:18-cv-80176)" commenced. The complaint detailed the founding and operation process of Bitcoin.

On November 17, 2021, during the trial of Kleiman v. Wright (Day 11), technical expert Nicholas Chambers testified that after David's death, 4 of the storage devices had been reformatted, and data on 13 others had been overwritten to varying degrees. The expert found that encrypted folders named "Do Not Delete" had existed on these devices, but the original data within them was now completely unrecoverable.

In March 2022, a federal court in Miami, Florida, ruled that Craig Wright must pay $143 million in damages. The jury felt Ira Kleiman was entitled to some compensation, but the court did not recognize Craig Wright as Satoshi Nakamoto.

The irony of the Kleiman v. Wright case is that a trust designed to protect family interests turned into a tragic verdict. Consider the trap Craig Wright was in. Both sides of the litigation, for their own benefit, needed to assume Craig Wright was Satoshi Nakamoto. This meant Craig was trapped by a situation he himself had created. If he admitted to being Satoshi, he faced liability for half of the 1.1 million Bitcoins (as David's estate, due to the 50/50 W&K ownership). If he recanted, claiming he wasn't Satoshi, he would be admitting to years of perjury and fraud, essentially fraud charges. Either choice would exact a devastating toll. It was precisely on this basis that Craig Wright was evasive when proving his identity. His witnesses, Ian Grigg, Uyen Nguyen, and Joseph Vaughn-Perling, were also evasive.

Satoshi was a cautious, thoughtful person who spent years erasing his tracks. After David Kleiman's death, the scant remaining evidence likely disappeared completely. Satoshi feared hacking, extortion, and legal seizure. He built defenses using law and cryptography, but ultimately found himself locked out by the very processes he had constructed. Under the absolute iron law of cryptography, he had permanently and irreversibly lost control of his Bitcoins and that immense fortune.

Satoshi was a mortal. May 2016 was the darkest period of Craig Wright's life. Having fled to the UK, he was pushed into the spotlight by new partners. Facing the cameras of the BBC and The Economist, he was compelled to promise that fatal signature verification. As a mortal who had lost 1.1 million Bitcoins, facing the collective betrayal of the core Bitcoin community members, his spirit completely collapsed. He stabbed himself in the neck. He was rushed to the emergency department of St. George's Hospital, where his injury was classified as "Major Trauma." After his release, he wrote on his blog, *"I'm Sorry"*: "I broke down, I didn't have the courage, I couldn't do it..."

He gave up proving himself. He had lost 1.1 million Bitcoins.

---

## 🏁 Chapter 8: Desperate Struggles and Absurdity of Fate

### 4.2.1 The Predicament and Futile Search for Private Keys

## 🎭 Efforts Made by Satoshi Nakamoto to Recover 1.1 Million Bitcoins

David Kleiman passed away in late April 2013 at his home in Palm Beach Gardens, Florida, with his body discovered on April 26th. About a week later, Dave's colleague Carter Conrad published an obituary. On May 2, 2013, Craig Wright, upon learning of Dave's death, posted an article expressing his remembrance. On February 11, 2014, Craig Wright suddenly reached out, risking exposure of his Satoshi identity, to inquire about the safety of the computers and USB drives in Dave's office and home.

These timestamps confirm two things: first, Craig knew of David's death within days but did not immediately inquire about the computers and USB drives. Second, it was only 9 months after Dave's death that Craig began actively seeking contact, hoping to obtain the computer and USB drive data.

What happened during those 9+ months?

It is certain Craig Wright attempted to recover the 1.1 million Bitcoins in the Tulip Trust but failed; he couldn't gather 8 of the 15 private key shares. So, he thought of seeking cooperation from David's estate heir. Before approaching him, he needed to cash out some money.

The Bitcoins held by Craig and David's jointly owned W&K company consisted of two main parts.

The first part was the 1.1 million Bitcoins mined in 2009, plus another 350,000 mined in the first 8 months of 2010, totaling 1.45 million. These were merged into the Tulip Trust (with an address list), belonging solely to Satoshi Nakamoto.

The second part was Bitcoins mined in the company's name, used for operations, expenses, market making, etc. This part was further divided: approximately 416,475 in 9 addresses, 40,000 in 1 address for emergencies, 3,518 in another, and 34,512 more consolidated from mining operations after David's death (totaling 494,505). Another portion was used for market-making on Liberty Reserve (with no specific number, but estimated around 10,000-100,000 based on the millions lost when Liberty was shut down).

By September 2013, Craig Wright held nearly 2 million Bitcoins (1.1 million + 350,000 + 490,000 + 10,000+).

Between October 16 and 22, 2013, Craig Wright sold 58,916 (34,512 + 24,404) Bitcoins from two addresses at around $160, cashing out approximately $9 million. Considering subsequent events, this cash-out was likely intended for Ira Kleiman.

In December 2013, Bitcoin broke $1,000.

On February 11, 2014, Craig Wright contacted Dave's colleagues and relatives, hoping to obtain the computers and USB drives from David's office and home.

Initially, Craig Wright and Ira Kleiman got along. Ira was understandably excited about the immense wealth, and Craig seemed willing to exchange cash for the data he held. Ira Kleiman had grown up in a broken home, raised by his mother, and had almost no contact with David Kleiman.

Craig Wright knew Ira Kleiman was in financial difficulty and made him an offer he believed was impossible to refuse: $12 million and the position of company director with a $30,000 monthly salary for 30 hours of work per month.

Ira Kleiman refused. It was more than most could imagine, more than most on earth dream of. He refused. He didn't want to be a director running a company; he wanted to loot it, divide the money. He reasoned that since W&K was legally 50/50, he was entitled to half of the 1.1 million Bitcoins.

Ira Kleiman had leverage. Before meeting Craig Wright, he was in financial difficulty with a mortgage of several hundred thousand dollars. But soon, he became suddenly wealthy, clearing all debts and buying an additional $400,000 house. We don't know exactly how many Bitcoins he found. But David had told Craig he mined around 350,000 Bitcoins in 2009-2010 (the amount from 3-5 personal computers), and he had indeed helped Craig run at least 2 nodes starting in January 2009.

What is certain is that the 1.1 million Bitcoins in the Tulip Trust and later mined coins were not lost, as the 1.1 million have never moved, and Craig has always controlled the 11 consolidation wallets from mining operations.

It is also certain that Ira Kleiman must have discovered some Bitcoin private keys among his brother's legacy; legally, these were part of his brother's estate, and he could legitimately own them. These funds also gave him the leverage to sue Craig Wright in 2018. Ira's lawsuit put Craig in a very awkward position, as he had already acknowledged in writing his partnership with David Kleiman. So, it seemed his only way to avoid paying David's half of the Bitcoins was to claim there were no Bitcoins and that he was not Satoshi Nakamoto.

The deterioration of the relationship between Ira Kleiman and Craig Wright led Craig to cash out more Bitcoins again, this time reaching $120 million.

On March 7, 2014, Craig Wright sold 261,114 Bitcoins from 5 addresses (30,000 + 40,000 + 40,000 + 40,000 + 111,114) near $600. This sell-off directly drove the price from $600 down to $350, netting approximately $120 million. Craig moved this money back to Australia through his company Hotwire. With such a large sum, he paid a huge amount of tax. Unwilling to accept this, Craig began forging documents, using his dozen registered companies to claim over $12 million in refunds, including $9.6 million in R&D tax incentives and $3.1 million in GST refunds. These forged documents for tax refunds became the irrefutable evidence used to blacken Satoshi's name. Because he had a history of forgery, everything he did was supposedly forged, including his identity as Satoshi.

In 2015, a third party, acting for Craig Wright, offered Ira Kleiman $600 million for 90% of his brother's estate (primarily intellectual property). In November 2015, angered, Ira chose to expose Satoshi's identity.

Returning to the earlier topic: 15 shares, needing only 8, why couldn't they be gathered? Because when the private keys were sharded in 2011, Bitcoin was worth only about $0.30. After Craig Wright and David Kleiman finalized the encryption plan, David was the one who executed it. Looking at the results, David ensured from 2011 that his cooperation was necessary for key reconstruction. For example, of the 15 shares, he might have only truly handed out 7. David Kleiman had been hospitalized long-term by then and had concealed his illness from Craig Wright. Even at the end of his life, knowing his health was deteriorating, numbing the pain with heroin and alcohol, with a loaded pistol nearby, with no one to care for him, and having clearly lost the ability to safeguard the private keys, he still failed to arrange for their transfer.

Satoshi underestimated human nature. He was also a poor judge of character. Among his followers, except for his direct disciple Gavin Andresen, all later betrayed him. For their own benefit—from Adam Back, to the cypherpunk community, to exchanges, to founders of altcoins—they all did their utmost to suppress him. Satoshi's identity was still dangerous in 2013, as subsequent events like Megaupload, Silk Road, Silk Road 2.0, Mt. Gox, Exit Scam, Sheep Marketplace, and Black Market Reloaded had governments worldwide digging for Satoshi. Before 2015, Bitcoin grew and stumbled in a brutal environment of "hacks, asset thefts, drug deals, crashes, and scams."

David Kleiman was 46 when he died. Had he been healthy, by 2015, when people were beginning to mythologize Satoshi, he would have undoubtedly become the true Satoshi, as he was the only one with control over the earliest 1.1 million Bitcoins. No signature would have been needed; that immense fortune itself would have been irrefutable proof.

Craig Wright had no backup. From the moment he handed over the private keys, he was no longer the owner of that wealth. This is my speculation from a human nature perspective, assuming the worst of David Kleiman. It's not baseless; Adam Back is a living example, his followers are living examples—the temptation of Bitcoin is immense.

---

The W&K company addresses disclosed on October 9, 2013. These addresses, outside the Tulip Trust, were acquired through mining, market making, and purchases. Satoshi maintained control over them until the 2020 hacking incident.

| Address | Deposit Time | Deposit Amount | Withdrawal Time | Balance / Latest Amount |
| :--- | :--- | :--- | :--- | :--- |
| 1FJuzzQFVMbiMGw6JtcXefdD64amy7mSCF | 2010-11-08 16:32:00 | 6,999 | Unmoved | 6,999 |
| 12ib7dApVFvg82TXKycWBNpN8kFyiAN1dr | 2010-05-13 08:22:38 | 31,000 | Unmoved | 31,000 |
| 1FeexV6bAHb8ybZjqQMjJrcCrHGW9sb6uF | 2011-03-01 10:26:19 | 79,957 | Unmoved | 79,957 |
| 1ALXLVNj7yKRU2Yki3K3yQGB5TBPof7jyo | 2010-07-24 23:35:23 | 4,000 | Unmoved | 4,000 |
| 16cou7Ht6WjTzuFyDBnht9hmvXytg6XdVT | 2011-06-14 17:29:36 | 53,000 | 2016/6/2 - 2018/05/03 | 0 |
| 1LXc28hWx1t8np5sCAb2EaNFqPwqJCuERD | 2013-08-13 17:12:26 | 34,512 | 2013-10-16 17:21:27 | 0 |
| 18JPragfuDVHWWG8ABQ15cghJFetnXUjBD | 2012-11-24 01:22:16 | 24,404 | 2013-10-22 17:17:58 | 0 |
| 1MyGwFAJjVtB5rGJa32M6Yh46cGirUta1K | 2011-11-16 05:45:03 | 30,000 | 2014-03-07 05:34:54 | 0 |
| 16Ls6azc76ixc9Ny7AB5ZPPq6oiEL9XwXy | 2011-11-16 05:38:46 | 40,000 | 2014-03-07 05:34:54 | 0 |
| 1cXNTyXj4xPGopfYZNY5xfSM1EPJJvBZV | 2011-11-16 05:59:08 | 40,000 | 2014-03-07 05:34:54 | 0 |
| 12HddUDLhRP2F8JjpKYeKaDxxt5wUvx5nq | 2011-11-16 05:38:46 | 40,000 | 2014-03-07 05:34:54 | 0 |
| 1933phfhK3ZgFQNLGSDXvqCn32k2buXY8a | 2011-07-02 02:42:15 | 111,114 | 2014-03-09 23:01:00 | 0 |

### 4.2.2 Theft Again: The Loss of 110,000 Coins

## 🔑 *110,000*: Craig Wright Lost "Self-Custodied" Bitcoins

On February 8, 2020, Craig Wright discovered a mysterious, unauthorized router in his home. Subsequently, an encrypted RAR archive on his home computer was deleted.

This RAR file was encrypted and contained 37 GB of data, including a `wallet.dat` file holding private keys. By this time, `wallet.dat` had encryption capabilities; it was generated by the Bitcoin wallet software Electrum and required the correct password to open and use the private keys for transactions. Losing this file meant losing control of the Bitcoins.

Craig Wright disclosed the wallet addresses `1FeexV6bAHb8ybZjqQMjJrcCrHGW9sb6uF` and `12ib7dApVFvg82TXKycWBNpN8kFyiAN1dr`. These two wallets contained a total of 79,956 + 31,000 = 110,956 Bitcoins. On-chain analysis also suggests that 4,000 Bitcoins in address `1ALXLVNj7yKRU2Yki3K3yQGB5TBPof7jyo` also belonged to Craig Wright. So he lost at least 114,956 Bitcoins.

At this point, Craig Wright possessed the password for the RAR file and the password for the `wallet.dat` file. But he only had the passwords.

The hacker had the RAR file (and the `wallet.dat` file contained within it). But the hacker did not have the passwords.

To move the Bitcoins, the hacker needed first to crack the RAR archive's password, then crack the `wallet.dat` password. As of now, because the Bitcoins haven't moved, it's certain the hacker has not fully cracked both passwords. Technically, cracking the RAR password is relatively easier, with many tools available. But cracking `wallet.dat` relies on brute force; if the password is complex enough, it's an impossible task.

The 79,956 Bitcoins in address `1FeexV6bAHb8ybZjqQMjJrcCrHGW9sb6uF` were purchased by Craig Wright in February 2011 via the Russian exchange WMIRK, using Liberty Reserve Dollars, and transferred to the wallet on March 1, 2011. Craig Wright earned Liberty Reserve Dollars as payment for his online casino work. This transaction had purchase orders as supporting evidence, but the buyer wasn't named.

Based on this purchase history, Craig Wright filed a lawsuit, asking Bitcoin developers to cooperate and help him retrieve the funds through technical means. The logic was straightforward: "I have purchase orders proving I bought them, they were stolen, so it's reasonable to get them back."

Satoshi set the precedent; everyone is Satoshi. As long as you're powerful enough, you can do what Satoshi did—for example, challenge Bitcoin's "immutability" and "decentralization."

| Person | Time | Event | Outcome |
| :--- | :--- | :--- | :--- |
| Satoshi Nakamoto | 2010-08-15 | Bitcoin inflated by 184.4 billion coins due to bug; Satoshi settles it within 5 hours, erases record | Success |
| Vitalik Buterin | 2016-07-20 | 3.6 million Ether stolen; Vitalik decides, modifies underlying code, forcefully transfers | Success |
| Craig Wright | April 2021 | 111,000 Bitcoins stolen; sues Bitcoin developers in the UK, demanding technical code modifications to recover and return the coins | Lost |

When you were Satoshi, you made the call; wasn't it just a code change? Only when you give up the power do you realize that the hardest thing to change in this world is precisely that code.

Having lost a vast amount of Bitcoins, Craig Wright was left with nothing but tears. But he failed to realize that in 2021, when he tried to legally force developers to modify the code to return his 111,000 Bitcoins, he faced not just a group of programmers (his former underlings), but an unalterable consensus behemoth built by global computing power.

Satoshi did not learn from the lesson of losing 1.1 million Bitcoins; he still kept no backup.

---

# ❤️ Part Five: The Predicament of Self-Verification—Private Key Signatures and the Eternal Enigma

## 🏁 Chapter 9: Storms of Public Opinion and Technical Scrutiny

### 5.1.1 Preemptive Obstruction, a Dinner Ending in Lies

## 🔑 Dinner with Mike Hearn in July 2016

Mike Hearn contacted Satoshi in April 2009 because he had many questions about Bitcoin's future development. His correspondence with Satoshi lasted from April 12, 2009, to April 23, 2011. He has published "almost all" of his emails with Satoshi on his website. After Satoshi's departure, Mike Hearn became a member of the Bitcoin development team. In 2014, while fundraising publicly, he received an email from Craig Wright asking, "Can I fund you?" Mike Hearn had received a great deal of help from Satoshi.

The dinner between Mike Hearn and Craig Wright was arranged by Jon Matonis. The reason was simple: Craig Wright needed to prove he was Satoshi, and Mike Hearn's acknowledgment was important. If both he and Gavin Andresen certified it, it would be the most convincing. Craig Wright had just undergone a farcical self-verification. He now needed the help of the man he had previously helped, Mike Hearn.

From Mike Hearn, we can see many issues that help understand why Satoshi's return is so difficult and why so many people refuse to acknowledge him. After Satoshi disappeared, those surrounding the Bitcoin ecosystem, to consolidate their own positions, all engaged in various acts of consuming Satoshi's legacy. Those who seized power, those who pretended to be him and issued orders, those who fabricated legends—all were Satoshi's former disciples.

Mike Hearn could have easily proven the other person was Satoshi by asking a few private matters known only between the two, given over 2 years of communication. But Mike Hearn chose a purely technical question and set a trap for Craig.

The specific question Mike Hearn asked was: What is the `SIGHASH_SINGLE` mode in the signing protocol for?

`SIGHASH_SINGLE` is actually a vulnerability. In Bitcoin's early classic code, Satoshi left a logic hole in his implementation of `SIGHASH_SINGLE`. This vulnerability could allow the forgery or theft of funds from that input under certain conditions.

Think about it: the vulnerability existed precisely because he didn't understand it. And he was asked about it 8 years after the code was written. Mike Hearn's question was a precisely targeted "gotcha." He was looking for a technical error made by the other party, trying to trap him again. Answer correctly, and you're complicit. Answer incorrectly, and you don't understand. If you don't understand, you can't be Satoshi, because Satoshi is a god who understands everything.

Craig Wright wasn't stumped, but his answer used obscure technical jargon. Now Mike Hearn was confused; his understanding of Bitcoin stopped at the bug level, and Craig's explanation made him feel talked down to.

During cross-examination, Craig asked Hearn if he had signed a non-disclosure agreement before the dinner. Hearn replied, "I don't remember" and "No, I don't think so." This made Craig feel uneasy; they also had a competitive relationship, as Mike Hearn worked for R3, and his company had some overlapping patent applications.

After the dinner, Mike Hearn concluded Craig Wright was not Satoshi Nakamoto. In truth, even if he had a firm opinion, he couldn't have admitted it.

Around the time of his departure in 2011, Satoshi had emailed Mike Hearn, telling him, "I've moved on to other things. Gavin and the others will take good care of it." This line, widely known after the email was made public, cemented Mike Hearn's status in the Bitcoin community.

But the error was that after Satoshi's departure and deification, Mike Hearn described several test Bitcoin transactions he made in 2009 as transfers between himself and Satoshi Nakamoto. The media spun it into a great story. With Satoshi gone, there was no risk. But if he reappeared, the lie would be exposed, and his credibility would be shattered. Though common in Bitcoin—almost every holder of early blocks has spun some legendary tale involving Satoshi—it was risky.

This public narrative of directly transacting with Satoshi was important to Mike Hearn. It implied that one of the two addresses belonged to Satoshi, giving Hearn future interpretive authority over Satoshi. Since Hearn held the private keys to both addresses.

After the dinner, although Mike Hearn wouldn't acknowledge Craig Wright as Satoshi, he also refused to attack him. Like Gavin Andresen, he too was expelled from the Bitcoin camp.

### 5.1.2 Forced onto the Stage: The Ultimate Proof to Gavin Andresen

## 🔑 Proving Satoshi, Craig Wright's Signature Saga: "You'll Never Become Satoshi Nakamoto"

Between March and April 2016, Craig Wright conducted a series of private cryptographic signature verifications as the beginning of his self-certification as Satoshi:

* **Early March 2016**: Performed two private key signatures for Andrew O'Hagan, involving private keys for blocks 1-11.
* **Mid-March 2016**: Performed a private key signature for Jon Matonis, involving private keys for blocks 1 and 9.
* **April 7, 2016**: Performed three private key signatures for Gavin Andresen, involving private keys for blocks 1 and 2.
* **Late April 2016**: Performed a private key signature for BBC's Rory Cellan-Jones, involving the private key for block 9.
* **Late April 2016**: Performed a private key signature for The Economist's Ludwig Siegele, involving the private key for block 9.
* **April 29, 2016**: During a private key signature for GQ's Stuart McGurk, Nicolas Courtois disrupted the process, causing a conflict and termination.

---

In 2015, Craig Wright faced a massive fine from the Australian Taxation Office (ATO). To settle his debts, he sought help from his friend and former colleague, Stefan Matthews. The two had worked together at the Centrebet online casino in the early 2000s. When Craig contacted him, Matthews was running a venture capital firm for billionaire and gambling magnate Calvin Ayre.

Craig Wright wanted to sell his intellectual property. He revealed his identity: he was actually Satoshi Nakamoto—the inventor of Bitcoin. This was almost a knockout blow; Matthews was eager to serve.

Matthews then began searching for potential investors interested in blockchain intellectual property. Among these investors, Robert MacGregor, CEO of Canada-based nTrust, showed the most interest. Matthews told MacGregor that Craig Wright was almost certainly the mastermind behind Bitcoin, mentioning that Craig had sent him early drafts of the Bitcoin whitepaper before its public release in 2008, and had subsequently given him 50,000 Bitcoins.

Convinced, MacGregor and Matthews introduced Craig Wright to gambling magnate Calvin Ayre. The three met in Vancouver, laying the foundation for a deal to help Craig Wright out of his predicament.

After the successful Vancouver meeting, Calvin Ayre agreed to acquire Craig Wright's intellectual property for a total of $30 million (two installments of $15 million each) to help him pay off the ATO fines. Previously, the two exposé articles had cost Craig Wright everything in Australia; this funding pulled him back from the brink of financial collapse in London. Since then, Craig Wright has frequently expressed gratitude for Calvin Ayre's substantial financial backing (with subsequent investments exceeding $100 million), while Calvin has stated that Craig Wright is actually wealthier than he is.

Subsequently, nTrust's subsidiary nCrypt was formally established in London, with offices overlooking Oxford Street in central London. The office's burgundy leather chairs and sofas were air-freighted from Sydney.

Under the agreement, Craig Wright received an annual salary of $500,000 for five years, plus $1 million for "life story rights, for subsequent publication or distribution" (i.e., the story of Satoshi inventing Bitcoin). nCrypt recruited nearly 30 employees to help Craig organize his intellectual property and file patents. Their plan was to package all approximately 4,000 IP rights and sell them wholesale to major corporations like Google, UBS, or Uber; MacGregor admitted they had held preliminary discussions with these companies.

During the patent push, Craig Wright brought his former employee, Danish national Alan Pedersen, to London. Upon arrival, Pedersen was tasked with preparing the first 32 patent applications. However, due to Craig Wright's poor management skills and interpersonal style, friction grew between him and the employees—especially new ones unfamiliar with him. Pedersen privately complained to colleagues at nCrypt: "Stay away from Craig Wright; he's an absolute nightmare. Every morning when he comes in, I wonder what he's going to say today." Pedersen later recalled, "When new people joined, I had to teach them in advance how to talk to Craig, it's something I had to do. Sometimes, when Craig couldn't explain something clearly to others, it was a source of his anger."

Craig Wright embarked on his path of self-certification in London, also becoming the focal point of the entire internet's headlines in 2016.

---

## 🏁 Chapter 10: Beyond Trust: The Supreme Authority Built with Mathematics

### 5.2.1 100% Confidence, the Unforgeable Digital Stamp

To sell the patents at a high price, the first step was to convince the entire crypto community that Craig Wright was Satoshi Nakamoto. Satoshi's sole disciple, the highest-ranking spokesperson in the Bitcoin project, Gavin Andresen, was the most qualified person to certify Satoshi's identity.

Details of the private key signature, including media accounts and COPA case testimonies, have discrepancies in their descriptions. We cannot verify the exact details of the process, as different techniques and software could be used. A single computer, two computers with a USB drive, offline, online—all could successfully perform the signature verification. That's the magic of the algorithm.

The broad steps are two: generate a "Base64 string" using the private key plus the content, then verify using the string plus the content. The generated signature is a Base64 string, looking like: `2aR4lYa2zvQoZFbfnsEDsk2Y6oNDzDszBj/3QljTJehJKYvcPeZWJCnkJeU8gSHF75fc2wrGJztWGBYMdl3IIA==`. Verification yields only one of two results: correct or incorrect.

But rest assured: apart from Satoshi, Gavin Andresen is the most knowledgeable person about Bitcoin on Earth. No one could fool him.

On April 6, 2016, at 21:35, Gavin Andresen flew from the U.S. East Coast to London, checking into the Covent Garden Hotel (10 Monmouth Street, London, WC2H 9HB). After a 6.5-hour flight, Gavin slept until noon the next day. On April 7th, at 13:00, he had lunch with Stefan Matthews, Rob MacGregor, and columnist Andrew O'Hagan.

At 14:00 that afternoon, Craig Wright and Gavin Andresen formally met in the basement meeting room of the Covent Garden Hotel.

The two met and spent over three hours discussing stories from the early days, views on Bitcoin's development, and ongoing research. During this time, Gavin also asked private questions known only to the two of them from 2009. Craig Wright answered them all.

At 17:30, Craig Wright logged into his computer and signed a specified message using private keys that only the true Satoshi could possess. Gavin Andresen was momentarily stunned but not entirely convinced.

Acting on his technical instincts, Gavin Andresen stated: "I need to verify this on my own computer too." He had to ensure the software hadn't been tampered with. To be absolutely certain, Gavin insisted on using a computer that did not belong to Craig.

This shocked Craig Wright. The core conflict was: Gavin insisted on using his own machine; Craig adamantly refused to use a computer not belonging to him.

Craig Wright stated, "I swore I would never publicly display the key, nor would I ever let go of it. I trust Gavin Andresen, but I cannot use the private key on his computer." He explained that he dared not put the private key on any computer controlled by another person, even temporarily, fearing it could be copied.

Craig then told Gavin, "Maybe later we can get to know each other better, like more email communication; after building more trust, I can sign more messages for you." Gavin nodded in agreement. The atmosphere in the room turned cold. In Craig's mind, he was still wary of the private key being leaked.

Ultimately, MacGregor broke the deadlock by sending an assistant to purchase a brand-new ThinkPad laptop. Craig Wright and Gavin Andresen jointly confirmed that the laptop's outer and inner packaging seals were intact, with no signs of tampering.

After mutual agreement, they completed the Windows initialization setup on the new machine. Upon reaching the desktop, they briefly connected to the hotel's Wi-Fi to download the necessary verification software. Gavin additionally verified the checksums of the downloaded software against the official website.

The entire verification process required two core steps: first, using offline media, together with the original 2009 environment, to read the unencrypted early wallet file intact and securely invoke the corresponding private key; second, using a modern version of Bitcoin wallet software (or a standalone ECDSA cryptographic tool) to sign and verify the specified text offline. Since Bitcoin's signature verification is based on the secp256k1 Elliptic Curve Digital Signature Algorithm (ECDSA), a purely local mathematical operation that doesn't require UTXO state reconciliation, the entire process could be performed completely offline.

Yet, faced with the brand-new laptop and a room full of people expecting him to fulfill his promise, Craig Wright attempted to back out again.

Gavin Andresen later recalled: "It was clear that Craig still deeply wished to keep his identity secret. He found it emotionally very difficult to perform the cryptographic proof."

MacGregor and Matthews reminded Craig he had to abide by the agreement and urged him to sign. Craig stated he needed to call his wife, Ramona. On the phone, Ramona encouraged him to sign. Indeed, Craig Wright's concerns were not unfounded. The 2009 `wallet.dat` file had no password protection (wallet encryption hadn't been developed yet), it was completely in plaintext. This meant that if the file were copied in an untrusted environment, the private keys would be completely exposed. This would not only mean losing the proof of Satoshi's identity but also all the Bitcoins in that private key pool.

Encouraged by his wife, Craig Wright returned to the meeting room and finally agreed to sign. He opened the new laptop, inserted a USB drive, and copied the `wallet.dat` file containing the private key for Bitcoin Block 1 onto it. Gavin Andresen watched every step closely, monitoring Craig to ensure he only copied the one `wallet.dat` file.

`wallet.dat` is the file format Bitcoin used in 2009, based on the Berkeley DB (BDB) database, containing private keys, transaction history, key pair sequences, etc. The earliest Bitcoin wallets used the original BDB read/write engine, with private keys stored in plaintext. Over the years, the Bitcoin network has undergone significant upgrades and soft forks. Code from 2009 cannot recognize modern block structures. If these early software versions were connected to the network, they would be rejected due to format mismatches or consensus errors, often crashing. To read the key pool and generated receiving addresses intact, it was necessary to run natively in a clean, completely offline Windows environment.

On the completely offline, pristine new computer, Craig and Gavin began the cryptographic verification. The specified signature text was: "Gavin's favorite number is eleven. CSW."

Craig signed the specified text but omitted the final name initials "CSW." Gavin Andresen ran the local wallet software for offline verification; the mathematical result was correct. But Gavin insisted this was insufficient; the exact specified text must be signed.

Craig added "CSW" back and generated the signature data again. Gavin ran the latest wallet software offline, inputting the original text, the signature data, and the public key from Block 1 (obtained from public blockchain data). The algorithm returned a correct result.

Clearly, Craig Wright, in front of the most knowledgeable Bitcoin developer, had proven he possessed the private key for that specific early Satoshi block. Theoretically, this was the first time Craig Wright had proven, under rigorous conditions, that he held Satoshi's private key.

After verification was completely successful, Gavin Andresen shook hands with Craig Wright, stating he was convinced. Craig Wright tearfully thanked Gavin for his efforts on the project. Gavin Andresen then made the following statement to the media: **"I believe Craig Steven Wright is the inventor of Bitcoin."**

MacGregor later recalled: "Craig broke down. He said he thought he'd never have to do this, and that he'd never known how to trust anyone in his life."

It should be emphasized that this was a private signature verification between the two. It was based entirely on cryptographic principles. This also represents the most rigorous identity verification process in modern cryptography:

Step 1: Hashing the text (fully offline) Gavin provides the string "Gavin's favorite number is eleven. CSW." On the offline computer, through two rounds of SHA-256 calculation, a fixed 256-bit hash value is generated.

Step 2: Private Key Signing (fully offline) Craig inputs Satoshi's private key and the hash value from step 1 into the offline computer, runs the ECDSA signing algorithm, and generates/outputs the signature data consisting of two large integers (r, s).

Step 3: Public Key Verification (fully offline) Gavin takes the signature data (r, s) along with the original text, imports them into the wallet verification software on the offline computer. This step does not require connection to the Bitcoin network because the verification algorithm only needs the three elements "original text, signature data, early target address/public key" to run locally.

Step 4: Local software runs the algorithm and concludes The result is only one of two: verification successful (outputs 1) or verification failed (outputs 0). Success mathematically proves that the signer possesses that private key.

Elliptic Curve Digital Signature Algorithm (ECDSA) verification is pure mathematical computation. It is a self-contained mathematical action that requires no network synchronization. Everything happens privately; outsiders cannot glean any leaked information from the network.

The definitive outcome is: Gavin Andresen publicly stated to the media: **"I believe Craig Steven Wright is the inventor of Bitcoin."**

### 5.2.2 Selling the Soul: Mainstream Media Private Key Verification

Convincing Gavin Andresen was the first phase. The second phase involved Craig Wright meeting with journalists from the BBC, The Economist, and GQ for signature verification.

These signature verifications took place in the offices of a PR company on Tottenham Court Road in London. After viewing Craig Wright's technical demonstrations, each group of journalists received a USB drive containing the signature information to take away for independent verification.

Initially, Craig was strongly opposed to journalists taking USB drives. As he had repeatedly emphasized during the meeting with Gavin, he didn't want anyone taking copies of the information he signed for verification (even though the copies contained no private key information and were theoretically safe). Ultimately, Craig Wright compromised, agreeing to copy the public key for each signature onto USB drives, allowing the media to take them and verify them against the Bitcoin network.

🔐 First Media: BBC Verification
The first journalist to interview Craig Wright was BBC technology correspondent Rory Cellan-Jones, accompanied by colleagues Priya Patel and Mark Ward for the on-site verification.

The atmosphere was extremely tense; everyone present could see Craig Wright hated the meeting. He considered performing private key signatures for anyone, including journalists, as humiliating and was deeply reluctant. Despite his firm resistance, Craig Wright ultimately signed a series of messages using private keys from Bitcoin blocks 1 through 9, including the address used for Satoshi's first transfer to Hal Finney.

The BBC journalists verified the signature results for all 9 blocks, confirming they were all correct. The journalist then asked Craig Wright why he wanted to become the public face of Bitcoin and the broader cryptocurrency field. Craig Wright replied: "I don't want to be the public face of anything."

🔐 Second Media: The Economist Verification
The second verification was conducted by The Economist's Ludwig Siegele.

According to those present, Siegele was noticeably less friendly towards Craig Wright, asking more direct questions. He seemed skeptical of Craig Wright's choice to acknowledge his identity privately rather than publicly.

Similar to the BBC process, Craig Wright signed a message from Bitcoin Block 9 on-site and showed it to Siegele. However, the journalist responded confusedly: "Sorry, I'm still not sure what this demonstrates."

"It proves I have the private key," Craig Wright said. "These are Bitcoin's earliest original private keys."

Siegele didn't press further on this point but moved to another question: "Why now?"

Craig Wright replied: "I've been trying to avoid the media, but it's starting to affect other people. I'd rather stay quiet. As for why now? Because I have employees, I have a family."

🔐 Third Media: GQ Conflict and Reversal
The following day, the third verification was for GQ's Stuart McGurk. This time, he brought along someone claiming to be a cryptography and cryptocurrency expert, Nicolas Courtois.

GQ wanted Craig Wright to explain his evidence to McGurk while under Courtois's scrutiny. However, this demonstration went "extremely poorly." About eight minutes into the presentation, Courtois directly challenged: "This private signing proves nothing; you have to publicly sign on the Bitcoin network, in front of everyone."

This remark triggered an emotional outburst from Craig Wright, who yelled: "If you don't like it, then get the hell out!"

It should be noted that among these three media outlets, the first two were unlikely to be swayed by bribes. Thus, GQ became the point of entry. After a night of planning, Nicolas Courtois was planted with the core mission of finding fault and provoking Craig Wright.

Craig Wright fell for it, completely unprepared to face someone whose sole purpose was to antagonize him. "Stop talking nonsense, get out!" Craig Wright roared again.

Courtois added: "I'm not saying your evidence is invalid, but you can't prove it privately; you have to sign publicly in front of the whole network..."

Moments later, Craig Wright shouted again. In the audio recordings from that day, much of his speech is hard to distinguish, but some snippets are very harsh, including: "There are thousands of transactions on Bitcoin every day, all signed with that damn digital generator!" and "If I hear one more piece of nonsense about how I did this with unknown nodes, you either give me evidence or get out!"

Craig Wright was thoroughly enraged by Nicolas Courtois, repeatedly telling him to "get out." The atmosphere throughout the demonstration was extremely hostile, even verging on physical altercation at one point.

Two days later, Courtois emailed Stuart McGurk, writing: "Craig deceived us; it's a hoax, I have proof." He claimed to have evidence that the software had been tampered with and the hotel's Wi-Fi had been hacked.

Clearly, journalist Stuart McGurk brought Courtois in to disrupt the event. But as a media outlet, GQ wasn't ultimately controlled by Stuart McGurk; there was an editor-in-chief above him. Ultimately, the editor-in-chief halted the publication of GQ's article on Bitcoin.

At this point, truth and falsehood no longer mattered. Nicolas Courtois had conveniently provided a narrative, and this so-called "expert" and "doctor" reached the final conclusion: the software was altered, and the network was hacked.

---
# ❤️ Part Six: The Genius's Predicament—Humble Submission Under the Microscope

## 🏁 Chapter 11: Low Profile and Endurance, You Signed the Only Solution, Yet Couldn't Solve for Human Greed

### 6.1.1 Against the Whole World, It Was Destined from the Start That You Wouldn't Become Satoshi

On the morning of May 2, 2016, news spread globally: "Private key signatures are all correct; Craig Wright has finally proven he is Satoshi Nakamoto."

That day, articles from the BBC and The Economist went live at 8:00 AM. Gavin Andresen's blog post also emphasized the evidence Craig Wright had shown him. Craig Wright also published his own blog post, offering more cryptographic evidence supporting his claim as Satoshi Nakamoto.

The BBC's article titled "Bitcoin founder reveals identity" took a positive stance on Craig Wright's claim. It stated, "Craig Wright has provided technical evidence to support his claim, signing with private keys known to belong to the creator of Bitcoin," and "the most prominent members of the Bitcoin community say they have verified his claim."

The Economist's report on Craig Wright's claim differed from the BBC's, expressing skepticism but not denial, as the USB drive they brought back could be verified. Siegele believed Craig Wright hadn't fully proven his claim. He wrote: "For Mr. Wright to convince the world that he is indeed who he claims to be, he must also perform a public signature."

The GQ article was suppressed, published only months later. GQ's refusal to verify the signature on-site, releasing rumors of hacked software and networks, had already fulfilled its mission. Surprisingly, the eventual GQ article took a positive stance: Gavin Andresen firmly stood by Wright. He explained his reasons for believing Wright was Satoshi Nakamoto in his own blog, based on the evidence he saw firsthand. "I believe Craig Steven Wright is the inventor of Bitcoin."

Gavin Andresen made a very definitive statement: "After spending time with him, I am without a doubt convinced: Craig Wright is Satoshi Nakamoto. Part of that time was spent meticulously verifying cryptographic signatures on messages signed with keys that only Satoshi Nakamoto should possess. But actually, I was fairly sure I was sitting next to Bitcoin's father even before I saw the key signed and verified on an un-tamperable, clean computer."

In the 2016 internet age, mainstream outlets like the BBC, The Economist, and GQ could no longer deliver a final verdict.

Bitcoin's vested interests began a ruthless counterattack. They fabricated lies, controlled narratives, and didn't hesitate to use the most stringent, illogical standards against the truth while remaining silent on their own ulterior motives. When the deterministic logic of mathematics (SHA-256) began to settle the debts of history, these mediocre consensus usurpers, with nowhere left to run, retreated into dark corners, using shameless media perjury to weave their final grand lies. This was not a growing pain of technological evolution; it was a bloody struggle among a pack of wolves, a clash of old and new orders.

May 3-4, 2016. Coordinated social media narrative: "The signature is fake; it was signed before by Satoshi and copied/pasted, the signature is insufficient; you must transfer a coin to prove it." "Craig modified the software and hacked the network to complete the signature."

On May 4, 2016, everything stopped. Craig attempted to harm himself; he was bleeding in the bathroom. His lawyer, Stefán, was with him, and his wife Ramona was on her way. An ambulance was called. Later, one of his colleagues confirmed to Gavin that Craig Wright, under immense pressure, had stabbed himself in the neck.

On May 5, 2016, Craig's blog updated with a farewell letter titled "I'm Sorry," claiming he lacked the "courage" to continue proving himself. That day, Craig was unshaven, pale, and hollow-eyed. His hands trembled. He told his wife Ramona: "Now I'm trapped. If you prove it, you go to jail. If you don't, you're a fraud." Craig clearly felt he had reached the end. He would provide no more evidence and have no further contact with the media.

Craig Wright finally realized his epiphany. He had complied with everyone's demands; mainstream media had accepted him. But the frenzied social media had launched shameless slander and framing, seemingly intent on destroying him for the sake of destruction. No one wanted Satoshi Nakamoto. He would never become Satoshi.

Ramona comforted Craig Wright: "If we tell everything, you'll definitely go to prison."

Looking back now, we can't help but ask, why did Craig no longer have the courage to prove himself?

Craig Wright sold online gambling software to Costa Rica and Panama—illegal. He exploited Australian government tax refunds and R&D grants—illegal. He applied for tens of millions in refunds through a dozen companies—illegal. Before 2015, Craig Wright was Bitcoin's largest market maker, manipulating and controlling its price trajectory—illegal. Craig Wright couldn't afford to pay half of the 1.1 million Bitcoins in the U.S. David Kleiman lawsuit and denied being Satoshi—perjury. Satoshi's journey was never that of a saint; he was a mortal, gambling his all on his destiny. Not proving himself as Satoshi left some plausible deniability. Proving it would expose him to claims worth tens of billions, combined with political risks. With Bitcoin's accumulated dirty history, Satoshi would be held legally responsible. The best way to protect himself was to remain silent, no matter what others said.

### 6.1.2 Won the Math, Lost the World, Because You Can Never Prove You Are Satoshi

It's worth exploring why, when the private key signatures were confirmed correct, opponents like Adam Back, Vitalik Buterin, Jack Dorsey, Changpeng Zhao, and Gregory Maxwell could still argue speciously and lie through their teeth.

Because if you choose to be contentious, Craig Wright truly could never become Satoshi Nakamoto.

🌌 1: Your signature is correct, but that's only Gavin's (or a few people's) claim. Private signatures don't count; you must sign publicly for the whole network to see.

🌌 2: You sign publicly, and it's correct. But that only proves you possess Satoshi's private key. How did you get it? Maybe Satoshi gave it to you? Or you stole it from him. It doesn't prove you are Satoshi.

🌌 3: You batch-sign thousands of the earliest blocks. That proves nothing. The Genesis Block 0 is the only true proof of Satoshi. It must be Block 0; nothing else counts. (Block 0's address is hardcoded in the source code; technically, that address wouldn't have a corresponding private key.)

🌌 4: You sign Block 0. So you hacked Satoshi's email back then, didn't you? Is his disappearance related to you?

See? A signature proves nothing. It's just a trap designed to land you in legal quicksand.

The signature is a carefully crafted "proof-of-falsity cycle." Cryptography can't prove identity, only ownership. In the computer world, a private key is an "objectively existing file," while identity is a "subjective social definition." Opponents can always use the logic "possessing his private key doesn't make you him" to invalidate any cryptographic proof. A signature is bait, luring you into a quagmire of "proving your innocence." If you can't prove your private key wasn't "stolen" or "taken," then by signing, you inevitably ensnare yourself in endless lawsuits and moral accusations.

Does submitting evidence help? Craig Wright submitted a Samsung USB drive from his time at BDO. It contained 97 files dating from 2004 to late 2008.

Yes, if you're being contentious, there's always a technical argument. No tech giant in history can definitively prove in court that "they created themselves." Like the UK COPA case: you submit hundreds of files and evidence. Then COPA scrutinizes with a microscope: wrong editor used, wrong font, wrong editing timestamps, wrong metadata, wrong physical traces, wrong OS environment, wrong compiler identifiers, wrong kerning and typesetting, wrong character encoding, wrong printer dot matrix, wrong paper manufacturing date.

Under such adversarial scrutiny, anyone is guilty in the face of technological history's dust. We could use the same underlying logic to challenge these tech giants. Challenge Microsoft: Modern Windows contains hundreds of millions of lines of source code and intricate dependency libraries. How can Microsoft prove to a court that every Bezier curve in its font libraries, every byte of its DLLs, every typesetting algorithm in its task scheduler is entirely original and has never undergone a single metadata change due to system crashes, cross-platform migrations, or timestamp errors over decades? Challenge Jack Dorsey: How can you prove you founded Twitter? Which specific patch version of Ruby was running on your backend? How many fields were in your MySQL database, what indexes, what compiler version? If you get one detail wrong, you're not the inventor of Twitter.

In modern computer science, a simple console file contains hundreds of metadata attributes. If one adopts a pre-ordained "fault-finding" approach, then Microsoft, Google, Apple, Amazon, Tesla—none could prove their own innocence. The digital world is inherently mutable and multidimensional. Any routine system upgrade, backup restoration, or cross-platform transfer leaves technical traces that can be interpreted as "forgery." If you don't believe it, anyone can act as a tech-savvy scoundrel and use this "technological magnifying glass" to deconstruct the entire history of human technology.

But didn't the orchestrators of this charade know this? They knew perfectly well. Proving truth or falsehood was never their core goal. Their real intent was to use "technical information asymmetry" to wage a cognitive war: bombarding the public with obscure technical details (metadata, encoding formats) to create the impression that "he is a fraud." Using slander, framing, and information flooding, they created doubt in the minds of the uninformed. In this carefully designed technological Rashomon, the goal of defamation was achieved, and truth was suffocated under the microscope.

Slander and framing were real. After Craig Wright's signature was verified correct, Blockstream CTO Gregory Maxwell (a former Satoshi underling) directly fabricated a claim: the digital signature was copied from an old Bitcoin transaction. This is like pasting a copy of a celebrity's signature into a book—it doesn't prove authorship.

The media parroted these voices. The signature was just a copy-paste job. That settled it; we were deceived. But the truth? Remember, this was a private verification, off-chain. You hadn't even seen a single letter of it. How could you know it was a copy-paste? At critical moments, lying to incite public outrage was permissible. Not only lying, but also paying off the media to amplify the noise, leaving you speechless with your bitterness. That's what Adam Back, Vitalik Buterin, Jack Dorsey, Changpeng Zhao, and Gregory Maxwell did to Craig Wright. These mediocre individuals staked their reputations on public lies in 2016. Private signature? Then don't blame us for muddying the waters and leaving you unable to defend yourself. Public signature? We had other responses ready. In short, you will never become Satoshi Nakamoto.

⚖️ The COPA case. The UK High Court, at the very beginning of its ruling, painted a picture of an ideal Satoshi.

⚖️ COPA case UK High Court's characterization of Satoshi: The materials Satoshi wrote at the time, including the whitepaper, forum posts, and emails, gave an impression of calm, erudition, collaboration, and rigor. He showed little arrogance and was willing to acknowledge and implement ideas and suggestions from others interested in Bitcoin. Given Satoshi's collaborative spirit and non-confrontational nature, I consider it highly unlikely that he would resort to legal action against developers. Satoshi would have understood that a hard fork of the Bitcoin blockchain arose from differences of opinion and would have likely let the matter rest. Ultimately, I believe the true Satoshi would likely never try to prove he is Satoshi through litigation.

The judge who said this is quite interesting. His name is James Mellor.

Since signatures were useless, Satoshi decided to stop signing. He offered an explanation to the public: after May 4, 2016, he destroyed the hard drive containing the private keys used in the signing process. He threw it from his home in Wimbledon, shattering the platters. He also smashed the drive with a hammer and crushed the USB drive with his foot. Due to Autism Spectrum Disorder (ASD), feelings of betrayal triggered an emotional reaction, leading to his impulsive actions.

We all know the private keys are still there. But we are also beginning to believe that for Satoshi, using a private key signature is equivalent to "selling his soul." Or perhaps his inherent pride couldn't tolerate such a humiliating act; he genuinely despised those who questioned him.

The only true proof of identity is not a private key, not a signature, not source code, not a whitepaper, not others' recognition. Only wealth can prove everything. This is the deepest, most tragic song in Bitcoin's history.

You once believed that every protocol written in the whitepaper was immutable. But you ultimately underestimated the absurdity of this world. When a pack of wolves hunts, when everyone is a villain, Satoshi is just a piece of paper casually torn up. No one wants to worship the purity of mathematics.

They don't believe in gods; they only believe in the mountain of gold beneath the god's throne.

To prove himself, Satoshi could only rely on the Bitcoins in his hands, using supreme wealth to reclaim his name.

---

## 🏁 Chapter 12: Interests and Interpretive Rights: The Strangulation of a Genius and the Reenactment of History

### 6.2.1 Suppressing a Genius Is Not Just Personal Behavior, But a Group Dynamic

### The Core Camp That Fears Craig Wright: Everyone is Satoshi, Except You.

When mediocrity confronts genius, it creates cognitive dissonance. Suppressing a genius is not just personal behavior; it's a group dynamic.

The essence of suppressing genius is the struggle for discourse power—mediocrity controls the discourse system to marginalize the genius's voice, rendering it unheard, misunderstood, and unrecognized.

<details open>
<summary><b>📐 Table (Default Open, Click to Collapse)</b></summary>

| Name | Identity | Conflict of Interest |
| :--- | :--- | :--- |
| Mark Zuckerberg | Facebook Founder | Withdrew after feeling used |
| Changpeng Zhao | Binance Founder | Initiated coordinated delisting sanctions |
| Vitalik Buterin | Ethereum Founder | Demanded Genesis Block 0 signature |
| Michael Saylor | MicroStrategy Founder | You must never sell BTC |
| Brian Armstrong | Coinbase Founder | Beneficiary of stolen credit |
| Jesse Powell | Kraken Founder | Responded to coordinated delisting sanctions |
| Jack Dorsey | Twitter Founder | Formed and manipulated counter-alliance |
| Emin Gün Sirer | Avalanche Founder | Coerced/induced to fabricate narratives |
| Charlie Lee | Litecoin Founder | Altcoin leader most fears the original |
| Roger Ver | Bitcoin Jesus | Failed attempt to carve up gains |
| Adam Back | Whitepaper Reference | Biggest beneficiary of Bitcoin |
| Peter Todd | Adam Back's crony | De facto Bitcoin power |
| Cory Fields | Adam Back's crony | De facto Bitcoin power |
| Michael Ford | Adam Back's crony | De facto Bitcoin power |
| Eric Lombrozo | Adam Back's crony | De facto Bitcoin power |
| Matt Corallo | Adam Back's crony | De facto Bitcoin power |
| Marco Falke | Adam Back's crony | De facto Bitcoin power |
| John Newbery | Adam Back's crony | De facto Bitcoin power |
| Samuel Dobson | Adam Back's crony | De facto Bitcoin power |
| John Hudson | Computer Forensics Expert | Evidence file font is wrong |
| Patrick Madden | Computer Forensics Expert | Evidence file editor version is wrong |
| Rory Cellan-Jones | BBC Tech Journalist | Bribes |
| Arthur van Pelt | Columnist | Bribes |
| Steve Lee | Jack Dorsey's crony | Counter-alliance member |
| Zooko Wilcox | Cypherpunk | Adam Back's tool |
| Mike Hearn | Cypherpunk | Adam Back's tool |
| Dustin D. Trammell | Cypherpunk | Adam Back's tool |
| Gregory Maxwell | Satoshi's crony (2011) | Initiated backstabbing Satoshi |
| Wladimir van der Laan | Satoshi's crony (2011) | Initiated backstabbing Satoshi |
| Martti Malmi | Satoshi's crony (2011) | Participated in backstabbing Satoshi |
| Matt Corallo | Satoshi's crony (2011) | Participated in backstabbing Satoshi |
| Luke Dashjr | Satoshi's crony (2011) | Participated in backstabbing Satoshi |
| Pieter Wuille | Satoshi's crony (2011) | Participated in backstabbing Satoshi |

</details>

Without Satoshi at the helm, these individuals steered Bitcoin in a different direction, leading directly to its hijacking. The "protocol immutability" that Satoshi designed into the original code and architecture, through real-world evolution and various internal conflicts, saw original Bitcoin modified numerous times, even the wallet address format was changed. Bitcoin addresses start with 1; addresses not starting with 1 are not Bitcoin.

Addresses starting with 1 were determined by Satoshi, hardcoded into the Bitcoin source code. If you create a fake Bitcoin, you need to change the address format—simple logic. If even the address format is changed, can you still call it Bitcoin?

Bitcoin's hijacking stems from the fact that Bitcoin's "voting mechanism" (more accurately, its consensus mechanism) is not a simple, single-dimensional vote but a power structure mutually checked and balanced by "hashing power (miners)" and "full-node users." During the 2015-2017 "block size debate," miners representing over 80% of the network's hashing power wanted to increase the block size. In practice, miners had little say; their role was merely to pay electricity bills and package transactions. In major decisions, the will of the nodes overrides hashing power.

In 2026, you could quickly and cheaply spin up 100,000 full nodes to support your desired upgrade. With just one IP address and 1TB of hard drive space, you could run a full node. That's equivalent to whoever sends the most spam having the most say—clearly not feasible. Thus, power was centralized in the hands of developers who control upgrades, granting them discretionary authority. Notice: miners have coins but no power; developers have power but no coins. Capital intervenes by funding developers to gain control of Bitcoin. This is what the individuals in that table did.

Among this camp, Mark Zuckerberg is unique. In September 2020, Twitter's CEO and founder Jack Dorsey established COPA (Crypto Open Patent Alliance). Mark Zuckerberg became a powerful endorser within COPA, representing Silicon Valley. Zuckerberg had long sought to acquire Twitter; in 2008, Facebook made a roughly $500 million offer. On October 27, 2022, Musk officially completed the acquisition of Twitter. On January 31, 2024, Mark Zuckerberg issued an official statement announcing his withdrawal from COPA.

Why did Satoshi suffer slander and betrayal from these individuals? They come from four groups: "Altcoins and exchanges," "Cypherpunks," "Satoshi's disciples from 2009-2011," and "Paid forensic experts and media."

Representatives of altcoins and exchanges, like Vitalik Buterin, displayed near-fanatical reverence for the Bitcoin protocol in his early years, almost as a pilgrim, deeply studying and trying to continue Satoshi's decentralized vision. Changpeng Zhao still faces unresolved legal issues in his home country, named on relevant judicial wanted lists. Coinbase is even more ironic: the word itself was coined by Satoshi for the mining reward.

The Cypherpunks—this was a mailing list that Adam Back joined via email. Mailing lists were widely used in the 90s, during the dial-up modem era. By 2000, they had largely been replaced by forums, chat rooms, instant messaging, and blogs. Note that this was a mailing list in 2008—only a tiny fraction of people who started using the internet in the 90s used them, mostly in open-source software circles. While the Cypherpunks mailing list fostered a near-idealistic academic and technical atmosphere, it was also a hub for open-source ideology. Craig's initial purpose in joining was to find clients and freelance reverse-engineering work. Key characteristics of those active on the Cypherpunks list in 2008 were: 1) reverence for open source and disregard for intellectual property, 2) strong technical skills.

Satoshi's disciples from 2009-2011—early Bitcoin adopters were largely interested in the currency as a tool to evade legal oversight. If you understood code, you'd immediately notice the Texas Hold'em poker function in the source code and quickly realize Bitcoin was essentially a chip. The first groups to give it "real intrinsic value" and liquidity came from the dark web, underground industries, drugs, money laundering, gambling, fake documents, and various illicit services. Is it surprising that such a group would collectively betray Satoshi? But you cannot deny that Satoshi was never a pure deity perched on a cloud; he was deeply embedded in this chaotic and rebellious reality. He was part of this group: selling online gambling software, starting a relationship with an employee before his divorce, manipulating Bitcoin prices, using a dozen companies for money laundering and tax evasion. This left an indelible mortal stain on his character. Yet, despite his mud-soaked past, his brilliance that burned through the night cannot be diminished. He wasn't a perfect saint but a madman who dared to gamble against the world. He had countless messes and stains but also single-handedly initiated a new era. Whether you like him or hate him, what he created with his genius-level intellect has irrevocably changed human technology and wealth rules. This epic, historic counterattack is undeniable. That is enough. That is a legend.

### 6.2.2 The Genius's Predicament Throughout History

Mediocrity suppresses genius because the rise of genius signifies the collapse of the old order—and the mediocre are often the beneficiaries of that old order. It's a rational form of selfishness: fear of being surpassed by innate talent; fear of having one's interpretive authority replaced; fear of one's existence becoming insignificant.

Isaac Newton invented calculus (which he called "the method of fluxions") in the 1660s but didn't publish it. Leibniz was the first to publish a paper on it in 1684, sparking a protracted priority dispute over calculus's invention. In 1712, the Royal Society concluded Newton had priority. Newton's true grievance was that, despite being the earliest inventor, his caution and fear of criticism prevented him from publishing promptly, robbing him of the glory of being the undisputed first inventor and embroiling him in endless conflict.

Newton was not only a scientist but also a rigorous textual scholar. He scrutinized the Bible like a scientific study, secretly investigating Jesus's identity, and dared not publicly reveal his beliefs due to the severe penalties of the Blasphemy Act. He endured immense psychological pressure and compiled a "List of Twelve Sects," cataloging theological schools that had distorted Jesus's nature.

Countless other examples exist: Galileo Galilei, Nikola Tesla, Alan Turing, Vincent van Gogh, Nicolaus Copernicus, Giordano Bruno.

People always mock genius first, then worship him—when they finally understand him, he is already dead.

In 2026, we still allow this to happen: **Craig Steven Wright.**

---

# ❤️ Part Seven: Shadow Rule—Satoshi's Private Keys Were Never Lost; He Still Controls Everything

## 🏁 Chapter 13: Not 1.1 Million Bitcoins, But 2 Million; The Private Keys Were Always There

### 7.1.1 Everything is Fake, Only the Timestamps are Real

Around 2014, because of the large volume of funds, Craig Wright revealed to Australian tax officials that he had injected over $200 million into his research and mining companies through complex structures. This money came from selling a portion of his early Bitcoins, intended to build the world's most extensive computer network to maintain mining share.

In December 2015, the first major leak of internal documents identifying Craig Wright as Satoshi occurred. The most critical document was the "Tulip Trust." It recorded Craig Wright transferring his Bitcoin assets to Dave Kleiman for custody. The document explicitly stated the trust assets included 1,100,111 Bitcoins, with the stipulation that these assets could not be altered before 2020.

Dave Kleiman's brother, Ira Kleiman, sued Craig Wright in Florida federal court in 2018, demanding a share of the 1,100,111 BTC estate (Kleiman v. Wright).

During the lengthy trial, the court ordered Craig Wright to disclose the specific on-chain address list for these 1.1 million Bitcoins. This was a U.S. court, unlike the ATO; deceiving the court carried severe consequences. Consequently, Craig Wright did what he would later regret most: he submitted a list of his unsold (note: not mined) address holdings.

In 2017, Craig's lawyers submitted to the court a document listing the unsold Bitcoin addresses he held. This list comprised 27,971 addresses, each containing 50 Bitcoins from blocks 1-75,400 (mined between January 3, 2009, and August 21, 2010), totaling 1,398,550 Bitcoins. This represents 37% of the block addresses from that period. Satoshi clearly mined more; this list wasn't his total mining output but his holdings—what he hadn't sold yet.

The list of 27,971 addresses belonging to Craig Wright was initially submitted as "sealed court evidence." However, the court inadvertently made the documents public on August 15, 2019, exposing the address list. After its publication, on-chain analysts began tracking it closely, developing various tools to monitor these addresses' movements.

This put Craig Wright on the defensive, as he still needed to sell Bitcoins to fund mining and development. Since then, he has indeed sold some each year. Over 10 years, he sold another 10,300. In 2024, he cashed out approximately $250 million; in 2005 (likely 2025? typo), about $50 million; and in the first half of 2026, approximately $50 million.

Dramatically: after this address list was published and came under intense scrutiny, 145 addresses from the list suddenly performed private key signatures, publicly messaging that Craig Steven Wright is a liar.

The joint signature from the 145 addresses: "Craig Steven Wright is a liar and a fraud. He doesn't have the keys used to sign this message. The Lightning Network is a significant achievement. However, we need to continue work on improving on-chain capacity. Unfortunately, the solution is not to just change a constant in the code or to allow powerful participants to force out others. We are all Satoshi." The gist is that Craig Wright is a liar, he doesn't have the private keys for those public addresses, and although the Lightning Network is good, we still need to work on on-chain scaling.

You read that correctly. Satoshi Nakamoto, Craig Steven Wright, is calling himself a liar!

The 145 addresses, each holding 50 Bitcoins, total 7,250 Bitcoins. Because they performed a public signature, it confirms they possess the private keys. In 2025, this was worth over $800 million. Not a single one has been sold to date.

Timestamps tell the story. These 145 addresses come from the same computer's `wallet.dat` file. Before 2012, the entire Bitcoin ecosystem was in a primitive genesis era. There were no seed phrases, private keys were stored in plaintext, and mining difficulty was 1. A personal computer could mine 3-5 blocks per day, recorded sequentially in the `wallet.dat`.

To confuse the issue, Craig Wright began using misdirection. From among his many `wallet.dat` files, he selected one to sign a message.

What information can we glean from these 145 addresses? Let's first distinguish between UTC and Sydney time (UTC+10).

1: From December 14, 2009, to January 10, 2010, a span of 27 days, 632 hours. He mined 136 blocks (6,800 Bitcoins), averaging 1 block every 4.65 hours.
2: Gaps exceeding 10 hours between blocks indicate periods when the computer was turned off. There were 15 such shutdowns. (This was a personal computer, frequently turned off).
3: Gaps of less than 30 minutes between blocks occurred 17 times. (This was a desktop; its hashing power significantly reduced block times).
4: There were 4 instances of 1-minute gaps, and 3 instances of 2-3 minute gaps. (e.g., blocks 32529-32530 had a 41-second interval).
5: Two distinct periods: May 11-19 and December 14-January 10 (suggesting a switch to a different computer).
6: December 23-26, 2009: Most frequent shutdowns, likely due to the Christmas holiday season, working less.
7: New Year's Eve, December 31, 2009, he worked until 16:00. After New Year's, on January 1, 2010, he was back at work by 9:30.
8: Working hours on January 1, 2010: 9:30 - 23:18.
9: Working hours on January 2, 2010: 5:34 - 23:45.
10: Working hours on January 3, 2010: 8:09 - 19:10.
11: Working hours on January 4, 2010: 5:39 - 22:36.
12: After shutting down around 10:00 AM on January 10th, he attended to other matters, and this computer was turned off for a long period until the private keys were exported.

A reasonable inference is that he briefly used an office computer in May 2009, downloading `bitcoin.exe` and mining 9 blocks. He switched to a laptop after May. On December 14, 2009, he resumed using the office computer. The records detail the mining history from this office computer's `wallet.dat`, which mined 145 blocks. A less charitable inference is that he discovered an office affair in December, leading him to spend nearly a month in the office. Shortly after, the Tulip Trust was established.

<details open>
<summary><b>📐 Table (Default Open, Click to Collapse)</b></summary>

| Original Time (UTC) | Converted Time (Sydney) | Elapsed Time | Minutes | Wallet Address / ID (that signed the message) |
| :--- | :--- | :--- | :--- | :--- |
| 2009-05-11 21:37:45 | 2009-05-12 07:37 | - | - | 1JaKriNjceGmggKYQkURmatQv6LXyvUiAB |
| 2009-05-11 22:00:34 | 2009-05-12 08:00 | 23 minutes | 23 | 1CpkvbaAhn81Vc4vbx1yr9jGuETvetutBj |
| 2009-05-12 20:22:44 | 2009-05-13 06:22 | 22h 22m | 1342 | 1MwWRaka2dQySercEFgZDenBvWpHw3kvCz |
| 2009-05-14 09:17:26 | 2009-05-14 19:17 | 1d 12h 55m | 2215 | 16BBCJoyBBuyk2bKM64EGCADgiacdpBsKP |
| 2009-05-14 15:36:04 | 2009-05-15 01:36 | 6h 19m | 379 | 13jEwgtkahPdHQkPTtbHwFm6mvC4Vq71Tj |
| 2009-05-16 08:06:11 | 2009-05-16 18:06 | 1d 16h 30m | 2430 | 19aXsBvYyGeiFnAbCaGWtmeQwiFFxzH3mZ |
| 2009-05-18 20:24:35 | 2009-05-19 06:24 | 2d 12h 18m | 3618 | 13forcak6Mv1ZYBo9wv3zeWB8UhDwBJr5S |
| 2009-05-19 04:31:06 | 2009-05-19 14:31 | 8h 7m | 487 | 1F39FW9NU8tuSCVhxVstd7piVSNw4YVGxY |
| 2009-05-19 06:52:59 | 2009-05-19 16:52 | 2h 21m | 141 | 12isdcKgXGQt1F42tCYHPevErL7rsax4Uc |
| 2009-12-14 15:46:00 | 2009-12-15 01:46 | 209d 8h 54m | 301494 | 1C4Ym7bZZffCCjtRwcwvR6phVzCwQDyEK7 |
| 2009-12-14 19:15:55 | 2009-12-15 05:15 | 3h 29m | 209 | 1KF7rv8hTcC88MHeYzKwBuACoecWaQJ91m |
| 2009-12-15 04:55:39 | 2009-12-15 14:55 | 9h 40m | 580 | 1MhpaS75Xxxyqvcv3CLBwz2L76gDDpysJm |
| 2009-12-16 05:29:32 | 2009-12-16 15:29 | 1d 34m | 1474 | 1Bn5U322mFuMKyoC9jKayfzbrpe3T3QscR |
| 2009-12-16 19:07:35 | 2009-12-17 05:07 | 13h 38m | 818 | 1D1Ci72Bhde38avQjP2Gyy6ZGhP2mgvoik |
| 2009-12-17 04:04:34 | 2009-12-17 14:04 | 8h 57m | 537 | 1LXUhX4tXfWGekjucDASYWSsPzYLhYM282 |
| 2009-12-17 08:40:43 | 2009-12-17 18:40 | 4h 36m | 276 | 1JqT7snx8i7zmx748FYJbXfXEeXdMgWr6d |
| 2009-12-17 12:54:10 | 2009-12-17 22:54 | 4h 14m | 254 | 15JM7KfaXPwhYRpDkAeE6YxVhC5bRusWk5 |
| 2009-12-17 13:01:22 | 2009-12-17 23:01 | 7m | 7 | 1FDs6tF2wxAPhPKgkT4eCd51WWqYuFdXXR |
| 2009-12-17 14:17:16 | 2009-12-18 00:17 | 1h 16m | 76 | 1Mfjtt7aJEkwcoocokQxLNE1jDEqh6LFKF |
| 2009-12-17 16:03:05 | 2009-12-18 02:03 | 1h 46m | 106 | 1KkajS3KDciJbfKk2Vg2SjUE6eKdiMktAa |
| 2009-12-17 17:58:07 | 2009-12-18 03:58 | 1h 55m | 115 | 1Bh4Vari8LcDcdH2qWJVK5sN4dA4vWfQe3 |
| 2009-12-17 20:05:33 | 2009-12-18 06:05 | 2h 7m | 127 | 16TqRUQtrBRv9jnpuyVFEH43SRKZhqrCQ7 |
| 2009-12-17 21:38:33 | 2009-12-18 07:38 | 1h 33m | 93 | 12Ft7JjoqV6fTzUA3mRnosDYtJekVqnZpT |
| 2009-12-17 23:58:14 | 2009-12-18 09:58 | 2h 20m | 140 | 12CTHhyJtr49LgoUShbWgebLBviLAFj6nj |
| 2009-12-18 11:16:54 | 2009-12-18 21:16 | 11h 18m | 678 | 1LpCzHxxWasKBUCqbyXRUsKn1RSvNaRupT |
| 2009-12-18 11:47:11 | 2009-12-18 21:47 | 31m | 31 | 12MZnJfu7GNrC8bSPuZhgNDr9otmUZnALu |
| 2009-12-18 13:20:47 | 2009-12-18 23:20 | 1h 33m | 93 | 1BPqcdb4kzgoPyjpyrL9xzhmMsJS5eQqvw |
| 2009-12-18 13:40:33 | 2009-12-18 23:40 | 20m | 20 | 1Q3HYAZwnooayQZWEkYSThT353KcbpFF3P |
| 2009-12-18 14:42:48 | 2009-12-19 00:42 | 1h 2m | 62 | 1GgLxr81StVBpRQPNQKnSF25kyEcpHCnz5 |
| 2009-12-18 17:42:57 | 2009-12-19 03:42 | 3h | 180 | 1B8tBmGzxLynfxop38RpNaJ8SM5wr3oj4W |
| 2009-12-18 20:52:53 | 2009-12-19 06:52 | 3h 10m | 190 | 15StD6n2ZTygoc7PM2bY13aAkwybNBUwn8 |
| 2009-12-18 22:10:04 | 2009-12-19 08:10 | 1h 18m | 78 | 18DfVFHfCAVFBhbmBLYxsE3HZqpaSu1Wvw |
| 2009-12-18 22:52:19 | 2009-12-19 08:52 | 42m | 42 | 1BQqVjRAGndm8tRrwQNwdgJR8yhhDxXzE7 |
| 2009-12-18 23:58:04 | 2009-12-19 09:58 | 1h 6m | 66 | 1HenciVLZmE9ugshcrW3GtZttP1bqr8W3s |
| 2009-12-19 05:05:25 | 2009-12-19 15:05 | 5h 7m | 307 | 19bf2fMfCt1b3MLbHwahJfdUNoZXTxYd5D |
| 2009-12-19 14:49:18 | 2009-12-20 00:49 | 9h 44m | 584 | 1GwaiUArAF6MfSPV8SwCnp5LKEEbu9qrQ9 |
| 2009-12-19 21:07:50 | 2009-12-20 07:07 | 6h 18m | 378 | 1BzknixNDGfyesGcTbFuyEiD2nyCgEY6rS |
| 2009-12-20 05:06:05 | 2009-12-20 15:06 | 7h 59m | 479 | 1zo1ifkrGNggtBKPhCn4486xHaaWBbXUd |
| 2009-12-20 08:30:38 | 2009-12-20 18:30 | 3h 24m | 204 | 1HRhFWoCspCQWfnotkHPc7Joi4XHjRBi8Z |
| 2009-12-20 08:49:50 | 2009-12-20 18:49 | 19m | 19 | 1NVTcGUYSP6s4zH95ex86ctATzv8peV5mR |
| 2009-12-20 13:30:44 | 2009-12-20 23:30 | 4h 41m | 281 | 1EmRU4xtkAsisWyALP7cJnRcWkkWHs9DvW |
| 2009-12-20 21:35:33 | 2009-12-21 07:35 | 8h 5m | 485 | 12JMQYae1sR4FMupqHYafeGqJUY3kf4A3M |
| 2009-12-21 00:53:39 | 2009-12-21 10:53 | 3h 18m | 198 | 1DYXvem7TuGT3oLgF2RsWyVc5ec1sJ82tH |
| 2009-12-21 09:23:11 | 2009-12-21 19:23 | 8h 30m | 510 | 1NChqEan8XUff1YPtgPYC9q2prfR1rXu9L |
| 2009-12-21 10:36:09 | 2009-12-21 20:36 | 1h 13m | 73 | 1C6BG4rqDdnaC3t3mzapNu46j9yVv1x4Eo |
| 2009-12-21 10:50:46 | 2009-12-21 20:50 | 14m | 14 | 1H6ou5ZVaKzyoV3ujeiSqQHncJv831RTcz |
| 2009-12-21 13:15:52 | 2009-12-21 23:15 | 2h 25m | 145 | 1NVou7bbmdsdVLEphqZadmX2gbR3QCDPAz |
| 2009-12-21 13:38:30 | 2009-12-21 23:38 | 23m | 23 | 1FbPLPR1XoufBQRPGd9JBLPbKLaGjbax5m |
| 2009-12-21 15:29:42 | 2009-12-22 01:29 | 1h 51m | 111 | 1KC2mZujBHLTD2NPQycfDowSfni895pXL9 |
| 2009-12-22 22:17:45 | 2009-12-23 08:17 | 1d 6h 48m | 1848 | 1EuHqvmmDA6dFRmDyu4rzk8b7VkAmEn7Vq |
| 2009-12-22 22:34:02 | 2009-12-23 08:34 | 17m | 17 | 18qJJUcMRWyXhMXR3F18vJXaHJRPYrxwYm |
| 2009-12-23 09:57:57 | 2009-12-23 19:57 | 11h 23m | 683 | 1MUzEx65ycYArLPPhxecjKBj4pzMmmjfsu |
| 2009-12-23 10:00:18 | 2009-12-23 20:00 | 3m | 3 | 12KFCJLu9D7PzbZgBLuNMj2MpfgzdDJ7kR |
| 2009-12-24 05:25:50 | 2009-12-24 15:25 | 19h 25m | 1165 | 1P5itXj2ET31bwGTwFx4Xb6EMaGaMRgTtP |
| 2009-12-24 05:58:38 | 2009-12-24 15:58 | 33m | 33 | 1L85SkdcRjMuLYuiKKq5QPywxHUs4GertE |
| 2009-12-24 17:51:31 | 2009-12-25 03:51 | 11h 53m | 713 | 1PGZSrRhYbDDDJPiZHW47ffSFUGTkch2n5 |
| 2009-12-25 01:07:18 | 2009-12-25 11:07 | 7h 16m | 436 | 1yKCpySRz2YQCGoovGSW7wASo9Jp7yhEF |
| 2009-12-25 13:40:10 | 2009-12-25 23:40 | 12h 33m | 753 | 1MjLPVSZBZ7YWjdMrf4DUus4DVAFkpgAmD |
| 2009-12-25 15:42:21 | 2009-12-26 01:42 | 2h 2m | 122 | 1NcXJKwGAbsSBCi86zjgFsLCT8HoT9nVTW |
| 2009-12-26 22:23:43 | 2009-12-27 08:23 | 1d 6h 41m | 1841 | 14RdV6JPBrTVeV5MfFqhGgfsZhMhCFotoQ |
| 2009-12-27 01:11:14 | 2009-12-27 11:11 | 2h 48m | 168 | 1Ba8UQfeUVjSRw8uHNSJ9wZqAZCSqweP19 |
| 2009-12-27 02:05:40 | 2009-12-27 12:05 | 54m | 54 | 17gzLQ924bNxXBHjgJVBaJEQAKVYTqzaR2 |
| 2009-12-27 03:24:34 | 2009-12-27 13:24 | 1h 19m | 79 | 1Ey9QHtKgcY6aLDLW2xBoMxPJbaXxZcyAK |
| 2009-12-27 08:14:03 | 2009-12-27 18:14 | 4h 50m | 290 | 1KnT26DTvstGKW7P6BxMBEz8QbKa1iix9C |
| 2009-12-27 17:26:57 | 2009-12-28 03:26 | 9h 12m | 552 | 1HTUif11qDAwse9fAXwcdM6o4QPx1hqrio |
| 2009-12-27 22:49:35 | 2009-12-28 08:49 | 5h 23m | 323 | 1MN82eH1Eu3hznewHFkfsAajknhj78Uup5 |
| 2009-12-27 22:50:14 | 2009-12-28 08:50 | 1m | 1 | 1X5NfjvcBzdidakWzw37YQPXkBqXr4e6X |
| 2009-12-27 23:16:52 | 2009-12-28 09:16 | 26m | 26 | 1FUjNePwqBv2gcGZFTkCM88jTqD2gWL4NA |
| 2009-12-28 04:16:24 | 2009-12-28 14:16 | 5h | 300 | 15mVDLozNmscibeBCy33yYyH7AKdsuAcKe |
| 2009-12-28 10:11:58 | 2009-12-28 20:11 | 5h 55m | 355 | 1Mc9yttKMqBVWeUUzAHgvq6gzmgLLyELhY |
| 2009-12-28 16:28:23 | 2009-12-29 02:28 | 6h 17m | 377 | 17KSkVatkQBSRDJukfMtgbYFQ2M3uvBL59 |
| 2009-12-28 18:21:53 | 2009-12-29 04:21 | 1h 53m | 113 | 1MRHrSxnmtUTv48UpxorA9PX2nSEC9yndi |
| 2009-12-28 19:04:56 | 2009-12-29 05:04 | 43m | 43 | 15RJkhWxG3PP5AzfR1AHVWovZxFt3nFysN |
| 2009-12-29 01:05:17 | 2009-12-29 11:05 | 6h 1m | 361 | 15zQPNWD3uAa812THBgQP4rVSiYCBRpZ3N |
| 2009-12-29 03:48:46 | 2009-12-29 13:48 | 2h 43m | 163 | 1NqxEQi9pgmoCzi5vh43ByT9EgAbQqcW2o |
| 2009-12-29 08:20:15 | 2009-12-29 18:20 | 4h 32m | 272 | 1HtMsYAjGKqnehgCXpTz8UkAw44ZLGdAJf |
| 2009-12-29 12:49:18 | 2009-12-29 22:49 | 4h 29m | 269 | 17WSviRk42u6vUbLg1xUixCQfC5t1zgjQX |
| 2009-12-29 13:09:44 | 2009-12-29 23:09 | 20m | 20 | 14CmMfkbvkfzM1cU68wZMVBwJuSE3iN7Ns |
| 2009-12-29 13:41:38 | 2009-12-29 23:41 | 32m | 32 | 1NWRrbPwHhpp28eQeman5YRV84D2aYe1Yw |
| 2009-12-29 19:21:50 | 2009-12-30 05:21 | 5h 40m | 340 | 1Ef6TCo7MMqMepWZ6tKAAEUyigTqJWpjPT |
| 2009-12-29 20:40:26 | 2009-12-30 06:40 | 1h 19m | 79 | 189k1PT89s9tUMigeJxHoccu44QRwEc2Tf |
| 2009-12-30 02:25:53 | 2009-12-30 12:25 | 5h 45m | 345 | 17u34144cabkgraRhwLuzKUANYzf7UB5Jq |
| 2009-12-30 05:08:39 | 2009-12-30 15:08 | 2h 43m | 163 | 12jaQdf2C29Cobh3XZHj4WoPk8o91MK4jy |
| 2009-12-30 05:46:55 | 2009-12-30 15:46 | 38m | 38 | 1LJc6PhvkmLvcqg8wcjJw29kXXm6rfFGMi |
| 2009-12-30 07:05:39 | 2009-12-30 17:05 | 1h 19m | 79 | 1EwiVkDkBLVUaoPuFVzW9NA82iaUUPZruU |
| 2009-12-31 03:31:06 | 2009-12-31 13:31 | 20h 26m | 1226 | 1LTXYmotcmkwp65Zv1UtcKaRNRrFQYmduP |
| 2009-12-31 05:37:04 | 2009-12-31 15:37 | 2h 6m | 126 | 151iVadZ37FF6JLSZzjGyM21U3pBv8tyt2 |
| 2009-12-31 06:05:39 | 2009-12-31 16:05 | 28m | 28 | 16TGQooBCkfV68AKPEKJ8HG4dUEecmSckv |
| 2009-12-31 23:30:50 | 2010-01-01 09:30 | 17h 25m | 1045 | 1FxyVmPEsnqnVS8baCjyuTDsdFHB7reTam |
| 2009-12-31 23:31:59 | 2010-01-01 09:31 | 1m | 1 | 1EAGWgwskQB6o3f1GGsbsWShXPr77QiULE |
| 2010-01-01 03:28:39 | 2010-01-01 13:28 | 3h 57m | 237 | 18sxpzUF2QK3WBiaNUt5oyFV7fcuL9xRo4 |
| 2010-01-01 05:16:48 | 2010-01-01 15:16 | 1h 48m | 108 | 1DYHUEjrVE5gyKAn7P13wuRhs6x9EeijBX |
| 2010-01-01 07:36:22 | 2010-01-01 17:36 | 2h 20m | 140 | 1FuF5iWcHnEPMAhpk5cH7bzdZqjvKTdwka |
| 2010-01-01 07:37:03 | 2010-01-01 17:37 | 1m | 1 | 14ZiwXFoDVKoxVyKjeZjdtSHsYnJxSRFSH |
| 2010-01-01 08:26:40 | 2010-01-01 18:26 | 49m | 49 | 1HGHEhR1tFjiF895SC2PHgRiZyGjpTV5dg |
| 2010-01-01 10:58:02 | 2010-01-01 20:58 | 2h 32m | 152 | 1M2iLUvkkm12zE1EjARx46XXA1EZzsfxos |
| 2010-01-01 11:35:21 | 2010-01-01 21:35 | 37m | 37 | 1FXcjyxCRuJkY72zrLxBjtEReQdv4f89pc |
| 2010-01-01 13:18:35 | 2010-01-01 23:18 | 1h 43m | 103 | 1LK8dnWdxZWxLcdTCpqHRebGwwVcMAPo6X |
| 2010-01-01 19:34:09 | 2010-01-02 05:34 | 6h 16m | 376 | 1Q9mvLQSHc4if71KZPG43re568u65ikQo1 |
| 2010-01-01 23:17:37 | 2010-01-02 09:17 | 3h 43m | 223 | 1JMPLmKGdgD9Dtz3a4b4HpQzxZ69uVvUbS |
| 2010-01-02 01:12:53 | 2010-01-02 11:12 | 1h 55m | 115 | 19PYG68GkQ9nY99QeUSyUFy6vWxSyPmXA8 |
| 2010-01-02 11:58:18 | 2010-01-02 21:58 | 10h 46m | 646 | 1CdZDnukUZ4QK3Ynjk5hukupczV2zzrXPh |
| 2010-01-02 13:45:51 | 2010-01-02 23:45 | 3h 47m | 227 | 12cFuwo1i3FMhkmJoCN8D4SjeCeRsXf96q |
| 2010-01-02 22:09:04 | 2010-01-03 08:09 | 6h 24m | 384 | 1FVD5rzMP6tR8JuubgYSFLopiP33HnSGkZ |
| 2010-01-03 03:52:50 | 2010-01-03 13:52 | 5h 43m | 343 | 1PwaHB72F5nb7hurX8jmC93MUDtMqHgdCY |
| 2010-01-03 03:54:50 | 2010-01-03 13:54 | 2m | 2 | 1BMnca8dAqphg9e98ALoZyJch2NmDirvyY |
| 2010-01-03 09:10:59 | 2010-01-03 19:10 | 5h 16m | 316 | 1BPo3xfuLWD5xZRVU61o9bEbW2XXyWLduY |
| 2010-01-03 19:39:12 | 2010-01-04 05:39 | 10h 29m | 629 | 15yfaq9UKSvPFTpP2q3VHwMfW8edwrxV7z |
| 2010-01-03 21:33:26 | 2010-01-04 07:33 | 1h 54m | 114 | 1NdmEC5HxfLSH6Z5xoxQUC8h3sfFoTSSRD |
| 2010-01-04 07:06:36 | 2010-01-04 17:06 | 9h 33m | 573 | 12Q8NX5RdYYAf8gA9NM5DALzWWtU5dZHxW |
| 2010-01-04 09:20:59 | 2010-01-04 19:20 | 2h 14m | 134 | 18pxRfY6BgE4W4gSfog6FFZBwGs1fcEre5 |
| 2010-01-04 12:36:45 | 2010-01-04 22:36 | 3h 16m | 196 | 1EpU3v1wRsPxBkpCsZCiA8QGa8jYXSREi8 |
| 2010-01-04 17:45:27 | 2010-01-05 03:45 | 5h 9m | 309 | 1DkxqjACGihnBHhiWGuJUMVRco6LHFpovT |
| 2010-01-04 18:29:27 | 2010-01-05 04:29 | 44m | 44 | 1BByuLe4598R4cxG163Y4g2th5yu5D2x98 |
| 2010-01-05 13:30:17 | 2010-01-05 23:30 | 19h 1m | 1141 | 1LfgsdyXxa59sggxG7iHC2jZdy26fWqBij |
| 2010-01-05 13:58:35 | 2010-01-05 23:58 | 28m | 28 | 1LBUqhwVyUZ8QZw8UCEbgFQjDFjikL1CSB |
| 2010-01-05 17:09:46 | 2010-01-06 03:09 | 3h 11m | 191 | 1VketozRRbdwxygHPRh4BL4jQgnH3xPWt |
| 2010-01-05 17:11:54 | 2010-01-06 03:11 | 2m | 2 | 1HCvxY4EW8P7EpXCYpRTLrrNuRfEdb4wuV |
| 2010-01-05 18:03:19 | 2010-01-06 04:03 | 52m | 52 | 1FTtHk9sc29yJXWcxKJdKz8C6YHyAQMgwU |
| 2010-01-05 22:29:13 | 2010-01-06 08:29 | 4h 26m | 266 | 1LVWSzpeQyoHYPzDuYVktPuH8qJqBiskUF |
| 2010-01-06 03:52:00 | 2010-01-06 13:52 | 5h 23m | 323 | 1LWFZazDBRt6bGDb8ukkCo4H9o297S8pma |
| 2010-01-06 11:09:17 | 2010-01-06 21:09 | 7h 17m | 437 | 13PaeVWHFvEVWjUJiCAono12o39CLeBEEd |
| 2010-01-06 13:31:13 | 2010-01-06 23:31 | 2h 22m | 142 | 1MNaNPHzju2KWAoPshfDBxknSSC5dWkfy |
| 2010-01-07 14:05:47 | 2010-01-08 00:05 | 1d 34m | 1474 | 1K3Qs6bx1wnxCjLcb6jxfjk5kksSJh1WyK |
| 2010-01-07 15:45:46 | 2010-01-08 01:45 | 1h 40m | 100 | 1AfE9BbPDPGx8egt5qRBo5vLDiy4RrLNeV |
| 2010-01-08 00:39:12 | 2010-01-08 10:39 | 8h 54m | 534 | 1PDUuvJfhoiijbqnGeHZZwXRJoBCsaQSr9 |
| 2010-01-08 02:18:58 | 2010-01-08 12:18 | 1h 39m | 99 | 1MraZtUepR19wk9Nti8dTnfUKDmXZUigT5 |
| 2010-01-08 05:22:04 | 2010-01-08 15:22 | 3h 4m | 184 | 12KFrqyEEtdvrSvfWvXYtieKoFZgoSgbXi |
| 2010-01-08 06:01:24 | 2010-01-08 16:01 | 39m | 39 | 12vQPdDVU8KHeXMSXBY7e4rRierNjWETLi |
| 2010-01-08 07:32:28 | 2010-01-08 17:32 | 1h 31m | 91 | 1MTMH8rnXtfTkPrNt9xpZVy2D95sKf8hYy |
| 2010-01-08 11:58:22 | 2010-01-08 21:58 | 4h 26m | 266 | 17iZXQzMYjxBxRbThhs36fmgR3cRKuD1yP |
| 2010-01-08 13:02:57 | 2010-01-08 23:02 | 1h 4m | 64 | 1VaPTvD7fn6dYN9ka9WUi3jN9mBiGnWF1 |
| 2010-01-08 16:37:02 | 2010-01-09 02:37 | 3h 35m | 215 | 1Kynn7w9MF8hUvqdaHRKY4KLWtwnGdH2Uo |
| 2010-01-08 19:40:21 | 2010-01-09 05:40 | 3h 3m | 183 | 1PLU3ytAptPgHXWujCrcxLzqg4LdFX2bu2 |
| 2010-01-08 20:17:25 | 2010-01-09 06:17 | 37m | 37 | 1KH2yPhaxPKKh53Vqkghjn2jfXDJWHRpbJ |
| 2010-01-09 00:23:49 | 2010-01-09 10:23 | 4h 6m | 246 | 1Gd6DBfutYmwr6Z7CtV8pQiRXG3ZGhw8GX |
| 2010-01-09 00:24:15 | 2010-01-09 10:24 | 1m | 1 | 1LHgE4M96DyCt7J5H2wzcVPWNJt9zD1U5f |
| 2010-01-09 02:51:44 | 2010-01-09 12:51 | 2h 27m | 147 | 1DpuecprK8vV6A4FtHU6VLqkUs4D2P59PU |
| 2010-01-09 05:51:54 | 2010-01-09 15:51 | 3h | 180 | 153w6WiJW1Z2uKYegDVVbbBYYhzps6VmWr |
| 2010-01-09 12:45:14 | 2010-01-09 22:45 | 6h 54m | 414 | 19TfJPQDTFT4uZj8vYn4ff3rxRxBTBELu |
| 2010-01-09 17:31:45 | 2010-01-10 03:31 | 4h 46m | 286 | 1LBmJDqhNboEbyJveb8jB5TNKW5GW7qboN |
| 2010-01-09 19:24:07 | 2010-01-10 05:24 | 1h 53m | 113 | 1HhHqRamECC7y4qfSEeYNvLJKCRUkxBY1u |
| 2010-01-09 20:02:29 | 2010-01-10 06:02 | 38m | 38 | 1CoFNuTemGzFPHqkuz2Ai5ZaweM7zfPJE6 |
| 2010-01-09 21:20:39 | 2010-01-10 07:20 | 1h 18m | 78 | 17fH8bs2eBSxYC4fLQgVPWXw2cV5bNrpon |
| 2010-01-10 00:16:01 | 2010-01-10 10:16 | 2h 56m | 176 | 1LsZpodgMzW8bzHiSQS1kpZu9JzpdVLPB9 |

</details>

Note that some block intervals are less than 1 minute. The theoretical Bitcoin block interval is 10 minutes. However, in 2009 (the Genesis era), many block intervals were just seconds apart (e.g., blocks 33786-33787 had a 35-second interval). This wasn't a system bug but was determined by the hashing power and difficulty at the time. Hashing power scale: In 2009, the entire network had fewer than 20 computers mining, total hashing power might have been only a few MHash/s, and mining difficulty was at its minimum of 1, making it easy for consecutive blocks to be found in very short timeframes. Difficulty adjustment lag: Bitcoin adjusts difficulty every 2016 blocks (about two weeks). If someone suddenly joined and the difficulty remained the same, block production would compress dramatically. Few network nodes: In 2009, a few core miners were directly connected, and block propagation was almost instantaneous. Once a valid hash was found, the block would be accepted by the network, and the next block could begin.

Timestamps. Traceable ledgers.

This demonstrates one thing: Craig Wright not only still has the private keys but has also preserved every single `wallet.dat` file intact.

The Tulip Trust's 1.1 million Bitcoins were a decoy to mislead his ex-wife during the divorce. At the time, Satoshi was 41, his wife was 59, and he had developed a new relationship with a colleague.

David Kleiman received only a list of addresses, containing no private keys, no 15 shares, and no trustees.

Craig's active contact 9 months after David's death was to obtain any remaining Bitcoins David might have had, as the price had then surpassed $1,000.

Going to the UK was to sell patents to Calvin Ayre, seeking third-party backing to solidify his intellectual property claims.

Shattering the hard drive with the private keys, with a lawyer present, was an act of regret, a desire to stop and silence the outside world, as the signature farce had led to a prolonged Bitcoin bear market around $200.

The theft of 111,000 Bitcoins was a fabrication to evade legal liability, as those addresses were closely linked to exchanges, suggesting involvement in market manipulation.

From start to finish, he has always controlled the private keys.

Satoshi retired when the CIA invitation came. The Kleiman v. Wright case forced him to disclose his address holdings. Satoshi's only fear was the U.S. government and American law.

---

## 🏁 Chapter 14: An Annual Salary of $100 Million, Bitcoin Community's Special Consensus Mechanism

### 7.2.1 Everything is Fake, Only the Continuous Selling and Cashing Out is Real

Satoshi has always been selling Bitcoins. Starting from January 16, 2009, until January 2010, Satoshi consolidated his Bitcoins about 40 times. Finally, between June 5 and June 28, 2011, he sold 77,622 Bitcoins through address `12higDjoCCNXSA95xZMWUdPvXNmkAduhWv`. At the time, Bitcoin's price was approximately $6-19, netting an estimated $500,000 to $1 million. This was also the first large-scale influx of Bitcoins into the market. From early block 235, you can see that Satoshi started consolidating and selling Bitcoins from November 2010, when the price was around $0.30. Traces in blocks 2775, 3549, 4164, 7312, 8970, etc., all confirm this.

He sells every year. Between October 16 and 22, 2013, he sold 58,916 Bitcoins, cashing out about $9 million. On March 7, 2014, he sold 261,114 Bitcoins, cashing out $120 million. From 2017 to 2026, over 10 years, he sold 10,300 Bitcoins. In 2024, he sold 3,200 Bitcoins from 64 addresses, cashing out approximately $250 million. In 2005 (likely 2025), he cashed out about $50 million, and in the first half of 2026, about another $50 million. These are just the tip of the iceberg.

Timestamps. Transaction records. Immutable ledgers.

<details open>
<summary><b>📐 Table (Default Open, Click to Collapse)</b></summary>

| Block | Sell Address | Sell Amount | Sell Time (sorted by last on-chain action) |
| :--- | :--- | :--- | :--- |
| 3607 | 1724SVrgVffLtzDspyQ7HRjuARbevPRe3D | 50 | 2017/8/7 9:32 |
| 44516 | 1N9UxRnma1qhrRzRnUJqBNCxB6tKrxpVJ8 | 50 | 2017/8/7 21:21 |
| 43049 | 1PREbw45NGEeqw76eG7n6RUfCSQvwjHrea | 50 | 2017/8/8 0:18 |
| 44539 | 1LYMFbD4wyh3KaJmpXvDxY5VKAeaXTxNix | 50 | 2017/8/8 4:48 |
| 44838 | 1K7fCf5bHvL373jziXf888KLDRdGL2vPHo | 50 | 2017/8/8 12:46 |
| 26384 | 1365vvPoaXL31PCJyNpr1CdTzZVD543iyf | 50 | 2017/8/9 1:55 |
| 43048 | 1uQRmZaQKyhgzQhMt7jPr1DCDfVTxNfkh | 50 | 2017/8/11 1:54 |
| 69014 | 16fRBuDTNbZoLf3LNvhWZ7Y94QdYrwL92n | 50 | 2017/8/23 4:00 |
| 48684 | 17DVWgmaWGJW4MD3dkUZK5HFoohxFiLEHu | 50 | 2017/9/1 21:40 |
| 45742 | 17ETAdwRyf1AD6azkAgq8g7XTtjbaMKZg6 | 50 | 2017/9/4 16:45 |
| 65569 | 1LT3cRQomYByi5WvRRwCB5pKDRUuXHxUEe | 50 | 2017/9/20 20:58 |
| 73951 | 12XDcpW26vaDqivxa6A5t8WqRLtUGGeoTd | 50 | 2017/11/7 2:02 |
| 73260 | 13ByKS9hFsGhLPQuJJaUPVtMfimKHEZnQK | 50 | 2017/12/2 7:04 |
| 68974 | 19FE11dXT18BkFtTMkcpJkNV7UPGQvz4fj | 50 | 2017/12/3 9:11 |
| 68006 | 1CyqXTcHSBLwbPhiDeRPVVKcjGBFzKFBBG | 50 | 2017/12/5 1:55 |
| 68291 | 1AjxnYs6WpKLuZ5aE8K7EjBoWSHGTyrJ6X | 50 | 2017/12/8 0:51 |
| 66390 | 1GKZtkiGQKXqXKH46piTc7q2tK6YrPV1Lu | 50 | 2017/12/8 6:26 |
| 65956 | 12uapYy6aTSsGHXdUY2PZShEXpNDdadyuz | 50 | 2017/12/8 6:29 |
| 53950 | 15NnGcUgVqxMvZjbAk9yYgCXppgGb4bH3q | 50 | 2017/12/11 5:58 |
| 55260 | 14GruSDDTQp9Mih2BrWG1vQTT1EKzM8MRH | 50 | 2017/12/11 5:58 |
| 69617 | 1LrYXEkJmJoY6gT6LSaeaw2CtC31gFWDPV | 50 | 2017/12/14 1:13 |
| 55173 | 1wnoms8t1M7AsSccXm9PxJxGtXGpYUXQM | 50 | 2018/1/3 22:59 |
| 33281 | 12Xt1MSxCALfr1pHBeScLkGYgUvp6xyHC2 | 50 | 2018/1/5 17:17 |
| 58349 | 1MN3ep1fE9NdvXdjavKjDs62KYVPmzgyLr | 50 | 2018/1/7 22:21 |
| 60141 | 1HPMchnz5uUMkwECCi8zCVAMMJPCmZJmqu | 50 | 2018/1/26 7:42 |
| 65005 | 136ft4gXzbCFt92ox7f956ydsyk3nBiLJs | 50 | 2018/1/30 11:25 |
| 68204 | 1AfyJ9fhMP6tXNTwzJyA2U7kwSrkNgQjuF | 50 | 2018/2/23 9:59 |
| 66996 | 1HofAbRzMMmEkbmpdpm7pvLKfkxXEXsTVU | 50 | 2018/2/23 16:16 |
| 67158 | 14gnZXG68dY6z3Jzo9qzd4wZvKmfFSuMHS | 50 | 2018/2/23 16:16 |
| 69442 | 1BcFVcDnAEopkjZ51aDbNvDaQT3oApYVkN | 50 | 2018/2/23 21:58 |
| 66724 | 14bA8oHHUdcjaZiis3N47FKYuVHHvrKStB | 50 | 2018/3/19 14:21 |
| 33784 | 16UyAsTwJYC9jkWJCSQL8rTFGqruwUvKvX | 50 | 2018/4/25 4:07 |
| 33538 | 1GdqwQ8Btsw1RPnm7yVwmexbSsG8A5fFHW | 50 | 2018/5/4 19:13 |
| 33590 | 1Lupc53c2MHo4xahh7eG2muSwxn8WpVeKx | 50 | 2018/5/4 19:13 |
| 68603 | 12gSps8bLgXNynsMtqU58M6Dw6oGq3yD5V | 50 | 2018/7/18 13:13 |
| 71722 | 19ktNCvX746q1GS59jvkDPk3tHNQ9tg8x6 | 50 | 2018/8/21 14:43 |
| 61047 | 17xRhUGkt1iYzFC7ZzgBk9mz9tZmaYvemo | 50 | 2018/11/24 11:51 |
| 56710 | 1AyGqRJnrSAVsMbQQvwMqBjkTEhu14niLy | 50 | 2018/11/24 12:34 |
| 52644 | 1G7Jgr8VpqHGZ2TinHRqvWPfAy1vo3ws8C | 50 | 2018/11/24 13:56 |
| 52652 | 1F93pUz4y7u9zZNQofkeQFzY9nkP3eAAuF | 50 | 2018/11/24 13:56 |
| 52632 | 16HjNFdFoYMRMkgnQrrx8jtpUH9qNR9ocN | 50 | 2018/12/8 18:45 |
| 66336 | 1EzuqaYYD4g5tkiV9gb7X4eVo2Pvt83Vfi | 50 | 2018/12/21 16:20 |
| 68283 | 19Q5JPo4U943AzwZWwfsZ1xBvg7QqJQkaG | 50 | 2018/12/21 16:20 |
| 66637 | 16JrmsHTAxQkgbPKE33o2rcBrAozSmCqSk | 50 | 2018/12/25 0:06 |
| 45697 | 13hNoMaevg1oCtSQq8ATcWvaQfPj1YN6eg | 50 | 2019/1/21 3:46 |
| 66446 | 19iPXFFyEcxsh8Ad9Xe5VYPe7RtnRcZ95S | 50 | 2019/2/19 0:34 |
| 69951 | 1Cws5uonX5XfJ5niyyCU5TXsWNFjABSuxG | 50 | 2019/3/19 22:25 |
| 66188 | 1KecU3fG7B4p2DhUExh1JKGMRYeefZiDcn | 50 | 2019/4/8 13:20 |
| 73303 | 12dz76LTr3opvqLSQKhsSJwXAMJ53CHbh5 | 50 | 2019/5/24 6:59 |
| 56617 | 1LeukqNkTGsiK6d5Bseqhzr5DgetFovJi2 | 50 | 2019/6/22 11:52 |
| 60768 | 16knHmP26b1pW21GwDr43A7WjpNm4oJHxz | 50 | 2019/6/22 11:52 |
| 61100 | 1NhkeF3aDUQcCzv4KDUpE9SjsYY3KHWLcs | 50 | 2019/6/22 11:52 |
| 59145 | 1KAJKUr9k1QaLBWSE7genKr2MgyfidasZ2 | 50 | 2019/6/24 11:29 |
| 70022 | 1EpArYtgmpS8hef649k6Fd1DENeTtm4ZCC | 50 | 2019/6/24 12:26 |
| 67992 | 1MrGyfhs6JhTpJRWSXuGGEGXG8qGF8GJrd | 50 | 2019/6/27 21:57 |
| 69302 | 13zG2LpCJHm1PpwffNuhz63p3eGEbRTEkT | 50 | 2019/6/27 21:57 |
| 69382 | 1GKAnL7pG6DpuUnRAUimqYskUAaaS4C5RF | 50 | 2019/6/27 21:57 |
| 70086 | 1CajXqwWoiQFxfSfWqXGCB4YT7mo1yYD3E | 50 | 2019/6/27 21:57 |
| 70698 | 1APW4vZeoNzJCc5uCvhBWJJwyMTKMJ96AK | 50 | 2019/6/27 21:57 |
| 74361 | 19s2jwXTwsvFDWo1Nh4Md61QKDStu11tge | 50 | 2019/6/27 21:57 |
| 65880 | 1NZnQtrzp4rFhpZZYVdGEoSg47hFpgVb1n | 50 | 2019/7/8 5:53 |
| 55660 | 1NUQ3f2JxnNpmV4fntAme9QWzuqfesP1CL | 50 | 2019/7/8 11:44 |
| 57585 | 1Cm4ZiSHwaxK6rT7cbqhWtxTGjcbSrWFzp | 50 | 2019/7/8 11:44 |
| 63790 | 18cLVrEcjvZVCifZNGXA7spJBAGkjP5fd6 | 50 | 2019/7/8 11:44 |
| 67690 | 1EMLQWjhgkMeA9nN6mxZVQNVcBX3joDG5M | 50 | 2019/9/3 3:03 |
| 67807 | 1Ao6fVphQA9r1WCxBncsjRiUtRyPYjgfKe | 50 | 2019/9/25 5:40 |
| 68668 | 1Ex9kQ5poWaTP8a45CT573NG7MzysYxb8 | 50 | 2019/12/20 8:26 |
| 75190 | 15vYxqxHcnPxCyoj3d3XRqHhae7R7TEjh3 | 50 | 2020/3/11 8:19 |
| 75295 | 1C8mZECqe1bjJug1nYKKLqejKxJBVeaJb5 | 50 | 2020/3/11 8:19 |
| 57436 | 16erb3D9TbmnW2U1bFnKSjQuqohXasMARi | 50 | 2020/5/7 2:46 |
| 66680 | 1Lgifz1ujJPUabzM7e25D8kKcpNqB9Czmc | 50 | 2020/5/13 9:14 |
| 3654 | 17XiVVooLcdCUCMf9s4t4jTExacxwFS5uh | 50 | 2020/5/20 20:54 |
| 57504 | 19h7oPeqkQeQAqKcNTGKkKr1Xd2AZ85xL2 | 50 | 2020/10/2 4:15 |
| 71521 | 1KRQqX1y3r8vyybG9Az156GdsBbpaUN8Po | 50 | 2020/10/29 13:00 |
| 70894 | 16qvrdawnsSQq68zfbT25xKKy2DePgPXwS | 50 | 2020/11/7 6:40 |
| 75398 | 1M8UZH7GXURswAYLVYSAVnTwYaZwjUojrF | 50 | 2020/11/7 13:37 |
| 66360 | 1DZWaUmuZucKzhA3DrcfSzUHo9TWmkbXTN | 50 | 2020/12/22 9:10 |
| 54171 | 1KicDu3bRF417QXKVHSsKjT22AJZTDMv6s | 50 | 2020/12/28 4:10 |
| 49428 | 1JCR2VJJVv5x3g8QEyPhSFpx3XTQoigGgC | 50 | 2021/1/3 10:28 |
| 49664 | 1L4QX44JMT8Pn6Ga5AyiY8AZyRr6vG4cot | 50 | 2021/1/3 10:28 |
| 49709 | 1CD5w33xpfp1P1hTFFRkxVNwfM4xfp22uY | 50 | 2021/1/3 10:28 |
| 62008 | 15v82kK4nQTnVx5ApuNDjA4uaGLhsWwNBN | 50 | 2021/1/8 9:11 |
| 67157 | 1DGWivpu9x1ZFkYJvhS91o1zp851CguPXB | 50 | 2021/1/14 10:37 |
| 72219 | 1NrzajTRDXdABV9tDvP75uLvCmv3A7fce1 | 50 | 2021/3/3 12:57 |
| 57848 | 13zAxktmqtUainuQBji5o6mSuiPA8tB6fX | 50 | 2021/4/10 9:05 |
| 66448 | 1K2196ZjtBhgxLDkqRbvcHxtnaN7fM4xcM | 50 | 2021/4/18 20:09 |
| 66718 | 1LsBSCxzDbRe18BrHMe1UKXKS6eoa4tmxc | 50 | 2021/4/18 20:09 |
| 73243 | 1F9Jncjoa6VNo4eFEGRvAMUEzQVry2WrPP | 50 | 2021/6/7 7:33 |
| 75015 | 16qxewbNQwHYdjQHx9HjEtxXaac9gvituH | 50 | 2021/6/9 7:41 |
| 75188 | 16hqbeAuVSmQxaEPA14q9qV3RhhdUYSAQX | 50 | 2021/6/9 7:41 |
| 75072 | 19xH51AGLMKGsKChDp38DRVQgSdFh3iMUh | 50 | 2021/11/10 14:32 |
| 75277 | 14nV5B2FxoWtgSvDS4N3puii1pyuund4jz | 50 | 2021/11/10 14:32 |
| 74869 | 1PCZnzs7kLFwjN4fJ44Zy9oZzsUxXg881W | 50 | 2021/11/12 8:47 |
| 75135 | 1J2W2P774QqnhpBfacSuqKHeVLRv2qG8JE | 50 | 2021/11/12 8:47 |
| 53784 | 19WZyg9VvnBbJPLDk9HL8H93hUbXwSPMER | 50 | 2022/2/5 4:54 |
| 68294 | 1fgs29YSWy4hhn2mBHugmjDRjbmmAKuPX | 50 | 2022/2/18 22:00 |
| 27811 | 1CUe12WDAo1DadWj1Y7XMXV2J8PiGsn2F1 | 50 | 2022/4/7 10:23 |
| 27749 | 18RrgpKNjMefzfrW9MSbQRd9pCK96VCwMB | 50 | 2022/4/7 10:53 |
| 27742 | 1Dt4PRm22rRbkX2yiwvtPNT1gRyJWQN8dx | 50 | 2022/4/8 3:25 |
| 27694 | 13NwknCrxfCunGC3NqcLwycR3ua8P9rNLf | 50 | 2022/4/8 3:27 |
| 27693 | 1AefXTGb6ZfTuEvDqVAGyGHFSxk5zmavuC | 50 | 2022/4/8 3:42 |
| 60781 | 1LaMDohdv7B3AtTEZcY9BkgqBY9yaZeiR4 | 50 | 2022/6/5 5:20 |
| 56573 | 1Li8RFUotXHJPNazCM8HAfnkxKcrKXXpiH | 50 | 2022/6/13 9:03 |
| 65974 | 18eXJskHRVvKrqmxD9T6K6UQ6GBC6ya2WS | 50 | 2022/8/22 21:30 |
| 56725 | 186C6SJ16yFqGbDbfvSfFoujSP2Ph235HJ | 50 | 2022/11/11 22:39 |
| 57150 | 1LB8BHdaRjeRsxz8SqiAFFQLjXkzCKsgvX | 50 | 2022/11/14 21:18 |
| 68709 | 13UXyHZsVRLeu28VEmdRF3pduSAxzcHL9k | 50 | 2023/2/1 13:32 |
| 71446 | 1QC2eAKL4dmvvaNUwCcxobKhewRubj4rWt | 50 | 2023/3/21 2:22 |
| 50153 | 16M6tUcPmpVkZ92Lr9mGRuiEiubJgRav9N | 50 | 2023/4/23 7:08 |
| 65670 | 1B67KGYNMxPB6cznHTTzgGprmw7kBxTRB1 | 50 | 2023/5/22 17:26 |
| 65899 | 1MSij5Qi9EbxGFLB9RmfHEFvfK51a9B3hx | 50 | 2023/6/26 8:15 |
| 65755 | 1PJs7kzDby9887tGMjFQ7fPhUzSFtm7mTS | 50 | 2023/6/26 9:28 |
| 56754 | 15tABe48T1RH2sQXCtztL74R9me3VPehni | 50 | 2023/7/25 4:25 |
| 65028 | 1BNE4d6jASBNc4yH8JXhhturSEQ2zpXBtR | 50 | 2023/11/7 9:52 |
| 73676 | 162jcE2Ko8fGTVrWD83q4NkPEpXppNwVp2 | 50 | 2023/12/5 7:15 |
| 74923 | 1ihNQYhAVdYbfzVriTd2BALVKcQoDQncP | 50 | 2023/12/5 7:15 |
| 75300 | 1F6YBWsbUefAA55zEkPPNzQ9YV2yadbSDY | 50 | 2023/12/5 7:15 |
| 72491 | 1Ke2UGX1vSi1DTp1Dokn2gD7pxjheCV2n8 | 50 | 2024/3/1 14:05 |
| 73631 | 1LnMTFabWpFawxfW6MyugUH7ALtVtj9ZHN | 50 | 2024/3/1 14:05 |
| 74160 | 1PFiuBGXb2KvrAMRvqMNBorrCkzdxQ2Dbt | 50 | 2024/3/1 14:05 |
| 71233 | 1G9XujyrdutqMv3pxrfMiMAAveq3GCmsmU | 50 | 2024/3/1 14:05 |
| 71666 | 1JFfHjB1J9pkaT6ytbyqum9PFCBWfYojba | 50 | 2024/3/1 14:05 |
| 71823 | 1DTKBkdHJvZDkqFT9PdLHtQzS74YZE21on | 50 | 2024/3/1 14:05 |
| 72036 | 17xy64MKzpTD989jffFu13P9rMF4uJGN5Q | 50 | 2024/3/1 14:05 |
| 72646 | 1J93SgZsMThTcZu7Ys747eFuv2KAqr1MpW | 50 | 2024/3/1 14:05 |
| 73780 | 17xChDGjrugzo3UK2YpBVZL7EcHbDDNcnb | 50 | 2024/3/1 14:05 |
| 74467 | 1JJXKSHCFYjkKcoTGytELce42R6Nr4yvQ8 | 50 | 2024/3/1 14:05 |
| 74603 | 1A4AuRSuLaS3zoVMgbtorKwWgiafK8uaeV | 50 | 2024/3/1 14:05 |
| 74751 | 16pQwUvtE6RWw4AkdeMLF3QHy8YcSRE5BH | 50 | 2024/3/1 14:05 |
| 75011 | 1PZ1RjRbMuUoon8LdDS7s5exmNyRnrobXN | 50 | 2024/3/1 14:05 |
| 75243 | 14fA7bM2R9qjZshaN8EdJbJtwTQAeBspSV | 50 | 2024/3/1 14:05 |
| 72454 | 1PLasr7jgWei2BTR2ezcKSDEj16bJhoDm5 | 50 | 2024/3/5 14:41 |
| 73129 | 1DCQK2K679exaPfU2yFgh4bgeeTL2n8RPL | 50 | 2024/3/5 14:41 |
| 73766 | 1NtaZN6wvty1wdG7AzZokzY2qGcjXRBzLQ | 50 | 2024/3/5 14:41 |
| 74513 | 19GmMByQuc65wLs8wCvcVzRHg1WLp5tP6g | 50 | 2024/3/5 14:41 |
| 75075 | 1741wGBVobpPAqio2oxZ22bSbGgaq7H2ks | 50 | 2024/3/5 14:41 |
| 72402 | 1PMutfNXM2yPvLDQ96CNXRprgrh2Jro1wj | 50 | 2024/3/27 5:24 |
| 74605 | 14mDnNuYWSmepCteWHKQ1GwgZJGnRHV56J | 50 | 2024/3/27 5:24 |
| 71723 | 1EFAnRpBEd5peAmWViquCannngyUs4eHAb | 50 | 2024/3/27 5:24 |
| 71926 | 18WnVtU8L1EKgpM84Mxz58iwASDMZuZ7Ck | 50 | 2024/3/27 5:24 |
| 72087 | 15PeDV6dyrziNZZu9hVMA6s9ipCufjSNkN | 50 | 2024/3/27 5:24 |
| 72565 | 1A9yn5Vs88BTaGtUpc1zH35XDXnvDsc29B | 50 | 2024/3/27 5:24 |
| 73097 | 16bjqqXccN8Bh2xkvgT7wBiKZFp3KpfBwz | 50 | 2024/3/27 5:24 |
| 73508 | 1M9iYBQQhiM6kzM3WG5Biaoo1WyehVrqv4 | 50 | 2024/3/27 5:24 |
| 73660 | 18tfGZNAc1DYaPsJiFa8Pzbh4bcJ9UW9Mx | 50 | 2024/3/27 5:24 |
| 74506 | 1GEW32A6dTQ5qeJKYendwYDeb8gA8eBPtb | 50 | 2024/3/27 5:24 |
| 74750 | 13P38TDmicdTXCpBvHksNMwQf1YQjV5LvP | 50 | 2024/3/27 5:24 |
| 75031 | 1GYyMY38JCLAjjpdUsDNa7q32PKSaGJRR7 | 50 | 2024/3/27 5:24 |
| 75186 | 1B2SUiaUtBTceh1jALLjUDwDRAgn6bcpcj | 50 | 2024/3/27 5:24 |
| 66611 | 1AmzfC1ZVu3Nt6Us3oK3ApjwKYFg7Qxn4L | 50 | 2024/5/22 20:33 |
| 66177 | 13ZB2AmQP4TZv6a6YC9Urqc67yHmMpLBgi | 50 | 2024/5/22 20:33 |
| 70765 | 1GwKDWkQpX1th5yXE48P81hZwrLyXgpHmx | 50 | 2024/5/23 3:20 |
| 71311 | 15CmDkwrrb5T5cgafB3JJjayDDneihTtPq | 50 | 2024/5/23 3:20 |
| 71425 | 1KSo6NqmrCdDw6Az7QiCp5ynd5ACZUSu1R | 50 | 2024/5/23 3:20 |
| 71499 | 12YWsHLW47J58b4Ys36ZiyCm31yQUApsEe | 50 | 2024/5/23 3:20 |
| 71856 | 18dnm8rSEDxdUBZVNjFHqTVjrBbdwcJ6y | 50 | 2024/5/23 3:20 |
| 72314 | 11NYqwiDUrhqgVDrVA1KXhsP2eVc8tAGH | 50 | 2024/5/23 3:20 |
| 72627 | 14gVxdABQkf6AuzLsKmyjdaoTpYcxzoqe2 | 50 | 2024/5/23 3:20 |
| 72839 | 19xqr8yDYs9hmVxugQW8cEFBgCv5GoEJx | 50 | 2024/5/23 3:20 |
| 73369 | 17nHn4rfpBH4wbaRtd63RYxaSXfeNzodD7 | 50 | 2024/5/23 3:20 |
| 73677 | 17Qk4gyXwdBRWD2CXSqqc9krWSeTR9YhuW | 50 | 2024/5/23 3:20 |
| 74286 | 1CNjYyChBEk7GL23RkQoTWVsvwQdMBLM6a | 50 | 2024/5/23 3:20 |
| 74842 | 17cvziYUhXqwtdQ9yFmheZbiJpU4NfgWki | 50 | 2024/5/23 3:20 |
| 71644 | 1B1KdZndpPSCCuH789TfGikcDtZhL9ohN2 | 50 | 2024/5/23 3:29 |
| 75400 | 1ExxUpZi6XyueLyhmYDdnEofxKE9LvE2bY | 50 | 2024/5/23 3:29 |
| 2455 | 13J8FkimCLQ2EnP1xRm7yHhpaZQa9H4p8E | 50 | 2024/9/20 14:53 |
| 2486 | 1MBBJBFEaYKHFZAeV7hQ7DWdu3aZktjzFH | 50 | 2024/9/20 14:56 |
| 56181 | 1EYQWBAbUqbKtbBNMa4oakS9vgQKbNjD5A | 50 | 2024/11/7 12:13 |
| 70755 | 18B8nqwgfzhybS7kiNFbcu5izEJAAucE73 | 50 | 2024/11/15 8:08 |
| 71305 | 14pmGAG4stnYECjEJgViJz7Gjf6nKvbrxq | 50 | 2024/11/15 8:08 |
| 71420 | 1JcVd2ny8PP7AjA4AXNBtnnw4NhZqyMaTY | 50 | 2024/11/15 8:08 |
| 71942 | 1DUS4WnfG1fWDoiRGxZaBKVdLreM9Ruvpe | 50 | 2024/11/15 8:08 |
| 72748 | 1GTQHWNyz4U9xp8KmADg37EFzSyRmDtcZA | 50 | 2024/11/15 8:08 |
| 74404 | 1Nv6bC785vofPJbo1gCBAgqBEVhoYwR3t7 | 50 | 2024/11/15 8:08 |
| 74606 | 16tpuUFzzouXjVaieSft9dd9d4CTFxkmos | 50 | 2024/11/15 8:08 |
| 74749 | 1MJUttMoic2tvZKad5o4tX6x1m75b9KpfG | 50 | 2024/11/15 8:08 |
| 74983 | 1LurLBsqAw9ZN9sdjYpi4Frd4bnsNdS8qM | 50 | 2024/11/15 8:08 |
| 72290 | 1MEF1cdAY3o7xuqswYm8hD49Rnm3ZBf2Q | 50 | 2024/11/15 8:08 |
| 72850 | 1Lo6X9n88s4oHEdRZ45wTk61UqmsMqDC7U | 50 | 2024/11/15 8:08 |
| 73223 | 1xfc9vyfTgfZoTjjpg28SnUXSJ2AQduSn | 50 | 2024/11/15 8:08 |
| 70918 | 1JheHjsD46tn4DYNRVKFeYPHmxkbxyDEPg | 50 | 2024/12/14 4:43 |
| 52565 | 15sxzZ4QSaoiMo5KYH9ab4xQj34yeJmKgb | 50 | 2025/3/24 0:38 |
| 65845 | 1Pqo2WFzZJztQ2Bu4ndheoaY3E8g3ULKhP | 50 | 2025/4/24 12:00 |
| 51604 | 12EWRT19v2eAvWjGDWjodCe7NP1CzmFphT | 50 | 2025/7/31 14:07 |
| 53338 | 1497JAU931jEi2NaQZ7dbtrjGgKBGhkiUV | 50 | 2025/7/31 14:24 |
| 53698 | 1NuqAKeX6JzW372QfEe7eFkewFx21fnqd3 | 50 | 2025/7/31 14:24 |
| 53087 | 13giEgKhu5K69vHKgehdmNuRMnmuw3oEyn | 50 | 2025/7/31 14:24 |
| 53607 | 1A1z7aMZb3sC8RSwMYjnvPA5417Vj8wmwk | 50 | 2025/7/31 14:24 |
| 56793 | 13Vhp9ANzEEAAhjFT5ZJpk7ipwjZoYd3jc | 50 | 2025/10/12 13:01 |
| 56837 | 1CNJvNetepLu4xsBxJKXqEaU8vXKTTyVzK | 50 | 2025/10/12 13:01 |
| 45711 | 17uEQxSfy76bkuq2f3UTU2EGHoM6N3j9Pa | 50 | 2025/12/2 9:24 |
| 70960 | 1Dyn6B7r21Lzqy83Wh3nZxT36w5GwpDT1j | 50 | 2026/1/10 15:13 |
| 71297 | 13gPLb9fyYaFRK5XA5cwXUofyep61B9bws | 50 | 2026/1/10 15:13 |
| 71488 | 1PVvDqars8v1h5fY2NMrFAcnhtLtrUvG9d | 50 | 2026/1/10 15:13 |
| 71657 | 137YUD6LcdWEX5u3HjwGb9AAzut1hU2UF7 | 50 | 2026/1/10 15:13 |
| 72118 | 17AAeEDQu7Qa9pxwyqTCVDgxTyUmX2UNnh | 50 | 2026/1/10 15:13 |
| 72482 | 12MRVukoQZ4FTE9oyFU1Dw5Jcdj78LW971 | 50 | 2026/1/10 15:13 |
| 73066 | 1Dj5MgTfQAYpGHQ4L9fqNDEojbQ1ynjk9E | 50 | 2026/1/10 15:13 |
| 74346 | 15gmMgYYCkNFaN8psNVfgDrkR6brCcLm6f | 50 | 2026/1/10 15:13 |
| 74631 | 1Jwq8A4dRMSbaBfCuS8kabozg6P8dPC6Zh | 50 | 2026/1/10 15:13 |
| 75205 | 18bBaJXSbACXVVrueaHL3CbnTzJJDQYQeo | 50 | 2026/1/10 15:13 |
| 70616 | 1L7t8B9XexFcRJrpr5zjym9Ercy15LoekM | 50 | 2026/1/10 15:16 |
| 73602 | 1BWsa8qF8h4xqL5SNRYXVa2z3WvmZGJNNm | 50 | 2026/1/10 15:16 |
| 73909 | 1K8rkVHwqSzuFhNvRS8D8T7YdzvvjRsf4F | 50 | 2026/1/10 15:16 |
| 73650 | 12FFtpTYYZJ2fxane8hKXcPCxek92F5FzY | 50 | 2026/2/11 0:41 |
| 67089 | 1FehNL3vLgY39VdBwA8nWPFWGAs2Vig4jQ | 50 | 2026/6/19 20:13 |

</details>

In the fairy tale, Satoshi invented Bitcoin, never sold a single coin, and then left.

On June 27, 2026, Craig Wright posted a photo of himself and his wife in a skyscraper, saying: `Sorry trolls. We are still strong`.
Someone commented: You live like Satoshi, without the responsibility.
Craig Wright replied: **`Yep`**

The Bitcoin community, at an average annual cost of $100 million, supports Satoshi. Compared to tech giants' CEOs, this price isn't high; he invented Bitcoin.

Never satisfied, endless desires, infinite money.

---

## 🏁 Chapter 15: The Emerging Billions on the Surface, and the Iceberg Below

### 7.3.1 Everything is Fake; Wealth is the Only Proof That Needs No Translation

Michael Saylor is famous for betting his company's funds heavily on Bitcoin. Every time Bitcoin crashes, Craig Wright publicly criticizes and taunts him, prompting Saylor to passionately proclaim: "Never sell your Bitcoin." Bitcoin is dead money infused with digital energy. He has siphoned tens of billions from U.S. capital markets into Bitcoin, making him its greatest evangelist. At every Bitcoin conference, his speeches end with a tribute to Satoshi. You could call it an understanding.

On July 4, 2025, as Bitcoin surged to an all-time high of $110,000-$120,000, 8 wallets dormant since 2011 (still that year) awakened. A total of 80,009 Bitcoins, worth approximately $9 billion, were dumped onto the market. The market absorbed this selling. Michael Saylor's efforts were key. As of the end of June 2026, Strategy, his company, reported total Bitcoin holdings: 847,363 BTC, acquired at a cost of approximately $64.1 billion, with an average price of about $75,646 per BTC.

| # | Bitcoin Wallet Address | First Deposit Time | 2025 Emptying Time | Amount |
| :-: | :--- | :-: | :-: | :-: |
| 1 | `12tLs9c9RsALt4ockxa1hB4iTCTSmxj2me` | 2011/04/03 05:08:32 | 2025/07/04 11:39:25 | 10,000 BTC |
| 2 | `1KbrSKrT3GeEruTuuYYUSQ35JwKbrAWJYm` | 2011/04/03 06:18:45 | 2025/07/04 12:06:43 | 10,000 BTC |
| 3 | `1P1iThxBH542Gmk1kZNXyji4E4iwpvSbrt` | 2011/05/04 09:14:27 | 2025/07/04 20:37:24 | 10,000 BTC |
| 4 | `1CPaziTqeEixPoSFtJxu74uDGbpEAotZom` | 2011/05/04 09:28:05 | 2025/07/04 21:07:46 | 10,000 BTC |
| 5 | `14YK4mzJGo5NKkNnmVJeuEAQftLt795Gec` | 2011/05/04 09:40:51 | 2025/07/04 21:31:42 | 10,000 BTC |
| 6 | `1ucXXZQSEf4zny2HRwAQKtVpkLPTUKRtt`  | 2011/05/04 10:01:23 | 2025/07/04 22:01:42 | 10,000 BTC |
| 7 | `1BAFWQhH9pNkz3mZDQ1tWrtKkSHVCkc3fV` | 2011/05/04 10:01:23 | 2025/07/04 22:30:35 | 10,000 BTC |
| 8 | `1f1miYFQWTzdLiCBxtHHnNiW7WAWPUccr`  | 2011/05/04 10:10:49 | 2025/07/04 22:54:13 | 10,009 BTC |
| **Total** | **Value ~$9 Billion** |   |   | **80,009 BTC** |

Do not doubt the owner of these 80,000 Bitcoins. These addresses are explicitly linked to the Ira Kleiman v. Craig Wright case. Court-disclosed materials clearly list 3 of these 8 addresses, with Craig Wright's signature next to them. The 3 addresses confirmed by Craig Wright are `12tLs9c9RsALt4ockxa1hB4iTCTSmxj2me`, `1KbrSKrT3GeEruTuuYYUSQ35JwKbrAWJYm`, and `1f1miYFQWTzdLiCBxtHHnNiW7WAWPUccr`.

The 8 addresses acted in concert. Knowing the true owner of one address is enough to know who sold these 80,009 Bitcoins. No self-verification needed: Wealth is the only answer.

### Never Satisfied; This Is Just the Opening Gambit of a Bigger Ambition

In 2003, Craig Wright obtained a PhD in Theology. His dissertation title was "The Tangled Roots of Creation Myths." This is where the story truly begins.

---

# The End

 ![Author](https://img.shields.io/badge/Author-卓宁-555555?style=flat-square&logo=probot)  [![Email](https://img.shields.io/badge/Email-cooooo%40gmail.com-blue?style=flat-square&logo=gmail)](mailto:cooooo@gmail.com) [![X (formerly Twitter)](https://img.shields.io/badge/X-%40psalmsa-black?style=flat-square&logo=x)](https://x.com/psalmsa) ![Share](https://img.shields.io/badge/Share-欢迎转发-success?style=flat-square) ![License](https://img.shields.io/badge/要求-转载请注明出处-fe7a16?style=flat-square)

---

# 📅 Satoshi Timeline: Key Early Milestones ✨

| Time | Event |
| :--- | :--- |
| **2008-08-18** | Satoshi Nakamoto registered the domain `bitcoin.org` using the anonymous domain registration service anonymousspeech.com and Finnish hosting company Louhi Net Oy. |
| **2008-08-20** | Satoshi Nakamoto sent his first email to Adam Back, inviting him to read the upcoming whitepaper. |
| **2008-08-21** | Adam Back replied briefly, suggesting he look into Wei Dai's "b-money." Adam Back did not read the whitepaper at that time. |
| **2008-08-22** | Satoshi Nakamoto emailed Wei Dai, asking for the publication year of b-money to cite it in his paper, and attached the abstract. Wei Dai replied with the date. |
| **2008-10-05** | Satoshi Nakamoto registered an account (nakamoto2) on SourceForge. He used this account to create a project named "Bitcoin" on SourceForge (the SourceForge Bitcoin project). |
| **2008-10-31** | Satoshi Nakamoto posted an email with the subject "Bitcoin P2P e-cash paper" to the metzdowd.com cryptography mailing list, attaching a link to the 9-page PDF whitepaper. Hal Finney, Ray Dillinger, and others responded. |
| **2008-11-03** | James A. Donald responded to the whitepaper, initiating the first public debate on Bitcoin's scalability (bandwidth and storage). Satoshi responded, explaining the SPV (Simplified Payment Verification) scheme, noting that only 12 KB of data per day would be needed for verification. |
| **November 2008** | Satoshi publicly calculated bandwidth needs on the mailing list, noting that Visa's 37 billion annual transactions (100 million daily) would require about 100 GB of bandwidth (costing ~$18), considering it "no big deal." |
| **2008-11-14** | In response to Hal Finney's proposal for an altruistic contribution model like SETI@Home, Satoshi explicitly corrected him, stating Bitcoin's incentive mechanism is purely economic, relying entirely on miners' self-interest and competition for block rewards. |
| **2008-12-08 / 09** | Satoshi uploaded the whitepaper to the SourceForge Bitcoin project. |
| **Early Jan 2009** | Just before the release of Bitcoin v0.1, Satoshi emailed Wei Dai again, informing him the website was live and the software would be released soon. |
| **2009-01-03 18:15 UTC** | Satoshi Nakamoto created the first block on the Bitcoin blockchain, the Genesis Block or Block 0. |
| **2009-01-09** | The first block after the Genesis Block, Block 1, was mined by Satoshi Nakamoto on January 9, 2009. |
| **2009-01-09** | Satoshi Nakamoto officially released the Windows version of Bitcoin v0.1 source code (`bitcoin.exe`) on the cryptography mailing list. |
| **2009-01-12** | The first person-to-person Bitcoin transaction occurred; Satoshi sent 10 Bitcoins to Hal Finney in Block 170. Several test transfers followed. |
| **2009-03-24** | Satoshi uploaded another version of the whitepaper to the SourceForge Bitcoin project. |
| **May 2009** | Satoshi asked Martti Malmi to write a FAQ for the SourceForge Bitcoin project. After the forum went live, he appointed Martti as a moderator. |
| **November 2009** | Satoshi established the Bitcoin forum at `bitcoin.org/smf/`. He single-handedly controlled all infrastructure (code, website, forum, domain). |
| **December 2009** | Bitcoin v0.2 was released, adding Linux support. |
| **Throughout 2009** | Bitcoin operated stably as a working prototype system. The price was near zero, and mining was primarily CPU-based. |
| **February 2010** | Developer dwdollar launched the first PayPal-based Bitcoin exchange, "Bitcoin Market." |
| **2010-05-18** | Laszlo Hanyecz posted on the Bitcoin forum, offering 10,000 Bitcoins for two pizzas. |
| **2010-05-22** | 19-year-old student Jeremy Sturdivant accepted the pizza offer and paid with his card. This ~$25-30 transaction represented Bitcoin's first real-world price discovery. |
| **June 2010** | Satoshi began posting regularly on the forum. Laszlo Hanyecz wrote GPU mining software; Satoshi privately asked him to stop releasing it to delay the "GPU arms race" and requested the forum thread be quietly shelved. |
| **2010-06-17** | Satoshi posted stating that Bitcoin's core design was fixed for its entire lifecycle upon v0.1's release. The protocol is immutable. |
| **2010-07-14** | Satoshi outlined the network's final form: ordinary users using lightweight clients, the number of nodes likely never exceeding 100,000, with maintenance handled by experts with server clusters. |
| **2010-07-15** | Satoshi committed a 990 KB block size limit to the client without any announcement. |
| **2010-07-18** | Jed McCaleb launched the Mt. Gox exchange using a domain he had for Magic: The Gathering trading. Bitcoin gained a continuous order book and USD price quotes, attracting speculators. |
| **2010-07-28** | The OP_RETURN vulnerability was discovered, allowing anyone to spend others' coins. Satoshi unilaterally modified the consensus-level opcode and pushed a patch within hours. |
| **2010-07-29** | Satoshi reiterated on the forum that users don't need to run nodes (analogous to Usenet). Developer Dan Larimer questioned Bitcoin's transaction rate, causing Satoshi to lose patience and reply: "If you don't believe me or don't get it, I don't have time to try to convince you, sorry." |
| **2010-08-11** | Satoshi posted about third-party custody, proposing the thought experiment of "gold turning into lead after being stolen." |
| **2010-08-15** | Jeff Garzik discovered an 184 billion BTC overflow transaction in block 74,638. Satoshi released v0.3.10 patch within 5 hours and executed a hard fork to reverse the transaction. He simultaneously disabled a set of opcodes like `OP_CAT` that could lead to network paralysis. This update included an "Alert System" (kill switch) with a hardcoded public key, capable of freezing transactions network-wide. |
| **2010-08-27** | Responding to a question about the "Mises Regression Theorem," Satoshi replied with the thought experiment of a "gray base metal transferable via communication channels." |
| **September 2010** | Gavin Andresen obtained commit access to the SourceForge code repository. |
| **2010-09-07** | Satoshi again committed a 1 MB block size limit without warning, capping Bitcoin's expansion. |
| **2010-10-03** | Jeff Garzik proposed raising the block limit to 7 MB; Satoshi rejected it, citing potential network forks. |
| **Nov/Dec 2010** | WikiLeaks was financially blocked by the U.S. system; the community discussed using Bitcoin for donations. User genjix posted on the bitcoin.org website discussing using Bitcoin to pay WikiLeaks. On December 5, 2010, Satoshi responded: "No, don't 'bring it on.' The project needs to grow gradually so the software can strengthen along the way. I make this appeal to WikiLeaks not to try to use Bitcoin. Bitcoin is a small beta community in its infancy. You would not come out with much more than pocket change, and the heat you would bring would likely destroy us at this stage." |
| **2010-12-11** | In response to a PC World article, Satoshi strongly opposed WikiLeaks using Bitcoin, calling it "poking the hornet's nest." |
| **2010-12-12** | Satoshi posted his 575th forum post (a routine technical comment) and then went offline, never posting publicly on the forum again. |
| **Early 2011** | Satoshi handed over the highest authority, the "Alert Key," to Gavin Andresen. |
| **Early 2011** | Satoshi still replied to a few emails behind the scenes, quietly pushing forward the handover. |
| **March 2011** | Jed McCaleb sold the Mt. Gox exchange to Frenchman Mark Karpelès, living in Tokyo. |
| **2011-04-23** | Satoshi sent his last known email to Mike Hearn: "I've moved on to other things. Gavin and the others will take good care of it." |
| **2011-04-27** | Gavin Andresen released his first client version, v0.3.21. On the same day, he announced his invitation to speak at the CIA. |
| **2011-06-14** | Gavin Andresen delivered his speech at CIA headquarters. |
| **Mid-2011** | Satoshi completely disappeared. The code was migrated to GitHub. The Bitcoin forum was taken over by Martti Malmi. Satoshi lost control over the code and forum. |

---

# 📅 The Birth Process of Bitcoin: This is the Story of One Man, Satoshi, Who Did All of the Following ✨

| Time | Event | Details | Purpose | Source |
| :--- | :--- | :--- | :--- | :--- |
| **2001-10-23** | Submitted "BlackNet Abstract" paper to Australian Government | Described a peer-to-peer transaction system for "online payments" without central intermediaries. | Apply for research grants and tax relief; successfully obtained relief from 2001 to 2009. | Australian Government Documents |
| **2002-10-03** | Submitted "BlackNet Project" R&D document to Australian Government | Mentioned "Phase 4 - Release Phase" and the concept of "digital cash." | Planned an IT security project and submitted tax benefit applications to Australian authorities. | Australian Government Documents |
| **2005-10-28** | Assignment prepared for University of Newcastle course `STAT6640` | Discussed and mastered concepts related to "non-linear processing methods" with faculty. | Research work while pursuing an MStat at the University of Newcastle. | Handwritten university assignment |
| **2006-06-15** | Security Summit Report "Implementing Effective Risk-Based Controls" | Mentioned distributed computing systems, hash chains, and Merkle trees (characteristics of Bitcoin). | Paper written for a Master's in Network and Systems Management at Charles Sturt University. | Papers and articles |
| **2006-08-30** | Paper "Predicates in Quorum Systems" | Discussed core Bitcoin concepts using Quorum systems for distributed system security. Author listed as `Satoshi`. | Explored the topic of "quorum systems." | Files `LPA.tex` and `LP1.tex` |
| **2007-06-18** | Northumbria University LLM Thesis Proposal | Contained professional terminology and concepts later used in the Bitcoin whitepaper. | Written for an LLM course. | LLM Thesis Proposal 2 |
| **2007-08-07** | Dr Wright meeting with Alan Granger at BDO | Meeting minutes mention "time chain," "P2P electronic cash," and "writing to paper." | Discuss planning for work needed in 2007 and 2008. | Handwritten meeting minutes |
| **2007-09-15** | "In-depth Analysis of Proof-of-Work Calculations in the Hashcoin Whitepaper: Exploring Alternative Strategies" | LaTeX document compiling into draft articles under the name `Satoshi` or `Satoshi Nakamoto`. | Discussed proof-of-work mechanisms in decentralized digital transactions. | File `NG3.tex` |
| **2007-09-19** | Paper "Competitive Transactions or Block Models" | Discussed time-hash protocols, double-spending, conflicting block transmission; term `UTXO` coined. | Precursor to the Bitcoin whitepaper. | Paper |
| **October 2007** | C++ Code | **💡 Historic Moment**: Starting in October 2007, wrote Bitcoin code "from scratch" in `C++`. | Used to build a simplified Bitcoin model. | C++ code files |
| **October 2007** | "Strategy of Nodes in Decentralized Systems: A Game-Theoretic Analysis" | Product development documents within the C++ code; technical notes, drafts, and articles on concepts explained in the whitepaper. | Evaluated transaction processing, cryptographic security, consensus mechanisms. | File `ESDT.tex` |
| **Before 2007-10-31** | Paper "King's Wi-Fi: Enhancing Network Security Using Consensus Systems in the Byzantine Generals Problem" | Described "using proof-of-work to solve problems in distributed computing" and the "Byzantine Generals Problem." | Written for review at the SANS Institute. | File `The King2.rtf` |
| **Before 2007-10-31** | One-page handwritten notes "Hash-based Shadow Mechanism" | Discussed hash chains and hash tokens; explored using hash chains/tokens in auction systems. | Notes, drafts, articles written while pursuing an LLM at Northumbria University. | Scanned handwritten document |
| **Before 2007-10-31** | Paper "Secure and Reliable Voting Mechanisms" | Secure/reliable voting in distributed networks: a quorum-based approach combining hash chains and PKI. | Written while pursuing a Master's in Information Systems Security at Charles Sturt University. | Files `Q.txt` and `IT1581b.rtf` |
| **Before 2007-10-31** | "Internal Controls and Immutable Logging in Message System Backend Operations" | Mentioned the concept of immutable logging, the foundation of blockchain technology used in Bitcoin. | Interest in and research on immutable logging concepts. | RTF file |
| **2007** | Initial draft of LLM proposal on "Payment Providers and Trusted Third Parties in Internet Law" | Mentioned "cryptographically proven electronic payment systems" for voluntary transactions without third parties. | PhD thesis proposal in machine learning submitted in 2007. | File `Proposala.rtf` |
| **2008-01-05** | Downloaded 1967 document "Tominaga Nakamoto: Monumenta Nipponica" | Satoshi Nakamoto is a combination of Tominaga Nakamoto and Ash Ketchum (Satoshi). | Chose `Satoshi Nakamoto` out of respect for the philosopher Tominaga Nakamoto. | Phone photo |
| **2008-01-24** | PDF version of the Whitepaper | Document included Dr Wright's name and contact details, pointing to Charles Sturt University. | Shared and discussed with faculty at Charles Sturt University. | PDF file |
| **2008-03-08** | Draft of Bitcoin Whitepaper, this version had 40 pages, later reduced to 20-10 pages. | Used this document as a student presentation tool in March 2008 (no intention to hide identity). | Teaching students about version control using document versioning. | OpenOffice document |
| **2008-03-12** | Email: "I need your help editing a paper I am going to release." | Sought further optimization after reducing the whitepaper from 40 to 10 pages. | Sent the whitepaper draft to David Kleiman. | Private communication |
| **2008-05-06** | "Timecoin ODT Whitepaper" | The term `Timecoin` was never made public; part of the story behind the Satoshi identity, known only to a select few. | This document was initially written under the name `TimeCoin` before evolving into Bitcoin. | Document |
| **2008-08-15** | "Block diffusion within bitcoin" | **🚀 Historic Moment**: The word `bitcoin` appears for the first time. | Preliminary research on the Bitcoin network theory, mentioning the concept of "Bitcoin." | Document |
| **2008-08-20** | Bitcoin Whitepaper written in LaTeX | The content of the Bitcoin Whitepaper was mostly complete; references were not yet finalized. | Draft shared with Adam Back and Wei Dai to check references. | Files `main.tex` and `E-Cash-main.tex` |
| **2008-08-30** | Registered domain `bitcoin.org` and email `satoshi@vistomail.com` | Cost 687 AUD plus 8 AUD processing fee from Anonymous Speech. | Anonymity, hiding identity. | Bank statement |
| **2008-09-10** | "Bitcoin Node Economics, Non-cooperative Finite Game" | Contained notes on the "economic effects of central core Bitcoin nodes." | Explored the economic effects of running nodes. | Document |
| **2008-10-03** | Printed the Bitcoin Whitepaper | Cover page of the printed Bitcoin Whitepaper with Dr Wright's name and contact details, and a handwritten note. | This document was stapled together and had coffee stains on it. | A4 printed paper |
| **2008-10-31** | Bitcoin Whitepaper (Bitcoin: A Peer-to-Peer Electronic Cash System) | **🔥 Historic Moment**: The Bitcoin Whitepaper was officially released, sent to the "Cryptography Mailing List." | Official release of the Bitcoin Whitepaper. | Cryptography Mailing List |
| **2009-04-09** | "TimeChain - A Logging System Built on Bitcoin" | Launched a Timecoin network in addition to Bitcoin, running on a server cluster. | For expanding and delivering the BlackNet project. | Testnet |

Bitcoin was not born from a one-year coding sprint in isolation. Through "this person's" timeline, you can trace the birth process of Bitcoin. He wasn't merely a cryptographer; he had to first understand human nature, possess profound knowledge, and have sufficient motivation to create Bitcoin.

The world believes Bitcoin's birth was a genius's lightning strike. In truth, it was a prolonged siege catalyzed by financial incentives. The concept took shape in 2001, driven not by faith, but by a ticket to secure research funding and tax privileges from the Australian government. After enjoying six years of state funding, greed and genius finally converged: C++ code began in October 2007; one year later, the whitepaper was finalized; in 2009, Bitcoin emerged, and the Genesis Block began its work. Yet, in the fateful year of 2009, the long-standing tax exemption battle finally failed. In this narrative spanning eight years, intertwining technological disruption and utilitarian calculation, from start to finish, only one person fought alone.

---

# 📅 Satoshi Nakamoto Brief History: Craig Wright Education Background ✨

<details open>
<summary><b>📐 Table (Default Open, Click to Collapse)</b></summary>

| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Time&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | University | Degree |
| :--- | :--- | :--- |
| 2020 - 2023 | Harvard University | Master of Arts - MA in Asian History |
| 2021 - 2023 | Grand Canyon University | DBA in Qualitative studies (GPA: 3.8) |
| 2018 - 2022 | University of Leicester | Doctor of Philosophy - PhD in Law |
| 2020 - 2022 | Brunel University London | Master of Arts - MA in Educational Leadership and Administration, General |
| 2020 - 2022 | The Open University | Master of Arts - MA in English Literature (British and Commonwealth) |
| 2020 - 2022 | Birkbeck, University of London | Master of Arts - MA in Philosophy (Philosophy of time) |
| 2021 - 2022 | Liberty University | Master of Science - MS in Criminal Justice / Forensic Psychology (GPA: 3.9) |
| 2020 - 2021 | University of Colorado Boulder | Postgraduate Degree / PG Certificate - Battery Pack Balancing and Power Estimation |
| 2020 - 2021 | Liberty University | Master of Science - MS in Political Science and Government (GPA: 3.85) |
| 2015 - 2020 | University of London | Master of Science in Finance (Quantitative Finance), Econometrics and Quantitative Economics |
| 2008 - 2014 | Charles Sturt University | Doctor of Philosophy - PhD in Computer Science / Economics *(Thesis: Quantitative & Game-Theoretic Modeling of Information Security Risks)* |
| 2010 - 2012 | SANS Technology Institute | Master's degree in Information Security Engineering |
| 2009 - 2012 | SANS Technology Institute | Master's degree in Engineering Management |
| 2006 - 2009 | Charles Sturt University | Master's degree - Master of Information Systems Security |
| 2006 - 2009 | University of Newcastle | Master of Statistics in Mathematics and Statistics *(Thesis: Power of Tests for Homogeneity of Variance within Groups)* |
| 2005 - 2008 | Northumbria University | Master of Laws - LLM in International Business/Trade/Commerce (Commendation) *(Thesis: Legal Liability of Internet Intermediaries)* |
| 2004 - 2006 | Charles Sturt University | Master's degree - Master of Management (Information Technology) |
| 2003 - 2005 | Charles Sturt University | Master of Networking and Systems Administration in Computer Systems Networking and Telecommunications |
| Not provided | Arden University | Master of Science - MS in Psychology |
| Not provided | Geneva Business School | Doctor's Degree DBA - Doctor of Business Administration |
| Not provided | Higher School of Economics | Master's degree in Data Science |
| Not provided | Kenya (Institution not specified) | Doctor's Degree in Theology / Theological Studies |
| Not provided | The Open University | Master of Science - MS in Mathematics |
| Not provided | University of Birmingham | Master of Arts - MA in Medieval and Renaissance Studies |
| Not provided | University of Exeter | Doctor of Philosophy - PhD in Computational and Applied Mathematics / Economics |
| Not provided | University of London | Master of Science - MS in Logistics and Supply Chain |
| Not provided | University of Southern Queensland | Bachelor of Arts - BA in English Language and Literature / Letters |
| Not provided | University of Southern Queensland | Bachelor of Science - BS in Mathematics |
| Not provided | University of Wales Trinity Saint David | Master of Arts - MA in Classical, Ancient Mediterranean and Near Eastern Studies and Archaeology |
| Not provided | Walden University | Doctor's Degree DBA - Doctor of Business Administration |
| 2008 | SANS Technology Institute | GIAC Security Expert - Malware (GSE-MALWARE) |
| 2008 | SANS Technology Institute | GIAC Security Expert - COMPLIANCE (GSE-COMPLIANCE) |
| 2008 | SANS (GIAC) | GIAC Security Expert (GSE) |

</details>

---

# 📅 Bitcoin Full-Stack Technology and Invention Evolution History: Authoritative Archive ✨

---

## From Static Cryptography to a Self-Sustaining Machine

Bitcoin's greatness lies not in inventing an entirely new set of underlying algorithms, but in its artistic engineering fusion of decades of independent computer science, cryptography, and game theory results. Satoshi transformed a cold, static "tamper-proof ledger" into the first decentralized payment machine in human history capable of self-perpetuation, self-driving, and never stopping.

This archive rigorously dissects the core technological modules constituting the Bitcoin system, precisely defining the boundary between "predecessor's foundations" and "Satoshi's originality," thereby constructing an airtight, complete picture of Bitcoin's invention.

---

## Not Invented by Satoshi — The 10 Predecessor Technological Foundations

Before the publication of the Bitcoin whitepaper in 2008, the following technological modules had already matured in their respective academic fields or engineering practices. Satoshi directly inherited and co-opted these tools as the building blocks for Bitcoin.

### 1. Peer-to-Peer Network

* **Technical Essence**: Peer-to-peer communication protocol. Nodes have equal status, interacting and broadcasting data directly without relying on a central server.
* **Historical Origin**: Stemmed from distributed network research like ARPANET (1969) and Usenet (1979), and was extensively validated at scale in P2P file-sharing systems like Napster (1999), Gnutella, and BitTorrent (2001).

### 2. Public Key Cryptography

* **Technical Essence**: Asymmetric encryption mechanism. Consists of a key pair; data signed with the private key can only be decrypted and verified using the corresponding public key, ensuring identity verification and tamper-resistance in a decentralized environment.
* **Historical Origin**: Theoretical foundation laid by Whitfield Diffie and Martin Hellman in 1976; RSA algorithm implemented by Ron Rivest, Adi Shamir, and Leonard Adleman in 1977.

### 3. Merkle Trees

* **Technical Essence**: A hash binary tree structure. It recursively hashes and compresses batches of transactions into a single root hash, ensuring data integrity while allowing verification of data inclusion via a proof path, without needing to download the entire dataset.
* **Historical Origin**: Patented by Ralph Merkle in 1979. Its clever design recursively organizes data so each parent node is formed from the hash of its children, enabling a precise fingerprint of the entire dataset.

### 4. secp256k1 Elliptic Curve Standard

* **Technical Essence**: The specific elliptic curve used by Bitcoin for all public key cryptography; all addresses, signatures, and transactions use this curve. Used to efficiently generate key pairs and perform the ECDSA signing algorithm.
* **Historical Origin**: Theory proposed by Neal Koblitz and Victor Miller in 1985; standardized by SECG after 2000, included in the SEC 2 (v1.0) document released in September 2000.

### 5. Hash-linked Timestamping

* **Technical Essence**: A structure linking data blocks into a chain. The header of each subsequent block must contain the overall hash of the previous block, forming a strictly logical, tamper-resistant linear timestamped chain.
* **Historical Origin**: Proposed by Stuart Haber and W. Scott Stornetta in their 1991 paper "How to Time-stamp a Digital Document." This is the most direct predecessor of the "Blockchain" data structure.

### 6. Proof of Work

* **Technical Essence**: A means of achieving access control or preventing resource abuse by expending computational resources. In Bitcoin, it's the consensus mechanism where nodes compete by racing to compute hashes for the right to record the next block.
* **Historical Origin**: Concept proposed by Cynthia Dwork and Moni Naor in 1992 to combat spam. In 1997, Adam Back invented Hashcash, applying PoW to anti-spam systems; its mechanism of "finding a hash with a specific number of leading zero bits" was inherited by Bitcoin.

### 7. Programmable Contracts

* **Technical Essence**: Translating contract terms into computer code that executes automatically when conditions are met. The core idea is reducing reliance on intermediaries and minimizing execution disputes through code transparency.
* **Historical Origin**: In 1996, Ian Grigg proposed Ricardian Contracts, which are readable by both humans and machines and cryptographically signed to prevent forgery. That same year, Nick Szabo further developed the influential concept of Smart Contracts.

### 8. Byzantine Fault Tolerance Theory

* **Technical Essence**: A theory in distributed computing concerning fault tolerance, exploring how nodes can reach consensus on system state despite the presence of arbitrary faulty, delayed, or malicious nodes.
* **Historical Origin**: The theory was introduced in a paper by Lamport, Shostak, and Pease in 1982. A milestone engineering implementation, Practical Byzantine Fault Tolerance (PBFT), was published by Miguel Castro and Barbara Liskov in 1999.

### 9. SHA-256 & RIPEMD-160

* **Technical Essence**: One-way cryptographic hash functions. SHA-256 generates a 32-byte fixed-length digest used in PoW, Merkle trees, and block chaining; RIPEMD-160 further compresses the public key hash.
* **Historical Origin**: Derived from SHA-0 (1990) and SHA-1 (1995). SHA-256 was designed by the NSA and published by NIST in 2001. RIPEMD-160 was developed by European researchers including Hans Dobbertin in 1996.

### 10. Early Digital Cash Theories

* **Technical Essence**: Attempts to simulate the properties of physical cash (anonymity, untraceability, use-once) using cryptography.
* **Branches**:
    * **DigiCash (1983-1998)**: Invented by David Chaum, based on blind signatures, achieving absolute privacy but crucially reliant on a bank; filed for bankruptcy in 1998.
    * **b-money (1998)**: Proposed by Wei Dai, first envisioning decentralized ledger maintenance via asynchronous P2P broadcasting, but remained a paper theory.
    * **Bit Gold (1998-2005)**: Proposed by Nick Szabo, utilized chained proof-of-work but remained a conceptual theory, never implemented.
    * **RPOW (2004)**: Proposed by Hal Finney, implemented a hash-based PoW token transferability but required a central server to prevent double-spending.

---
# 📅 Bitcoin Core Technology and Thought Evolution Milestones ✨

To restore history, the table below outlines the 10 core technological foundations and conceptual sources that formed the building blocks of the blockchain before the Bitcoin whitepaper's release in 2008:

| Time | Person | Identity | Invention / Core Contribution | Category |
| :--- | :--- | :--- | :--- | :--- |
| **1957** | William Feller | Princeton Mathematician, Probability Theory Founder | Mathematical formula for Poisson distribution model (used to analyze attacker success probability; Whitepaper Reference [8]) | Mathematics & Theory |
| **1969** | ARPANET Team | U.S. DARPA | Fundamental concept of Peer-to-Peer (P2P) network communication | Foundational Networking |
| **1974** | Vint Cerf & Bob Kahn | Computer Scientists, "Fathers of the Internet" | Proposed TCP/IP protocol (foundational protocol for Bitcoin's node communication and data broadcasting) | Foundational Networking |
| **1976** | Whitfield Diffie & Martin Hellman | Stanford Cryptography Researchers | The Key Exchange, laying the foundation for public-key cryptography | Cryptography |
| **1977** | Rivest, Shamir & Adleman | MIT Researchers | Proposed RSA algorithm (first practical asymmetric encryption and digital signature, proving feasibility of digital cash) | Cryptography |
| **1979** | Ralph Merkle | Stanford Computer Scientist | Merkle Tree / Hash Tree, for efficient data integrity verification (Whitepaper Reference [7]) | Data Structure / Cryptography |
| **1979** | Claus Schnorr | German Mathematician, Cryptographer | Invented Schnorr signatures (patent protection expired in 2008, Satoshi used ECDSA initially; later introduced to Bitcoin via Taproot upgrade in 2021) | Cryptography / Signature Algorithm |
| **1982** | Leslie Lamport, Robert Shostak & Marshall Pease | SRI Researchers, Computer Scientists | Formulated the "Byzantine Generals Problem," establishing theoretical foundations for state machine consensus and fault-tolerant verification rules | Distributed Systems Theory |
| **1983** | David Chaum | Cryptographer, DigiCash Founder | Blind Signatures and eCash, first commercial attempt at achieving absolute privacy in digital cash | Cryptography / Digital Cash |
| **1985** | Neal Koblitz & Victor Miller | University of Washington Mathematician / IBM Researcher | Laid the theoretical foundation for Elliptic Curve Cryptography (ECC) | Cryptography |
| **1988** | Timothy C. May | Former Intel Physicist, Cypherpunk Founder | Published "The Crypto Anarchist Manifesto," envisioning anonymous digital currency and encrypted information markets | Cypherpunk Ideology |
| **1991** | Phil Zimmermann | Colorado Software Engineer | Invented PGP encryption software and won legal battle against the U.S. government, establishing "code as speech" legal protection | Legal Protection / Cryptography |
| **1991** | Stuart Haber & W. Scott Stornetta | Bell Labs Cryptography Researchers | Timestamping tamper-proof technology, most direct predecessor to the blockchain data structure (Whitepaper References [3][4][5]) | Data Structure / Cryptography |
| **1992** | Cynthia Dwork & Moni Naor | Harvard / Weizmann Institute Researchers | Proposed the theoretical concept of Proof of Work (PoW), initially for combating spam | Consensus Mechanism / Cryptography |
| **1992** | John Gilmore, Eric Hughes & Tim May | Cryptographers, Free Software Advocates | Co-founded the Cypherpunks mailing list, establishing a community focused on encryption and privacy discussions | Community Ecosystem |
| **1993** | Eric Hughes | One of the Cypherpunk Founders | Published "A Cypherpunk's Manifesto," establishing privacy and code as the movement's core tenets | Cypherpunk Ideology |
| **1993** | Bruce Schneier | Cryptographer, Security Expert | Published "Applied Cryptography," significantly lowering the barrier for hackers to engage in cryptographic engineering, becoming a community bible | Cryptography Engineering Promotion |
| **1996** | Doshai | Anonymous Cypherpunks Mailing List User | Explored architectures for digital transactions and internet banking independent of centralized authority, fostering the decentralized mindset | Community Ecosystem / Theory Exploration |
| **1996** | Ian Grigg | Financial Cryptographer | Proposed Ricardian Contracts, binding legal contracts with cryptographic code, laying the foundation for programmable contracts | Smart Contracts / Finance |
| **1996** | Hans Dobbertin | European Open-Source Academic Community | Developed RIPEMD-160 hash compression algorithm (used by Satoshi for secondary hashing of SHA-256 public keys to create shorter Bitcoin addresses) | Cryptography / Address Algorithm |
| **1997** | Adam Back | British Cryptographer | Invented Hashcash, a direct application of proof-of-work, became the basis for Bitcoin mining (Whitepaper Reference [6]) | Consensus Mechanism / Cryptography |
| **1998** | Wei Dai | Computer Scientist, Cypherpunk Member | Proposed the conceptual blueprint for b-money, first envisioning P2P asynchronous broadcasting and decentralized local ledgers (Whitepaper Reference [1]) | Digital Cash Theory |
| **1998** | Nick Szabo | Computer Scientist, Legal Scholar | Introduced the Bit Gold concept (chained proof-of-work) and the Smart Contracts concept | Digital Cash / Smart Contracts |
| **1999** | Miguel Castro & Barbara Liskov | MIT Computer Scientists | Published PBFT (Practical Byzantine Fault Tolerance), first practical engineering solution for consensus in distributed systems | Distributed Systems Engineering |
| **1999** | Henri Massias, Xavier Serret-Avila & J.-J. Quisquater | European Information Theory & Cryptography Researchers | Proposed a timestamping system design with minimal trust requirements, optimizing block chaining mechanisms (Whitepaper Reference [2]) | Data Structure / Cryptography |
| **2001** | Designed by NSA / Published by NIST | U.S. Government & National Standards Agency | Standardized and released the SHA-256 hash algorithm, becoming the core cryptographic basis for Bitcoin operations | Cryptography |
| **2001** | Bram Cohen | Computer Programmer | Invented the BitTorrent protocol; its revolutionary decentralized P2P data distribution architecture deeply inspired Satoshi's network layer design for Bitcoin nodes | Distributed Foundational Networking |
| **2003** | Emin Gün Sirer | Cornell Computer Scientist | Proposed the KARMA system, first academically proving that proof-of-work based tokens could serve as a medium of exchange | Distributed Systems / Monetary Theory |
| **2004** | Hal Finney | Cryptography Pioneer, PGP Core Developer | Invented RPOW (Reusable Proofs of Work), demonstrating token transferability based on cryptographic proofs | Digital Cash / Consensus Mechanism |

## Status of Related Figures

This section compiles the current basic living status (as of 2026) of key figures who contributed to specific scientific, cryptographic, and technical fields relevant to this history. The list filters out other historical identities and technical contributions, focusing only on core personal backgrounds.

<details open>
<summary><b>📐 Table (Default Open, Click to Collapse)</b></summary>

| Name | Date of Birth | Status | Satoshi Identity Controversy |
| :--- | :--- | :--- | :--- |
| William Feller | 1906-07-07 | 💀 Deceased; Date of Death: 1970-01-14 | Excluded |
| Vint Cerf | 1943-06-23 | Vice President and Chief Internet Evangelist at Google | Excluded |
| Bob Kahn | 1938-12-23 | Chairman, President, and CEO of CNRI | Excluded |
| Whitfield Diffie | 1944-06-05 | Chief Scientist at Cryptic Labs; Visiting Scholar at Stanford | Excluded |
| Martin Hellman | 1945-10-02 | Professor Emeritus of Electrical Engineering at Stanford | Excluded |
| Ron Rivest | 1947-05-06 | Professor at MIT CSAIL | Excluded |
| Adi Shamir | 1952-07-06 | Professor at Weizmann Institute | Excluded |
| Leonard Adleman | 1945-12-31 | Professor Emeritus at USC | Excluded |
| Ralph Merkle | 1952-02-02 | Senior Research Fellow at Artemis Health Institute; Professor Emeritus | Excluded |
| Claus Schnorr | 1943-08-04 | Professor Emeritus at Goethe University Frankfurt | Excluded |
| Leslie Lamport | 1941-02-07 | Distinguished Scientist at Microsoft Research; Independent Researcher | Excluded |
| Robert Shostak | 1948-12-13 | Retired from Silicon Valley; Occasional Independent Consultant | Excluded |
| Marshall Pease | 1920-03-30 | 💀 Deceased; Date of Death: 2001-11-14 | Excluded |
| David Chaum | 1955-03-03 | Founder & CEO of Elixxir | Excluded |
| Neal Koblitz | 1948-12-24 | Professor at University of Washington | Excluded |
| Victor Miller | 1947-03-03 | Retired from IBM; Occasional Independent Researcher | Excluded |
| Timothy C. May | 1951-12-21 | 💀 Deceased; Date of Death: 2018-12-14 | Excluded |
| Phil Zimmermann | 1954-02-12 | Visiting Professor at TU Delft; Co-founder of Silent Circle | Excluded |
| Stuart Haber | 1955 | Chief Scientist at Stuart Haber IT Labs | Excluded |
| W. Scott Stornetta | 1959 | Chief Scientist at Yugen Partners | Excluded |
| Cynthia Dwork | 1958-06-27 | Professor at Harvard SEAS & Radcliffe Institute | Excluded |
| Moni Naor | 1954-11-22 | Professor at Weizmann Institute | Excluded |
| John Gilmore | 1955 | EFF Board Member; Open Source Fund Donor | Excluded |
| Eric Hughes | 1966 | Independent Software Consultant in Silicon Valley | Excluded |
| Bruce Schneier | 1963-01-15 | Lecturer at Harvard Kennedy School; Security Architect at Inrupt | Excluded |
| Ian Grigg | ~1960s | Financial Cryptography Advisor at Block.one | Excluded |
| Hans Dobbertin | 1952-04-17 | 💀 Deceased; Date of Death: 2006-02-02 | Excluded |
| Adam Back | 1970-07 | CEO of Blockstream | 🔴 Suspected |
| Wei Dai | 1976 | Highly private, reclusive computer engineer | 🔴 Suspected |
| Nick Szabo | 1964-04-05 | Independent Scholar; Advisor to Blockchain Projects | 🔴 Suspected |
| Miguel Castro | ~1969 | Deputy Managing Director at Microsoft Research Cambridge | Excluded |
| Barbara Liskov | 1939-11-07 | Institute Professor Emerita at MIT | Excluded |
| Henri Massias | N/A | Security Lecturer and Consultant in Europe | Excluded |
| Xavier Serret-Avila | N/A | Security Expert and Consultant in Europe | Excluded |
| Jean-Jacques Quisquater | 1945-01-13 | Professor Emeritus at UCLouvain | Excluded |
| Bram Cohen | 1975-10-12 | Founder & Chairman of Chia Network | Excluded |
| Emin Gün Sirer | 1971 | Associate Professor Emeritus at Cornell; CEO of Ava Labs | Excluded |
| Hal Finney | 1956-05-04 | 💀 Deceased; Date of Death: 2014-08-28; Body Cryonically Preserved | 🔴 Suspected |

- 🔴 **Suspected**: Heavily suspected, frequently discussed in cryptographic communities, blockchain history, or mainstream media investigations, with supporting circumstantial technical evidence.
- ❌ **Excluded**: Died before the Bitcoin whitepaper publication in 2008, factually impossible, or never seriously considered a candidate.

</details>

---

<table>
<tr>
<td>

# 🔍 Final Verdict: Definitive Exclusion of Satoshi Candidates

> **Introduction**: Satoshi Nakamoto left behind a very restrained, undeniable digital footprint online. His public traces are highly concentrated between 2008 and 2011, primarily including a private email (`satoshin@gmx.com`), newsgroup mailing list activity, a SourceForge project management account, and `Bitcoin.org` domain management/payment details. However, these were compromised in September 2014 when the email account was stolen (note: the German free email provider GMX allowed password resets via birthdate at the time, leading to its compromise). Subsequently, various accounts had their passwords reset. Any clear evidence linking to Satoshi's identity had been tainted. Furthermore, the primary forum where Satoshi posted was migrated to Bitcointalk, and its content and posts have been heavily modified; the current Bitcointalk account does not belong to Satoshi.

---
## 🗂️ They Are Definitely Not Satoshi (Click sections to expand)

<details>
<summary><b>⏱️ 1. Why Adam Back Appears in the Bitcoin Whitepaper References</b></summary>

<br>

> Satoshi Nakamoto's email interactions with Cypherpunk members Adam Back and Wei Dai before releasing the Bitcoin whitepaper. This is also why Adam Back and Wei Dai appear in the whitepaper's references.

| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Time&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Sender / Interactant | Email Subject / Core Content | Key Details & Follow-up |
| :--- | :--- | :--- | :--- |
| **2008-08-20** | Satoshi ➡️ Adam Back | Informing Hashcash will be cited, inviting him to review the draft. | Satoshi proactively paying tribute. |
| **2008-08-21** | Adam Back ➡️ Satoshi | Brief reply, no collaboration mentioned, suggests investigating Wei Dai's "b-money." | Back later admitted he set the project aside and didn't read the whitepaper. |
| **2008-08-22 16:00** | Satoshi ➡️ Wei Dai | Subject: "Citing your b-money page"<br>Informs him of extending his idea, referencing Back's recommendation. | Verified b-money's publication year for accurate citation; attached a summary of a "peer-to-peer electronic cash system" solving double-spending. |
| **August 2008** | Wei Dai ➡️ Satoshi | Replied with the publication date for b-money. | Confirmed b-money was published in **1998** on the Cypherpunks mailing list. |
| **January 2009** | Satoshi ➡️ Wei Dai | Informs `bitcoin.org` is live, v0.1 is officially released. | Email begins: "Hi Wei, just wanted to let you know... the official release is tomorrow." |

</details>

<hr>

<details>
<summary><b>👤 2. Candidate Screening: Adam Back — ❌ Excluded</b></summary>

<br>

| 📋 Dimension | Core Facts & Exclusion Logic |
| :--- | :--- |
| **🆔 Basic Information** | **Date of Birth**: July 1970<br>**Current Status**: CEO of Blockstream, now one of Bitcoin's biggest beneficiaries. Blockstream controls the code changes for BTC (Bitcoin Core). By permanently capping the BTC block size at 1 MB, they create transaction scarcity and high fees, forcing users onto Blockstream's fee-based Lightning Network. Capital controlling Blockstream includes the Bilderberg Group, AXA, MasterCard, DCG, the Federal Reserve, and the Federal Reserve Bank of New York. |
| **❓ Reason for Suspecting Satoshi** | Hashcash's invention hasn't been a badge of honor for Adam Back but a chain imprisoning him in Satoshi's shadow. Pushed to the forefront as a puppet by interest groups, Back continues to play a divided role: vehemently denying his identity in courts and media, yet in private emails and public texts, like a paranoid archaeological forger, he mimics Satoshi's archaic typing habits—like the "double spacing" after periods. This transparent imitation serves as his pathetic disguise as an outsider. |
| **⏳ Pre-2010 Attitude** | **Complete Academic Apathy**. During Bitcoin's nascent stage from 2008-2010, he ran no nodes, participated in no early email discussions, and didn't even download the client, displaying a total attitude vacuum. Back has admitted he didn't actively use or closely follow Bitcoin until around 2013. He told an interviewer: "I had doubts about Bitcoin's sustainability. It was 2009, there were no transactions, no value." He missed the early mining window and wasn't present on the `bitcoin.org` forum during its formative years. |
| **✉️ Early Communication & Exclusion Evidence** | **Physical Exclusion Evidence (Authentic 2008 Emails)**. The 2024 UK High Court (COPA case) revealed original emails from Satoshi to Back on August 20, 2008, requesting the correct citation format for Hashcash. Verified via digital signatures and server headers as authentic two-way communication, physically eliminating him from suspicion. |
| **📢 Public Statements on Identity** | Repeatedly stated publicly on Bloomberg, CoinDesk, and Twitter: "I am not Satoshi." He insists he is merely an inspired reference in the paper and notes the inherent contradiction between his role as a corporate CEO and Satoshi's decentralized, anonymous myth. He suffers from a schizophrenic self-contradiction: vocally distancing himself from Satoshi yet subtly and deliberately exploiting the ambiguity, even pixel-perfectly imitating Satoshi's speech patterns. Through Blockstream and decades of investments in early crypto assets, Back is publicly known as one of the wealthiest and most powerful figures in the space, but we know him for what he is—a clown riding Satoshi's coattails while being among those who most ruthlessly suppress him. |

</details>

<hr>

<details>
<summary><b>👤 3. Candidate Screening: Wei Dai — ❌ Excluded</b></summary>

<br>

| 📋 Dimension | Core Facts & Exclusion Logic |
| :--- | :--- |
| **🆔 Basic Information** | **Date of Birth**: 1976<br>**Current Status**: Extremely private, reclusive computer engineer and cryptography researcher. |
| **❓ Reason for Suspecting Satoshi** | His 1998 proposal for `b-money` is the theoretical bedrock of modern cryptocurrency, emphasizing anonymous distributed electronic cash. Satoshi cited him first in the Bitcoin whitepaper (Reference [1]). His legendary status in cryptography, privacy-focused demeanor, and online anonymity mark him as a seed candidate. (A widely circulated photo of an Asian man labeled "Wei Dai" is actually of a professor at NYU with the same name.) |
| **⏳ Pre-2010 Attitude** | **Timeline Mismatch and Neglect**. Around 2008, he had shifted focus to rationalist philosophy forums (LessWrong), no longer active in core cryptography circles. When Bitcoin launched in 2009, he never expressed interest publicly or privately, only examining it later with academic detachment when it gained small financial value. |
| **✉️ Early Communication & Exclusion Evidence** | **Cognitive Asymmetry Proof**. In August 2008, Satoshi wrote a humble email to Wei Dai, expressing intent to "turn his idea into a complete working system." However, the communication revealed a vast technical gap: Satoshi's concepts—financial game theory, hashing power Nash equilibrium, and dynamic difficulty adjustment—were entirely outside the scope of Wei Dai's original `b-money`. This disparity, combined with authentic, time-stamped one-way email communication, provides an irreversible physical and logical exclusion chain. |
| **📢 Public Statements on Identity** | Has repeatedly and firmly denied being Satoshi on LessWrong and in personal emails. He clarified that their interaction was limited to brief academic discussion, with him being consulted and inspired. He even pointed out irreconcilable differences between Bitcoin's design (deflationary issuance, PoW resource consumption) and his original `b-money` vision. He expressed regret at not having contributed earlier, thus definitively distancing himself. |

</details>

<hr>

<details>
<summary><b>👤 4. Candidate Screening: Nick Szabo — ❌ Excluded</b></summary>

<br>

| 📋 Dimension | Core Facts & Exclusion Logic |
| :--- | :--- |
| **🆔 Basic Information** | **Date of Birth**: April 5, 1964<br>**Current Status**: Independent scholar, advisor to multiple blockchain projects, frequently publishes on law and cryptography. |
| **❓ Reason for Suspecting Satoshi** | Inventor of Bit Gold; its inflation-control and scarcity mechanisms closely mirror Bitcoin's. The complete lack of interaction or communication with Satoshi fueled media suspicion. |
| **⏳ Pre-2010 Attitude** | **Fatal Atypical Silence**. As recently as April 2008, he was publicly recruiting volunteers to help code Bit Gold on his blog (proving he still hadn't solved the double-spending deadlock). When the Bitcoin code launched in January 2009, perfectly addressing this flaw, he fell into an unusual silence lasting years, only mentioning Bitcoin publicly in 2011. Szabo is the foundational theorist of "digital gold," consistently insisting Bit Gold was the true digital gold, yet it never progressed beyond the conceptual stage; no code has ever been seen. |
| **✉️ Early Communication & Exclusion Evidence** | **Zero Communication Mystery**. A mysterious "communication gap" exists between Satoshi and Szabo in early public records. Strangely, the Bitcoin whitepaper meticulously lists 8 references but omits the most closely related Bit Gold. While Satoshi later claimed he "learned of the project only after publication," this deliberate non-overlap, combined with fundamental differences in coding style (Satoshi preferring C++ pragmatism, Szabo proficient in Perl/C financial scripting), paradoxically excludes Szabo via a "reverse exclusion" logic. |
| **📢 Public Statements on Identity** | In a 2014 email to financial writer Nathaniel Popper, he clearly responded: "I'm afraid you have the wrong person, I'm used to being mistaken for Satoshi, but I'm not ('I'm not Satoshi')." Szabo conceptualized Bit Gold but has no publicly known communication with Satoshi and has never acknowledged any interaction. |

</details>

<hr>

<details>
<summary><b>👤 5. Candidate Screening: Hal Finney — ❌ Excluded</b></summary>

<br>

| 📋 Dimension | Core Facts & Exclusion Logic |
| :--- | :--- |
| **🆔 Basic Information** | **Date of Birth**: May 4, 1956<br>**Current Status**: Deceased (Date of Death: August 28, 2014; Body cryonically preserved). |
| **❓ Reason for Suspecting Satoshi** | Hal Finney was the recipient of Bitcoin's first transaction and the first person to report bugs to Satoshi, engaging in extensive email correspondence. He invented RPOW in 2004, one of the most important predecessor technologies to cryptocurrency. He was also a key developer of the open-source encryption software PGP. He deserves our respect. |
| **⏳ Pre-2010 Attitude** | **Extreme Enthusiasm vs. Physical Deterioration**. Finney received the first Bitcoin transaction from Satoshi in January 2009. He was a brilliant cryptographer and a true Cypherpunk. By late 2010, however, his ALS had progressed significantly, making typing extremely difficult. Meanwhile, Satoshi was posting and coding at high frequency and speed. The divergence in their physical capabilities is an unbridgeable gap. |
| **✉️ Early Communication & Exclusion Evidence** | **Overwhelming Physical Proof (Debugging Trails & Key Separation)**.<br><br>In the days following Bitcoin's launch in January 2009, Hal Finney ran it on Windows (Win32). The program crashed frequently. He and Satoshi exchanged dense emails, with Finney sending error logs and Satoshi fixing bugs almost in real-time. Hal Finney confirmed this in his 2013 post "Bitcoin and me": *"I was the second person to run Bitcoin... We exchanged emails for the next few days, mostly me reporting bugs and him fixing them almost instantly."* These 2009 emails have come to light primarily because:<br>1. **Finney's own partial disclosure**: He showed some emails to blockchain journalists (e.g., Nathaniel Popper) to prove "Satoshi and I are two different people."<br>2. **2013 Memoir**: Hal, suffering from ALS, published a long post titled "Bitcoin and me (Hal Finney)" on the Bitcoin forum. He recalled: *"Those were the days when difficulty was 1, and you could find blocks with a CPU, not even a GPU. I mined several blocks over the next days. But I turned it off because it made my computer run hot, and the fan noise bothered me."* <br><br>Hal Finney recalled putting Bitcoin aside after shutting down his computer and only hearing about it again in late 2010. When he checked his old wallet, the early mined and received coins were still there. Finney returned to the community in November 2010. Though his ALS was worsening, he continued coding with remarkable determination. |
| **📢 Public Statements on Identity** | Repeatedly and firmly denied being Satoshi. In a 2014 Forbes interview, he stated: "I am not Satoshi." To prove his innocence, he showed his early `wallet.dat` to media before his death, containing not only the 10 BTC transaction from Block 9 but also several early blocks he mined in mid-January 2009. He also pointed out fundamental differences in coding style and logic. He was Satoshi's first code auditor and tester.<br><br>Finney described his first encounter with Bitcoin: "When Satoshi announced the first version of the software, I downloaded it immediately." **Read this carefully: a user's statement, not a developer's. A developer/co-creator wouldn't "download" the software version; they would *build* it.** |

</details>

<hr>

<details>
<summary><b>💰 6. From Cryptography to Balance: The Simplest Path to Finding Satoshi</b></summary>

<br>

💬 Satoshi Nakamoto is a **pragmatic, impatient, business-minded developer** who embedded a poker lobby directly into the source code, preferred Windows, panicked over WikiLeaks, fixed consensus-breaking bugs within 5 hours, and wrote code resembling that of a 90s-era online gambling company's risk department.

💬 Satoshi didn't care if the code was "beautiful," only whether the system would crash. In 2008, when he sat down to solve the double-spending problem that had stumped professional cryptographers for 20 years, he didn't use cutting-edge academic tools or industry standards. He chose the boring, clunky, yet robust C-style patterns he had used his entire career: Hungarian notation, monolithic main files, Berkeley DB, Windows binaries, `wxWidgets`, structs, and pointer-heavy C++. Release first, patch later.

📌 **Profile Conflict Analysis**:
This profile doesn't fit Hal Finney, Adam Back, Nick Szabo, Wei Dai, or any prominent academic cryptographer. It fits a very different kind of professional, almost certainly someone who worked in the **gambling industry in the late 1990s and early 2000s**, where performance, security, and transaction integrity were paramount. In 2026, the ultimate key to finding Satoshi is no longer looking at code; it's looking at wallets.

> **🎯 Final Conclusion**: The real Satoshi Nakamoto wasn't a revolutionary; he was a **product manager** and a **senior engineer**. His career instilled in him a habit of continuously releasing products, assuming users are fools and attackers are geniuses.

</details>

</td>
</tr>
</table>

---

# 📅 Satoshi's Originality — 11 Core Invention Modules ✨

| 💎 Satoshi's Unique Inventions |
| :--- |
| Building upon the 10 predecessors' foundations, Satoshi didn't write academic papers. He stood on the high ground of industrial implementation and systemic game theory, personally developing and creating the following 11 modules. |
| 👑 **1. Unspent Transaction Output (UTXO) Ledger Model**<br><br>* Breakthrough: Abandoned the millennia-old traditional "Account/Balance" system entirely. The Bitcoin ledger doesn't record "how much is in someone's account"; it only consists of scattered, unspent digital checks (UTXOs) across the network.<br>* Engineering Value: Each transaction's input must precisely point to and consume an existing UTXO, while generating new UTXOs (outputs). This "spend and destroy" coin-like design natively prevents Double-Spending attacks in asynchronous decentralized networks and allows concurrent verification of different users' transactions without locking the entire account tree. |
| 👑 **2. Difficulty Adjustment Algorithm (DAA)**<br><br>* Breakthrough: Broke the fixed difficulty deadlock of Adam Back's Hashcash. Satoshi introduced an adaptive negative feedback control loop.<br>* Engineering Value: The system specifies that every 2016 blocks (about 2 weeks), nodes automatically adjust the target hash difficulty proportionally based on the actual time taken. This invention counteracts hardware development (Moore's Law) and hashing power fluctuations, successfully anchoring the average block time to about 10 minutes, creating the first decentralized self-sustaining clock in history. |
| 👑 **3. Economic Incentives & Halving Game Model**<br><br>* Breakthrough: First integration of game theory (Nash equilibrium) into a pure technical ledger. Satoshi realized cryptography alone couldn't prevent node misbehavior; "human selfishness" had to be harnessed for security.<br>* Engineering Value: Designed block rewards (coin distribution) and transaction fees. Total supply is capped at 21 million, with rewards halving every 210,000 blocks (~4 years). It achieves a delicate game-theoretic balance: the economic benefit of honest mining (Coinbase reward + fees) for an attacker with 51% hashing power far outweighs the cost of attacks that would undermine the system's credibility. |
| 👑 **4. Nakamoto Consensus (Longest Chain Rule)**<br><br>* Breakthrough: The soul of the Bitcoin loop. Previous BFT consensus required known, limited members. Satoshi pioneered "probabilistic deterministic consensus" for fully open, permissionless networks.<br>* Engineering Value: Ingeniously combines PoW with the longest chain rule. During network delays or forks, global nodes unconditionally follow the chain with the highest cumulative PoW. It uses thermodynamic energy consumption as voting power, perfectly solving the history consistency problem in decentralized ledgers. |
| 👑 **5. Block Header Data Structure Architecture**<br><br>* Breakthrough: A remarkably precise 80-byte tamper-proof skeleton. Satoshi combined previous technologies (hash links and Merkle trees) into a minimal structure, building the "Timechain."<br>* Engineering Value: The block header is strictly constrained to 6 fields, totaling 80 bytes. This forms the absolute backbone of the block. Tampering with even one byte in the Merkle tree changes the Merkle root, invalidating the PoW proof computed from these 80 bytes. |
| 👑 **6. Bitcoin Script Language & Execution Environment**<br><br>* Breakthrough: Satoshi personally crafted a low-level, stack-based, left-to-right scripting system.<br>* Engineering Value: This highly programmable, Turing-complete language runs on a dual-stack architecture (main and alt stacks), functionally complete under specific constraints. Every UTXO is locked by a locking script; spending requires the correct unlocking script. This laid the foundation for multi-signature, time-locks, and smart contracts. |
| 👑 **7. Simplified Payment Verification (SPV)**<br><br>* Breakthrough: Lightweight client verification theory. Satoshi outlined and implemented a mobile-friendly scaling solution in Chapter 8 of the whitepaper.<br>* Engineering Value: Allows lightweight devices to verify their transactions without downloading the entire blockchain, only the 80-byte block headers every 10 minutes. By requesting a Merkle path proof from full nodes, they can 100% locally confirm their transaction's inclusion with minimal data and computation. |
| 👑 **8. Coinbase Transaction Mechanism**<br><br>* Breakthrough: Decentralized currency minting mechanism.<br>* Engineering Value: A special transaction type—`Coinbase`—with no inputs, only outputs. As the first transaction in each block, it allows the winning miner to mint the specified amount of Bitcoin plus fees. This completely removes reliance on a central bank for currency issuance. |
| 👑 **9. Mempool Prototype**<br><br>* Breakthrough: A distributed buffering zone for unconfirmed transactions in nodes' volatile memory (RAM).<br>* Engineering Value: In Satoshi's 2009 v0.1.0 code, he designed the `mapTxMemPool` data structure. Upon receiving a valid transaction, nodes hold it in the Mempool for miners to select based on fees, rather than writing it directly to disk. This is the core hub for high-concurrency asynchronous transaction flow. |
| 👑 **10. Base58Check Encoding & Address Format**<br><br>* Breakthrough: The first blockchain user experience (UX) and error-proofing innovation.<br>* Engineering Value: Before Bitcoin, public keys were unwieldy hexadecimal strings. Satoshi personally removed 4 visually confusing characters (0, O, I, l), inventing the Base58 character set. Combined with a double SHA-256 checksum (Base58Check), typographical errors are caught by the client, preventing funds from being sent to an invalid address. |
| 👑 **11. Wallet & Key Management Prototype**<br><br>* Breakthrough: First client-side implementation of automated private key, public key, and address management.<br>* Engineering Value: Introduced `wallet.dat` in v0.1.0. For privacy and backup convenience, he designed a Keypool (a buffer of 100 pre-generated random keys). Though later superseded by BIP32/BIP39 deterministic wallets, it represents the first practical key management module in blockchain history. |

| 💎 Time | Person | Goal Achieved | Invention / Core Contribution | Category |
| :--- | :--- | :--- | :--- | :--- |
| **2008** | Satoshi | Prevent double-spending | **UTXO Ledger Model**: Revolutionized the account balance system, using unspent transaction outputs as the ledger basis for concurrent verification and native double-spend prevention. | Ledger Data Model |
| **2008** | Satoshi | Consistent 10-minute block time | **Difficulty Adjustment Algorithm (DAA)**: Introduced an adaptive control loop, countering Moore's Law, anchoring average block time to 10 minutes. | Consensus Self-Regulation |
| **2008** | Satoshi | Make honest mining more profitable than attacking | **Economic Incentives & Halving Model**: Cap at 21 million with halving every 4 years, uses Nash equilibrium to ensure honest mining yields greater rewards than cheating. | Tokenomics / Game Theory |
| **2008** | Satoshi | Hashing power decides consensus | **Nakamoto Consensus (Longest Chain Rule)**: Combined PoW with the longest chain rule, pioneering probabilistic deterministic consensus for permissionless networks, using thermodynamic energy for history consistency. | Distributed Consensus |
| **2008** | Satoshi | Tampering with ledger is impossible | **Block Header Data Structure**: Packed hash pointers and Merkle trees into an 80-byte minimal skeleton, building the "Timechain" where localized tampering invalidates the entire block. | Core Data Structure |
| **2008** | Satoshi | Disallowed complex instructions | **Bitcoin Script Language**: A stack-based, non-Turing complete (functionally complete) scripting system, removing loops to prevent DoS attacks, laying the foundation for programmable finance. | Programming Language / Smart Contracts |
| **2008** | Satoshi | Simplified verification for mobile | **Simplified Payment Verification (SPV)**: Lightweight client scaling solution allowing mobile devices to verify transactions with just block headers and Merkle paths. | Network Scaling / Light Client |
| **2008** | Satoshi | Fair, decentralized money issuance | **Coinbase Transaction Mechanism**: A special transaction with no inputs, allowing the winning miner to mint new coins, removing dependence on a central bank. | Currency Minting / Transactions |
| **2009** | Satoshi | High-concurrency transaction queue | **Mempool Prototype**: An in-memory distributed buffer for unconfirmed transactions, serving as the hub for high-concurrency asynchronous transaction flow. | Network Engineering / Transaction Flow |
| **2009** | Satoshi | Prevent address transcription errors | **Base58Check Encoding & Address Format**: Removed 4 visually confusing characters and added a checksum, optimizing UX and preventing asset loss due to typos. | UX / Encoding Standard |
| **2009** | Satoshi | Key determines ownership | **Wallet & Keypool Prototype**: Designed the Keypool with pre-generated private keys, implementing the first automated key management module. | Key Management / Client Engineering |

| 💎 Architecture Panorama | The Ultimate Closed-Loop Form — A 7-Layer Self-Sustaining Architectural System |
| :--- | :--- |
| **Introduction** | Combining the 10 predecessor foundations with Satoshi's 11 original inventions yields the 7-layer industrial-grade full-stack architecture of the Bitcoin system, evolving from underlying technology to a self-sustaining loop. Layer by layer, no logical gaps exist: |
| **7-Layer Full-Stack Architecture** | <table><tr><th>Layer</th><th>Core Name</th><th>Technology Stack & Core Components</th></tr><tr><td>**Layer 7**</td><td>**Economic Game Theory**<br>(Incentive & Game Theory)</td><td>`Coinbase` mechanism + Halving model + Fees (Source of self-sustenance)</td></tr><tr><td>**Layer 6**</td><td>**System Scheduling**<br>(System Scheduling & Engineering)</td><td>`Mempool` prototype + `wallet.dat` keypool</td></tr><tr><td>**Layer 5**</td><td>**Consensus Drive**<br>(Consensus & Dynamism)</td><td>`PoW` hashing power + `Nakamoto Consensus` longest chain rule</td></tr><tr><td>**Layer 4**</td><td>**Verification & Control**<br>(Validation & Control)</td><td>`DAA` difficulty adjustment clock + `SPV` mobile verification + Validation rules</td></tr><tr><td>**Layer 3**</td><td>**Ledger Logic**<br>(Ledger & Logic)</td><td>`UTXO` model + `Bitcoin Script` (Turing-complete, functionally constrained)</td></tr><tr><td>**Layer 2**</td><td>**Data Skeleton**<br>(Data Structure & Skeleton)</td><td>80-byte block header + Merkle Tree + Hash-linked tamper-proof chain</td></tr><tr><td>**Layer 1**</td><td>**Cryptographic Network**<br>(Infrastructure & Cryptography)</td><td>`P2P` network + `secp256k1` + `Base58Check` encoding</td></tr></table> |
| **Operational Dynamics Analysis**<br>**(How the System Achieves Self-Sustenance Step by Step):** | <ol><li>**Infrastructure Initialization (Layer 1)**: Establishes a global communication channel via the physical `P2P Network` without central servers, uses `secp256k1` for absolute ownership, and translates mathematical public keys into user-friendly addresses via `Base58Check`.</li><li>**Building the Static Ledger (Layers 2 & 3)**: Transactions are expressed using the `UTXO model`. Transfers aren't balance changes but the destruction of old coins and creation of new ones, locked by `Bitcoin Script`. Transactions are compressed into `Merkle Trees` and locked into the 80-byte `Block Header` via `Hash-linked Timestamping`, forming an immutable static history.</li><li>**Introducing the Adaptive Clock & Verification (Layers 4 & 5)**: To move this static ledger forward, nodes must compete via `Proof of Work`. The `DAA` acts as an adaptive valve, enforcing a ~10-minute block release. When network splits occur, the `Nakamoto Consensus (Longest Chain Rule)` acts like gravity, pulling nodes toward the chain with the most cumulative work, dynamically resolving forks.</li><li>**Activating the Endogenous Perpetual Motion (Layers 6 & 7)**: Unconfirmed transactions queue in the `Mempool`. Miners spend vast physical energy on `PoW` to maintain the system because Satoshi embedded `Economic Incentives` and the `Coinbase mechanism` at the top layer.<br><br><ul><li>For each block successfully mined, the miner can mint new Bitcoins.</li><li>**Game Theory Loop Formed**: Network security increases $\rightarrow$ confidence in its scarcity (halving model) grows $\rightarrow$ higher profit expectations $\rightarrow$ attracts more hashing power $\rightarrow$ `DAA` increases verification difficulty $\rightarrow$ attack cost skyrockets $\rightarrow$ network security further increases.</li></ul></li></ol> |

---

# 📅 Bitcoin Early Code P2P Poker (Gambling) Logic Analysis ✨

In the first version of the Bitcoin source code (v0.1.0 Alpha), lines 1573 to 1731 of the original source tree contained framework code for a multiplayer card game running inside the Bitcoin client. Satoshi Nakamoto had built a complete **P2P Poker game** within it. Below is a structured analysis of this underlying source code, its core directives, and its actual design intent.

## 👽 Core Code Reveals Secular Origins, Design Intent, Motivational Prototype

| Core Category | Specific Functions/Instructions | Corresponding Technical Implementation / Business Logic | Satoshi's Deep Design Intent (Decentralized Vision) |
| :--- | :--- | :--- | :--- |
| **1. Poker Action Handlers** | <ul><li>`SendDealHand` (Deal)</li><li>`SendFold`</li><li>`SendCall`</li><li>`SendCheck`</li><li>`SendRaise`</li><li>`SendLeaveTable`</li></ul> | Defined the `CPokerLobbyDialogBase` class in early repositories (like `main.cpp`) to handle core poker game commands. | **Testing Ground for Conditional Payments and Smart Contracts**: Poker requires a pot, needing players to lock bets and pay the winner. This perfectly mimics **Multi-signature** and **Timelock** scenarios. Poker proved that mutually untrusting individuals could safely bet and settle funds without a central server. |
| **2. Game State & Network Sync** | <ul><li>`SendBet`</li><li>`GetGame`</li></ul> | Broadcast player actions and current game state among P2P nodes. | **Built-in "Killer App" to Attract Early Nodes**: The first version also included an IRC chat client and P2P marketplace. Satoshi envisioned the client as integrated entertainment software for "chatting, trading, playing poker, and mining," incentivizing users to run nodes for trustless poker, thus bolstering network security. |

### 🙌 The Harsh Underlying Truth

Although Bitcoin evolved into a global digital asset, tracing its historical roots and initial code reveals:
1. **Funding and Compliance Camouflage**: During its conceptual incubation (2001-2009), these functions partly served to secure research funding and tax exemptions from the Australian government.
2. **The Original Purpose**: Bitcoin's initial implementation was likely aimed at developing a **decentralized online poker platform**. In that original design, "Bitcoin" was simply intended as a **trustless gaming chip** for internal use.

---

# 📅 Bitcoin Early Historical Events & Background (2009 - 2010) ✨

| 🌊 Satoshi Only Sent Bitcoin to 2 People Before November 2009 |
| :--- |
| First launch Jan 3, 2009, ran 6 days, then abandoned. Second launch Jan 9, 2009, mined Block 1, mainnet running since. |
| On January 12, 2009, Satoshi performed multiple test transfers from the Block 9 address `12cbQLTFMXRnSzktFkuoG3eHoMeFtpTu3S`.<br/>
`2009-01-12 03:30:25 Sent 10 to Hal Finney (1Q2TWHE3GMdB6BZKafqwxXtWAWgFt5Jvm);`<br/>
`2009-01-12 06:02:13 Sent 10 to Zooko Hearn (1DUDsfc23Dv9sPMEk5RsrtfzCw5ofi5sVW);`<br/>
`2009-01-12 06:12:16 Sent 1 to (1LzBzVqEeuQyjD2mRWHes3dgWrT9titxvq);`<br/>
`2009-01-12 14:21:00 Sent 1 to (1BDvQZjaAJH4ecZ8aL3fYgTi7rnn3o2thE);`<br/>
`2009-01-12 06:34:22 Sent 1 to (13HtsYzne8xVPdGDnmJX8gHgBZerAfJGEf);`<br/>
`2009-01-14 20:40:55 Sent 1 to (15NUwyBYrZcnUgTagsm1A7M2yL2GntpuaZ);`<br/>
`2009-01-14 20:40:55 Sent 1 to (1BBz9Z15YpELQ4QP5sEKb1SwxkcmPb5TMs);`<br/>
`2009-01-12 20:04:20 Sent 10 to (1ByLSV2gLRcuqUmfdYcpPQH8Npm8cccsFg);`<br/>
`2009-01-13 18:49:42 Block 360 (18SH9vwx24L5cTabfkgtGMjF8A56pD9AUJ) sent 50 to (15NUwyBYrZcnUgTagsm1A7M2yL2GntpuaZ);`<br/>
`2009-01-15 14:25:20 Consolidated 250 Bitcoins from Blocks 268, 417, 431, 442, 450 to address (19QKDUJtx9n7Vaga6nX1bVHdsnT4Khfyi6), never moved since. This was his first consolidation test.`<br/>|
| In early 2009, Satoshi only sent Bitcoin to two people: Hal Finney and Zooko Wilcox-O'Hearn, both subscribers to the Cypherpunks mailing list. |
| When the Bitcoin forum (`bitcoin.org/smf/`) launched on November 22, 2009, Satoshi occasionally sent Bitcoin to some registered users upon request; it was worthless then. Many were anonymous, one was `Nicholas Bohm`. |
| In the 2026 COPA case, Satoshi said he sent Bitcoin to Zooko because Zooko expressed great interest, having previously researched a similar project called MojoNation. Zooko denied receiving Bitcoin from Satoshi, claiming his first Bitcoin came from OTC trades. It appears Zooko did not keep the private keys for the address where Satoshi sent Bitcoin. In the COPA case, Nicholas Bohm testified he received Bitcoin from Satoshi, stating that Satoshi knew his name. In fact, he had anonymously requested it from the forum. |
| Mike Hearn claimed to have conducted test transactions with Satoshi on April 18, 2009; this is false. In reality, Mike Hearn conducted the tests himself. Hearn was among those who communicated with Satoshi via email before his departure. For various reasons, he later lied about testing with Satoshi in 2009 and subsequently losing the early private keys. This lie became widely known in the Bitcoin community and contributed to his reluctance to acknowledge Craig as Satoshi when they later met. |
| One of the earliest Bitcoin miners was Max Lynam. After Bitcoin launched, Craig Wright sent the program to his uncle for testing. The uncle enlisted his son Max Lynam (Craig's cousin) to run it on his laptop continuously until late 2011. Due to business failure, they had to close down. His father turned off the computer and threw it in the trash before moving. In 2013, Max Lynam, his wife, and daughter visited Melbourne and met Craig's second wife, Ramona. During dinner, Craig asked: "Do you still have that computer?" Upon learning of its fate, he said: "You should have kept it; it might be worth something." Craig explained that if Bitcoin reached $800, Max would be rich. He estimated, based on their computer and runtime, that they should have around 6,500 Bitcoins. |
| In 2009, Satoshi mined over 67% of the year's Bitcoins. He released 1/3 of his hashing power, deliberately lowering mining difficulty to allow early participants to mine blocks. |

| 🌊 Date | Event Summary | Historical Background Chronicle |
| :--- | :--- | :--- |
| **Feb 6, 2010** | **First Exchange Launches**<br>`BitcoinMarket` goes live, introducing online order matching. | As the number of miners grew, private trading became cumbersome. Forum user `dwdollar` (real name `Dustin Trammell`) proposed and built this platform. He wrote at the time: "I am trying to create a market where Bitcoins are treated as a commodity." The site initially relied on PayPal for fiat deposits, but was later banned by PayPal due to a massive wave of credit card chargeback fraud. |
| **May 22, 2010** | **Bitcoin Pizza Day is Born**<br>Laszlo Hanyecz buys two Papa John's pizzas for 10,000 `BTC`. | Laszlo Hanyecz, a Florida programmer and the first person to write GPU mining code, posted on the Bitcoin forum on May 18 looking to buy pizza. Four days later, 19-year-old user `Jercos` (`Jeremy Sturdivant`) took the request, ordered the food out of his own pocket for about $25, had it delivered to Laszlo's house, and successfully received the 10,000 Bitcoins. This was the first commercial transaction using Bitcoin for a physical commodity in the real world. |
| **Jun 18, 2010** | **Satoshi Reveals Development History**<br>Satoshi admits on the forum that the project had been under design since 2007. | At the time, someone on the forum questioned whether the Bitcoin system could sustain itself in the long run. In his reply, Satoshi revealed his cards, stating that he had spent at least a year quietly writing code before publishing the white paper in 2008, because he had to "convince myself that a trustless system could actually work on a code level before publishing the theory." |
| **Jul 11, 2010** | **The Media Effect Explodes**<br>A report on `Slashdot` triggers an influx of trial users, and Bitcoin enters its price narrative. | Around this time, Bitcoin v0.3 was released and submitted to the tech news site `Slashdot`. A massive wave of traffic rushed in, briefly crashing the official `bitcoin.org` website. The influx of new miners and speculators immediately broke the supply-demand balance, sparking Bitcoin's first micro-bull run since its inception. |
| **Jul 18, 2010** | **Mt. Gox Exchange Launches**<br>Founded by Jed McCaleb, it would later become the world's largest exchange. | Programmer `Jed McCaleb` learned about Bitcoin after coming across the `Slashdot` article. Finding the user experience on `BitcoinMarket` to be subpar, he spent a week coding a new exchange. He used an idle domain name he owned, "`mtgox.com`" (originally standing for "Magic: The Gathering Online eXchange"), and a legend was born. |
| **Aug 15, 2010** | **The Value Overflow Bug**<br>A hacker generates 184.4 billion `BTC` out of thin air; fixed via soft fork. | Because early code did not rigorously validate whether transaction values would exceed variable limits when handling massive amounts, a hacker exploited this flaw in block `#74,638` to send nearly 184.4 billion Bitcoins to two addresses. Upon discovery, Satoshi rushed out the v0.3.10 patch within 5 hours. By rallying all honest hashing power to upgrade, they used a completely new and compliant long chain to isolate and wipe out the hacker's anomalous block. |
| **Dec 5, 2010** | **WikiLeaks Controversy (Prelude)**<br>Cut off by traditional finance, calls grow for WikiLeaks to use Bitcoin; Satoshi strongly objects. | Julian Assange's "WikiLeaks" had published a vast amount of classified US diplomatic cables, resulting in an immediate financial blockade by Visa, Mastercard, and PayPal. Tech publication `PC World` published a column suggesting that WikiLeaks embrace Bitcoin. Satoshi was extremely anxious, knowing that Bitcoin's fragile hashing power at the time would be destroyed if it drew a targeted crackdown from US intelligence agencies. He posted a plea for WikiLeaks to spare Bitcoin, writing: "No, don't 'bring it on'. The project needs to grow gradually so the software can be strengthened along the way. I make this appeal to WikiLeaks not to try to use Bitcoin." |
| **Dec 11, 2010** | **Satoshi's Sigh**<br>WikiLeaks accepts Bitcoin. Satoshi posts: "In any other context, this would be great to get this much attention. WikiLeaks has kicked the hornet's nest, and the swarm is headed our way." | **Background Story**: Despite Satoshi's multiple attempts to discourage it, under survival pressure, WikiLeaks announced it would accept Bitcoin donations, instantly propelling Bitcoin into the headlines of major international media outlets. Feeling that things had completely spiraled out of his control, Satoshi left a deeply pessimistic message on the forum. This event shattered the protective shield of Bitcoin's low-profile growth, forcing Satoshi to sever his public identity to protect the network. |
| **Dec 12, 2010** | **Complete Withdrawal**<br>Satoshi publishes his final forum post, marking his last public statement. | On December 12, 2010, Satoshi made his final post on the public forum. The post, numbered 575, was a minor update regarding DoS protections. There was no farewell message, no valedictory speech, and no dramatic statements. He simply posted a routine technical note, went offline, and never returned to the forum again. |

---

# 📅 List of Early Bitcoin Miners During 2009 ✨

| Name | Identity | Mining Start | Duration | Notes / Early Exploits | Attitude Toward Craig Wright |
| :--- | :--- | :--- | :--- | :--- | :---: |
| **Hal Finney** | Cryptographer | Jan 2009 | Shut down days later | Recipient of the first transaction in Bitcoin history (`Block 170`). | No public stance before passing |
| **David Kleiman** | Satoshi's Friend | Jan 2009 | Full Year | Held 1.1 million Bitcoins with Satoshi in the 2011 Tulip Trust. | No public stance before passing |
| **Max Lynam** | Satoshi's Cousin | Jan 2009 | Full Year | Mined until late 2011, later discarded the laptop containing approx. 6,500 Bitcoins. | Testified in support |
| **Ray Dillinger** | Cryptographer | Jan 2009 | Brief Test | Participated in node operations/test mining, but never kept or moved assets from that era. | Explicitly opposed |
| **Dustin D. Trammell** | Cryptographer | Jan 2009 | Brief Test | Mined thousands of Bitcoins on a few computers in Jan 2009; treated them as tests and didn't save them. | Testified against in `COPA` case |
| **Martti Malmi** | Finnish Student | May 2009 | Continuous | Self-reported mining over 50,000 Bitcoins in 2009–2010, exchanging 5,050 of them for $5.02. | Testified against in `COPA` case |
| **Mike Hearn** | Google Engineer | Apr 2009 | Brief Test | Emailed Satoshi to ask how Bitcoin worked and downloaded the client for a brief mining test. | Explicitly rejects |
| **Laszlo Hanyecz** | Programmer | Oct 2009 | Continuous | Discovered `GPU` multi-threaded mining; Satoshi advised him to slow down. He later bought two pizzas with 10,000 Bitcoins. | Explicitly opposed |

Throughout 2009, Bitcoin's network-wide mining difficulty (`Difficulty`) was exactly 1. This was the initial baseline state of the entire Bitcoin network and the absolute theoretical minimum difficulty set in the code. Simply put, a difficulty of 1 meant the network was in its easiest possible mining state. On January 9, 2010, one year after Bitcoin launched, the mining difficulty rose to 1.2. By early 2011, it neared 15,000, and six months later, it broke past 1 million.

Satoshi mined a total of over 1.1 million Bitcoins over the course of 2009, selling more than 70,000 during the run to $19 in 2011. Following the exposure of the Tulip Trust, 1.1 million became the standard accepted figure for 2009. As of 2026, the remaining unsold 2009-mined Bitcoins belonging to Satoshi span 20,929 block addresses, totaling 1,045,972 BTC (this figure is derived from real-time on-chain data tracking as of June 30, 2026).

Therefore, a key distinction must be made: the 1.1 million coins refer to those mined in 2009, excluding subsequent years.

Starting in 2010, mining difficulty increased. From January 1, 2010, to August 21, 2010, Satoshi mined at least 7,041 more blocks, yielding roughly 350,000 coins.

For others mining in 2009, some figures remain unverified, including:  
`Dustin D. Trammell`: Mined thousands of coins briefly in January 2009 using a few personal workstations and servers. (Self-reported)  
`Martti Malmi`: Mined roughly 55,000 coins between 2009 and 2010 using a laptop. (Self-reported)  
`Max Lynam`: Estimated to have mined roughly 6,500 coins between 2009 and 2011. (Estimated by `Craig Wright`)  
`Laszlo Hanyecz`: Mined roughly over 40,000 Bitcoins between October and December 2009. (Self-reported, discovered `GPU` mining)  
`David Kleiman`: Estimated to have mined roughly 350,000 coins between 2009 and 2010 across two computers. (David told `Craig`)  
`Nicholas Bohm`: Mined roughly 100,000 Bitcoins in 2009 using an `HP Compaq` computer. (Court evidence)  
The two church computers maintained by Satoshi are estimated to have mined 80,000–100,000 coins. (Estimated by `Craig Wright`)  

Excluding sporadic testing, the entire year of 2009 saw roughly 20 to 30 computers mining globally.

During Bitcoin’s first year, `Craig Wright` mined at least two-thirds of the blocks.

---

# 📅 Mining Difficulty Timeline of the Satoshi Era ✨

| Date | Network Difficulty | Event |
| :--- | :--- | :--- |
| 2009-01-09 | 1 | Bitcoin launches |
| 2009-12-31 | 1 | Difficulty remains at 1 all year |
| 2010-01-09 | 1.2 | Bitcoin's 1st anniversary |
| 2010-02-06 | 1.8 | `Bitcoin Market` launches |
| 2010-05-22 | 12 | Pizza Day |
| 2010-06-22 | 17 | `The Farmers Market` |
| 2010-06-29 | 19 | Bitcoin Faucet |
| 2010-07-15 | 45 | Block size limited to 990 KB |
| 2010-07-18 | 181 | `Mt. Gox` exchange launches |
| 2010-07-28 | 245 | `OP_RETURN` bug |
| 2010-08-15 | 390 | 184 Billion bug |
| 2010-09-07 | 623 | Enforcement of 1 MB block size limit |
| 2010-10-05 | 1319 | `New Liberty Standard` |
| 2010-12-05 | 8078 | WikiLeaks Controversy |
| 2010-12-12 | 12252 | Satoshi's last post |
| 2011-02-09 | 25998 | Bitcoin hits dollar parity ($1) |
| 2011-02-14 | 34091 | Tulip Trust established |
| 2011-06-24 | 1067600 | Bitcoin touches $19 |
| 2011-08-06 | 1888800 | Difficulty reaches 2 million |

At a difficulty of 1, computers on the network need to try an average of $2^{32}$ (roughly 4.29 billion) hash collisions to find a single block. Regarding PC hardware power in 2009: a typical personal computer `CPU` at the time could run about 1 million to 10 million hash calculations per second (i.e., $1\ \text{Mhas/s}$ to $10\ \text{Mhas/s}$). This means that if you were mining alone on a regular computer in 2009, it would take an average of just 7 to 10 minutes to solo-mine a block and claim the 50 Bitcoin reward.

Satoshi designed the code to automatically adjust the network difficulty every 2,016 blocks (roughly every two weeks) based on block generation speeds. If total hash power was too strong and blocks were found too fast (less than two weeks), the difficulty would adjust upward; if hash power was too weak and blocks took too long (more than two weeks), difficulty would drop. However, throughout Bitcoin's initial year in 2009, only 20–30 computers were mining globally. Combined, the total network hash power frequently took two weeks or longer to accumulate 2,016 blocks. Because the code dictated that difficulty could not drop below 1, whenever an adjustment cycle was triggered, the system would find the hash power still incredibly weak and keep the difficulty pinned flat against the technical floor of 1.


The Real Game Changer

Around October 2010, the first public `GPU` mining software began circulating. `AMD` (then known as `ATI`) graphics cards became the undisputed kings of Bitcoin mining due to their `ALU` (Arithmetic Logic Unit) architecture, which was natively well-suited for the `SHA-256` algorithm.

The most legendary mining cards of that era were the `ATI Radeon HD 5870` and the dual-core flagship `HD 5970`:  
Hash power of a single `HD 5870`: Approx. $350\ \text{MH/s}$ (i.e., $0.35\ \text{GH/s}$)  
Hash power of a single `HD 5970`: Approx. $700\ \text{MH/s}$ (i.e., $0.70\ \text{GH/s}$)

By February 14, 2011, miners were assembling makeshift wooden or aluminum open-air rigs. A standard home PC (equipped with a kilowatt power supply and a compatible motherboard) could host 4 graphics cards. Just 10 of these rigs (carrying 40 graphics cards in total) could pump out $13.78\ \text{GH/s}$ of hash power—accounting for roughly 5.5% of the entire global network.

This explains why, after October 2010, Bitcoin's network mining difficulty skyrocketed like a rocket from just over 1,000 to past 1 million. For the first time, humanity realized that a generational gap in technology allowed ten GPU rigs to easily obliterate the output of thousands of legacy servers.

---

# 📅 Analysis of Early Bitcoin Difficulty and Hash Power Dilution ✨

In 2009, 1U to 4U rack servers typically housed two multi-core enterprise `CPUs` (such as `Intel Xeon`) and lacked any concept of modern `GPUs`. A typical configuration featured dual `Intel Xeon E5520` processors (totaling 8 physical cores / 16 threads, clocked at $2.26\ \text{GHz}$). With multi-threaded parallel processing, an entire server's combined output was roughly $16.5\ \text{MH/s}$.

Following Bitcoin's launch, `Craig Wright` utilized 10 to 12 servers for mining, yielding an estimated total hash power of $200\ \text{MH/s}$.

This table tracks network difficulty shifts at core historical milestones during Bitcoin's genesis era (2009–2011) and quantifies the evolution of on-chain hash power share under specific hardware allocations ($200\ \text{MH/s}$ server clusters in 2009–2010, upgrading to a $13.78\ \text{GH/s}$ GPU farm in 2011).

## February 2011: W&K sets a monthly target of mining 12,000 coins, requiring 13.78 GH/s. If no hardware was added prior, hash power dilution would look like this:

| Timeframe | Network Difficulty | Satoshi's Hash Power | Estimated Total Network Hash Power | Hash Power Share (Not equivalent to mining ratio) | 
| :--- | :--- | :--- | :--- | :--- | 
| **2009-01-09** | 1 | 200.00 MH/s | 7.16 MH/s | **100.00%** | 
| **2009-12-31** | 1 | 200.00 MH/s | 7.16 MH/s | **100.00%** | 
| **2010-01-09** | 1.2 | 200.00 MH/s | 8.59 MH/s | **100.00%** | 
| **2010-02-06** | 1.8 | 200.00 MH/s | 12.88 MH/s | **100.00%** | 
| **2010-05-22** | 12 | 200.00 MH/s | 85.90 MH/s | **100.00%** | 
| **2010-06-22** | 17 | 200.00 MH/s | 121.69 MH/s | **100.00%** | 
| **2010-06-29** | 19 | 200.00 MH/s | 136.01 MH/s | **100.00%** | 
| **2010-07-15** | 45 | 200.00 MH/s | 322.12 MH/s | **62.09%** | 
| **2010-07-18** | 181 | 200.00 MH/s | 1.29 GH/s | **15.44%** | 
| **2010-07-28** | 245 | 200.00 MH/s | 1.75 GH/s | **11.40%** | 
| **2010-08-15** | 390 | 200.00 MH/s | 2.79 GH/s | **7.16%** | 
| **2010-09-07** | 623 | 200.00 MH/s | 4.46 GH/s | **4.48%** | 
| **2010-10-05** | 1,319 | 200.00 MH/s | 9.44 GH/s | **2.12%** | 
| **2010-12-05** | 8,078 | 200.00 MH/s | 57.82 GH/s | **0.35%** | 
| **2010-12-12** | 12,252 | 200.00 MH/s | 87.70 GH/s | **0.23%** | 
| **2010-12-31** | 14,484 | 200.00 MH/s | 103.68 GH/s | **0.19%** | 
| **2011-02-09** | 25,998 | **13.78 GH/s** | 186.10 GH/s | **7.40%** | 
| **2011-02-14** | 34,091 | **13.78 GH/s** | 244.03 GH/s | **5.65%** | 
| **2011-06-24** | 1,067,600 | **13.78 GH/s** | 7.64 TH/s | **0.18%** | 
| **2011-08-06** | 1,888,800 | **13.78 GH/s** | 13.52 TH/s | **0.10%** | 

> * Total Network Hash Power ($H/s$) = $\text{Difficulty} \times \frac{2^{32}}{600 \text{ seconds}} \approx \text{Difficulty} \times 7,158,278.8$
> * When absolute hash power exceeds the network's back-calculated theoretical limit, actual on-chain share is noted as 100%. This is a theoretical value; in practice, Satoshi only mined 67% of blocks in 2009, indicating he throttled about 1/3 of his total power.

Between 2009 and 2010, Satoshi deployed fiber optic networks at the `Bagnoo` farm, converting a subset of sheds and rooms into data centers. He operated 55 to 75 servers (69 servers in 2009). Most ran `CentOS`, `Red Hat`, and `Solaris` to handle `DNS` and `sendmail` workloads, while a portion ran the `Timecoin` testnet.

A cluster of 10 to 12 Windows machines ran the core Bitcoin software. Operating within a single subnet, they appeared as a single node to the outside network. Therefore, even with 10 to 12 physical machines clustered in one location, they only broadcast as a single node. Separately, 3 laptops and 4 desktops were stationed at another site in Tenterfield. His core motivation during those days (2009–2010) was to deploy and test the application of this technology rather than seek economic profit. Hashing was merely a minor component back then. In Bitcoin's earliest phase, the vast majority of computing power was actually spent verifying `ECDSA` (Elliptic Curve Digital Signature Algorithm) signatures. `ECDSA` calculations are significantly heavier than simple hashing. Consequently, the servers spent much of their cycles executing block verification and audits.

The server rooms utilized a three-phase power distribution network billed via a separate commercial meter, generating a monthly electricity expense of 11,000 AUD, settled through `Information Defense Pty Ltd`.

Under multi-threaded conditions, the hash power of Satoshi's early 10–12 servers completely dominated the network. Satoshi intentionally paused his mining operations for 5 minutes at intervals, releasing his hash power to allow other participants a chance to successfully mine blocks.

In 2009, a standard home PC (a mainstream dual-core `Core 2 Duo` yielded around $1.5\ \text{MH/s}$) running 24/7 at max `CPU` load could mine roughly 4 blocks (200 BTC) daily, totaling around 73,000 BTC over a full year.

Notably, by mid-2010, Satoshi's hash power had surrendered its dominant position. Without the deployment of new hardware, the capacity of those 10–12 computers had fallen to just 0.2% of the global network by the end of 2010.

When W&K was established on February 14, 2011, it targeted a monthly output of 12,000 Bitcoins, which demanded roughly 5.5% of total network power (approx. $13.78\ \text{GH/s}$). This confirms that Satoshi expanded his infrastructure at that time—for example, deploying 10 rigs equipped with 40 `ATI 5970` graphics cards. Yet within six months, this share was diluted down to 0.1% once more.<br/>

---

# 📍 The End of the Satoshi Era, But the Journey Continues ✨

## Bitcoin v0.1 released

```text
Satoshi Nakamoto Fri, 09 Jan 2009 17:05:49 -0800

Announcing the first release of Bitcoin, a new electronic cash
system that uses a peer-to-peer network to prevent double-spending.
It's completely decentralized with no server or central authority.

See bitcoin.org for screenshots.

Download link:
[http://downloads.sourceforge.net/bitcoin/bitcoin-0.1.0.rar](http://downloads.sourceforge.net/bitcoin/bitcoin-0.1.0.rar)

Windows only for now.  Open source C++ code is included.

- Unpack the files into a directory
- Run BITCOIN.EXE
- It automatically connects to other nodes

If you can keep a node running that accepts incoming connections,
you'll really be helping the network a lot.  Port 8333 on your
firewall needs to be open to receive incoming connections.

The software is still alpha and experimental.  There's no guarantee
the system's state won't have to be restarted at some point if it
becomes necessary, although I've done everything I can to build in
extensibility and versioning.

You can get coins by getting someone to send you some, or turn on
Options->Generate Coins to run a node and generate blocks.  I made
the proof-of-work difficulty ridiculously easy to start with, so
for a little while in the beginning a typical PC will be able to
generate coins in just a few hours.  It'll get a lot harder when
competition makes the automatic adjustment drive up the difficulty.
Generated coins must wait 120 blocks to mature before they can be
spent.

There are two ways to send money.  If the recipient is online, you
can enter their IP address and it will connect, get a new public
key and send the transaction with comments.  If the recipient is
not online, it is possible to send to their Bitcoin address, which
is a hash of their public key that they give you.  They'll receive
the transaction the next time they connect and get the block it's
in.  This method has the disadvantage that no comment information
is sent, and a bit of privacy may be lost if the address is used
multiple times, but it is a useful alternative if both users can't
be online at the same time or the recipient can't receive incoming
connections.

Total circulation will be 21,000,000 coins.  It'll be distributed
to network nodes when they make blocks, with the amount cut in half
every 4 years.

first 4 years: 10,500,000 coins
next 4 years: 5,250,000 coins
next 4 years: 2,625,000 coins
next 4 years: 1,312,500 coins
etc...

When that runs out, the system can support transaction fees if
needed.  It's based on open market competition, and there will
probably always be nodes willing to process transactions for free.

Satoshi Nakamoto
```
On December 12, 2010, Satoshi Nakamoto published his final post on the Bitcoin forum, at which time the price of Bitcoin was hovering in the $0.30 range.

On February 9, 2011, the price of Bitcoin broke through $1 for the first time in history, achieving parity with the US dollar.

Satoshi's greatness absolutely does not lie in inventing some brand-new underlying cryptographic algorithm. Bitcoin actually uses almost no cutting-edge or complex cryptographic technology; Bitcoin does not use zero-knowledge proofs, blind signatures, homomorphic encryption, nor does it use group signatures, ring signatures, or any more advanced cryptographic primitives that had already appeared in the literature prior to 2008. Satoshi combined three widely available cryptographic building blocks (ECC keys, `ECDSA` signatures, and the `SHA-256` hash algorithm) together and integrated them into a single set of consensus rules. If you deconstruct Bitcoin, every single one of its underlying cryptographic and network components (`P2P` networking, public-key cryptography, elliptic curves, Merkle trees, timestamps, `PoW`, hash algorithms, programmable contracts, Byzantine fault tolerance, and digital cash theories) was an existing invention from predecessors.

Satoshi's true identity is that of an **unparalleled, top-tier system architect and a genius economist**. With extremely forward-looking engineering craftsmanship, he created mining, the `UTXO` ledger, halving incentives, longest-chain consensus, block headers, `SPV`, the mempool, address formats, non-Turing completeness, adaptive difficulty adjustments, and wallet prototypes, locking the technical components of predecessors precisely together like gears. Using selfish human nature as fuel and rigorous cryptography as boundaries, he allowed the Bitcoin system to completely break free from the organization and intervention of centralized human entities, moving toward an eternal, self-driven evolution. This engineering closed-loop has been flawless over the past dozen years and will remain so for an even longer future.

---
<sub>【Reading Notice】This article is a true record of the history of Satoshi Nakamoto and Bitcoin and will be continuously improved. Its value will eventually be proven by time, and it is destined to be collected and published. This article focuses on the history around Satoshi Nakamoto's retirement in 2011. After Satoshi left the stage, subsequent followers forked Bitcoin dozens of times, bringing a flurry of interest battles and chaos. Only by confirming the true identity of Satoshi Nakamoto can the orthodox Bitcoin be determined. Every number, time, person, and institution appearing in the text is fully verifiable with no fiction whatsoever. If you have doubts about the sources of the content, please conduct your own cross-searches. May mathematics and truth be with you.</sub>
