# Changelog

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
