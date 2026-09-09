# Changelog

## [0.7.0] — Defensive Security, Forensics, Wireless & Exploitation

### Added
- Fully written Module 17 (Defensive Security): attacker-view →
  defender-action framework, Linux hardening habits priority-ordered,
  basic incident-response workflow
- Fully written Module 18 (Digital Forensics Fundamentals): integrity-first
  principle, `file` magic-byte detection, timestamp analysis, `strings`
  extraction — all commands actually executed in the build sandbox; a
  sample evidence dataset (`labs/digital-forensics/sample-evidence/`)
  was built and every lab step run against it, including the `binary_stub`
  which was rebuilt twice after an initial implementation (escaped null
  bytes) produced one-line `strings` output; the corrected Python-built
  version correctly produces multi-line output
- Fully written Module 19 (Wireless Security Concepts): WEP/WPA2/WPA3
  protocol history and weakness analysis, monitor mode, offline dictionary
  attack mechanics — documented from official 802.11 and aircrack-ng
  documentation; not live-tested (no wireless hardware in build sandbox)
- Fully written Module 20 (Exploitation Concepts in Safe Labs): Metasploit
  methodology, vulnerability→exploitable→impact framework, Metasploitable
  2 lab workflow — documented from official Metasploit documentation; not
  live-tested (no Metasploit/Metasploitable in build sandbox)

### Changed
- README status table: Modules 17–20 now marked Complete
- ROADMAP updated: entire core technical curriculum (00–22, 26) now written
- TEST_LOG.md updated with Module 17–20 testing details

## [0.6.0] — Web Security, Vulnerability Assessment & Password Security

### Added
- Fully written Module 14 (Web Security Fundamentals): HTTP request/response
  anatomy, cookies/sessions, and a real, fully-tested SQL injection
  demonstration (`labs/web-security/sqli_demo.py`) showing both the
  vulnerable string-concatenation pattern and the parameterized-query fix
  actually working against each other
- Fully written Module 15 (Vulnerability Assessment): CVE/CWE vocabulary,
  a real worked example (vsftpd 2.3.4 / CVE-2011-2523, fact-checked via
  web search against multiple sources), and a runnable local vulnerability
  lookup tool (`labs/vulnerability-assessment/vuln_lookup.py`)
- Fully written Module 16 (Authentication & Password Security): why fast
  hashes are unsuitable for password storage, salting, and a fully-tested
  demonstration script (`labs/password-security/hashing_demo.py`) proving
  each claim with real, executed code rather than assertion
- A genuine testing catch in Module 14: an initial lab draft assumed the
  payload `' OR '1'='1` would dump an entire table; actually running it
  revealed SQL operator precedence (`AND` binds tighter than `OR`) made
  that assumption wrong, and the lab was rewritten around the corrected,
  tested behavior rather than the original (incorrect) assumption

### Changed
- README status table, ROADMAP, and TEST_LOG updated to reflect Modules
  14–16 and the next priority (Modules 17–20)

## [0.5.0] — Traffic Analysis

### Added
- Fully written Module 13 (Traffic Analysis): capture vs. display filters,
  `tcpdump` and Wireshark/`tshark` usage, plaintext vs. encrypted traffic
  visibility
- `tcpdump`/Wireshark/`tshark` commands documented from official
  documentation, explicitly flagged as not live-tested since the build
  sandbox has no packet-capture tools installed and no network access
  (checked directly: `tcpdump`, `tshark`, and Python's `scapy`/`dpkt`
  libraries are all absent)

### Changed
- README status table, ROADMAP, and TEST_LOG updated to reflect Module 13
  and the next priority (Modules 14–20)

## [0.4.0] — Network Enumeration

### Added
- Fully written Module 12 (Network Enumeration): banner grabbing, Nmap NSE
  scripts, SMB enumeration (`smbclient`, `enum4linux`), NFS enumeration
  (`showmount`)
- The core banner-grabbing technique was actually tested locally (a
  simulated service via `nc`, confirming the connect-and-read mechanic)
  before being applied conceptually to real services in the lab
- `smbclient`/`enum4linux`/`showmount`/NSE-script commands documented from
  official tool documentation, explicitly flagged as not live-tested since
  the build sandbox has no Metasploitable VM or network access

### Changed
- README status table, ROADMAP, and TEST_LOG updated to reflect Module 12
  and the next priority (Modules 13–20)

## [0.3.0] — Networking Troubleshooting & Security Fundamentals

### Added
- Fully written Module 09 (Network Troubleshooting): a layered diagnostic
  method, with every `nc`-based port-connectivity example actually executed
  during this build — including a genuine gotcha discovered by testing
  (`nc -l` only accepts one connection before exiting, which the lab uses
  as a deliberate teaching moment rather than hiding it)
- Fully written Module 10 (Security Fundamentals): CIA triad,
  vulnerability/exploit/threat/risk, authentication vs. authorization,
  defense in depth, least privilege, attack surface — plus a hands-on
  cryptography lab (hashing, symmetric, and asymmetric encryption via
  `openssl`) with every command actually executed and verified, including
  a wrong-password decryption failure case
- Modules 00–11 now form a complete, tested conceptual and Linux/networking
  foundation ahead of the hands-on Kali tool modules (12–20)

### Changed
- README status table, ROADMAP, and TEST_LOG updated to reflect the new
  completions and the next priorities (Modules 12–20)

## [0.2.0] — Linux Fundamentals Complete

### Added
- Fully written Modules 02–07, completing the entire Linux Fundamentals
  track (00–07): Kali Fundamentals, Terminal & Bash, Filesystem &
  Permissions, Users/Groups & Processes, Package Management, Services &
  System Administration
- Every command and lab in Modules 02–06 actually executed and verified
  during this build, including several real nuances caught by testing
  (e.g., SUID showing uppercase `S` vs lowercase `s` depending on the
  execute bit; `dpkg -S` requiring a resolved path, not a symlink)
- Module 07 documented and cross-checked against official `systemd`/`cron`
  documentation; explicitly flagged as not live-tested since the build
  environment lacks a real `systemd` init — see `tests/TEST_LOG.md`

### Changed
- README status table updated: Modules 02–07 now marked Complete
- `video/README.md` updated to state plainly that no video production is
  planned for the near term (a deliberate decision, not an oversight)
- `ROADMAP.md` near-term priorities re-ordered now that Linux Fundamentals
  is complete

## [0.1.0] — Initial Release

### Added
- Full repository structure: 30-module curriculum, docs, labs, scripts,
  tests, video mapping template
- Fully written modules: 00 (Orientation), 01 (Linux Fundamentals),
  08 (Networking Fundamentals), 11 (Reconnaissance Concepts),
  21 (Automation with Bash), 22 (Security Automation with Python),
  26 (Building Your Own Security Lab)
- Scaffolded structure for all remaining 23 modules
- Tested Bash scripts: `system_info_collector.sh`, `log_analyzer.sh`
- Tested Python scripts: `file_hash_generator.py`, `log_parser.py`
- Core governance docs: README, LICENSE (MIT), CONTRIBUTING, CODE_OF_CONDUCT,
  SECURITY, ROADMAP
- `docs/getting-started/ethics-and-legal.md` and `docs/glossary.md`
- Validation tooling in `tests/`
- Fabricated sample log fixture for log-analysis labs (`labs/log-analysis/sample.log`)

### Known Limitations
- 23 of 30 modules are scaffolds pending full content (see ROADMAP.md)
- No labs have been reproduced against a real Kali VM / real Metasploitable
  VM / real DVWA-Juice Shop-WebGoat instance — see `tests/TEST_LOG.md` for
  exactly what has and hasn't been verified
- Video course mapping is a template only; no videos exist yet
