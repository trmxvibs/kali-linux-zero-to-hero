# Roadmap

## Current State (this release)

**Fully written modules:** 00–22, 26 — the complete course from
**Linux Fundamentals** (00–07) through **Networking** (08–09), **Security
Fundamentals** (10), **Reconnaissance through Exploitation** (11–20),
**Automation** (21–22), and **Lab-Building** (26). The entire core
technical curriculum is now written. See `README.md` for the complete
status table.

**Remaining scaffolds:** Modules 23–25 (CTF Methodology, Vulnerability
Research, Reporting) and 27–29 (Advanced Workflows, Final Projects, Career
Guidance) — structures in place, content pending.

**Tested:** see `tests/TEST_LOG.md`. Module 18's forensics commands
(`file`, `strings`, `stat`, `sha256sum`) and the sample evidence dataset
were fully live-tested. Notable not-live-tested areas: Module 07
(`systemctl`/`cron`), Modules 08–09 (`ip`/`ping`/`dig`), Module 12
(SMB/NFS/NSE), Module 13 (`tcpdump`/Wireshark), Module 16
(`john`/`hashcat`/`bcrypt`), Module 19 (wireless hardware), Module 20
(Metasploit/Metasploitable) — all flagged in their own lessons.

**Video:** not planned for the near term. See `video/README.md`.

## Near-Term Priorities

1. Complete Modules 23–25 (CTF methodology, vulnerability research,
   reporting) — they build on the now-complete technical foundation.
2. Complete Modules 27–29 (advanced workflows, final projects, career).
3. Verify tool-dependent modules against a real Kali VM + Metasploitable.
4. Expand Module 14 web labs with DVWA/Juice Shop alongside the existing
   from-scratch local demonstration.

## Medium-Term

- Community translations
- CI automation running `tests/validate_links.py` and
  `tests/validate_structure.py` on every pull request
- A full "Beginner Review" pass once all modules are content-complete

## How to Help

See `CONTRIBUTING.md`. The most needed contributions right now are:
Modules 23–25 and 27–29, and real-hardware verification of Modules 07,
09, 12, 13, 16, 19, and 20.
