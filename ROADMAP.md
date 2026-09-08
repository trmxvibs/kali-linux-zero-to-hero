# Roadmap

## Current State (this release)

**Fully written modules:** 00–16, 21, 22, 26 — i.e. the complete **Linux
Fundamentals** track (00–07), **Networking** (08–09), **Security
Fundamentals** (10), and **Reconnaissance through Password Security**
(11–16), plus Automation and Lab-Building. See `README.md` for the
complete status table.

**Scaffolded modules:** 17–20 and 23–29 have their `README.md` and
standard file structure in place; lesson content is a placeholder pending
contribution, following the format in `CONTRIBUTING.md`.

**Tested:** every script in `scripts/bash/` and `scripts/python/`, plus
the new `labs/web-security/sqli_demo.py`,
`labs/vulnerability-assessment/vuln_lookup.py`, and
`labs/password-security/hashing_demo.py` — all actually run, including a
real gotcha caught by testing in Module 14's SQL injection lab (an
operator-precedence nuance that made an initial payload assumption wrong,
corrected after actually running it) — see `tests/TEST_LOG.md`. Notable
exceptions requiring a real environment: Module 07's `systemctl`/`cron`,
Module 09's `ip`/`ping`/`dig`, Module 12's SMB/NFS/NSE tools, Module 13's
`tcpdump`/Wireshark, and Module 16's `john`/`hashcat`/`bcrypt` (none
installed in the build sandbox) — all flagged clearly in their own
lessons and in `tests/TEST_LOG.md`.

**Video:** not planned for the near term — this is a deliberate current
decision, not a gap. See `video/README.md`.

## Near-Term Priorities

1. Complete Modules 17–20 (Defensive Security, Digital Forensics, Wireless
   Security, Exploitation Concepts) — the remaining hands-on/conceptual
   modules building on Module 26's lab.
2. Reproduce Module 14's web lab against DVWA/Juice Shop/WebGoat directly,
   in addition to the local from-scratch demonstration already included.
3. Verify Module 07, 09, 12, 13, and 16's tool-dependent commands against
   a real Kali VM + Metasploitable lab, and update `tests/TEST_LOG.md`
   from "documentation-verified" to "live-tested" once done.
4. Complete Modules 23–29 (CTF methodology through career guidance) once
   the hands-on tool modules exist for them to build on.

## Medium-Term

- Populate `projects/` with the "Realistic Projects" progression described
  in the course design (network discovery, traffic analysis, web app
  assessment, capstone report).
- Populate `video/course-map.md` with actual video numbers once video
  production begins — the mapping template and required columns already
  exist.
- Expand `scripts/bash/` and `scripts/python/` with the remaining utilities
  named in Modules 21/22 (network info collector, port monitor, HTTP header
  analyzer, URL validator, DNS info tool, basic lab-only port scanner).

## Long-Term

- Community translations
- A second full pass ("Beginner Review" and "Security Professional Review",
  as described in the project's original design brief) once all modules are
  content-complete
- CI automation running `tests/validate_links.py` and
  `tests/validate_structure.py` on every pull request

## How to Help

See [CONTRIBUTING.md](CONTRIBUTING.md). Picking up a single scaffolded
module and bringing it to the same standard as Module 01 or Module 08 is
the single most useful contribution right now.
