# Roadmap

## Current State — v1.0 Complete

**All 30 modules are now fully written.** This is the first complete version
of the course — every module from 00 (Orientation) through 29 (Career &
Further Learning) has its full lesson content, practical lab, commands
reference, troubleshooting, security notes, exercises, and challenge.

See `README.md` for the complete status table.

**Tested:** see `tests/TEST_LOG.md` for the full inventory.
- Commands actually executed and verified: Modules 01–06, 09 (nc-based),
  10 (openssl), 12 (nc banner grab), 14 (sqli_demo.py, curl), 15
  (vuln_lookup.py), 16 (hashing_demo.py), 17 (find-based commands), 18
  (file/strings/stat/sha256sum against real sample evidence dataset)
- Documentation-only (no live execution): Modules 07, 08/09 networking
  commands, 12 (SMB/NSE), 13 (tcpdump/Wireshark), 16 (john/hashcat),
  19 (wireless), 20 (Metasploit) — all clearly flagged in their lessons

**Video:** not planned. See `video/README.md`.

## Maintenance Priorities

1. **Live-test the documentation-only modules** against a real Kali VM +
   Metasploitable lab — update `tests/TEST_LOG.md` from
   "documentation-verified" to "live-tested" for each one.
2. **Expand Module 14's web labs** with DVWA/Juice Shop alongside the
   existing from-scratch SQLi demonstration.
3. **CI automation** — run `tests/validate_links.py` and
   `tests/validate_structure.py` on every pull request.
4. **Community translations** — coordinate in issues before starting.

## How to Help

See `CONTRIBUTING.md`. The most useful contributions now:
- Real-hardware verification of Modules 07, 09, 12, 13, 19, 20
- New exercises or improved challenges for any module
- Typo fixes and clarity improvements
- New lab environments (DVWA, Juice Shop integration)
