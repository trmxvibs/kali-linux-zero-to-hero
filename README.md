# Kali Linux Free Course

A free, open, beginner-to-advanced course in Linux, networking, and
ethical cybersecurity — built around one idea:

> Don't teach people how to run security tools. Teach them why the tools
> work, what problem they solve, how to interpret their output, and when
> they should NOT be used.

This is documentation first, tools second. Every lesson explains a concept
in plain language before introducing any command, and every lab runs
against systems built specifically for this purpose — never real,
unauthorized targets. See [Ethics & Legal Boundaries](docs/getting-started/ethics-and-legal.md).

## ⚠️ Project Status — Read This First

This repository is a **real, working foundation**, not a finished
30-module encyclopedia. Honestly:

- **Fully written**, following the course's complete lesson format (concepts,
  labs, commands, troubleshooting, security notes, exercises, challenge):
  Modules **00–12, 21, 22, 26** — i.e. the entire **Linux Fundamentals**
  track (00–07), **Networking** (08–09), **Security Fundamentals** (10),
  **Reconnaissance & Enumeration** (11–12), plus Automation and Lab-Building
- **Scaffolded** (README + checkpoint structure in place, lesson files are
  placeholders): the remaining modules — tracked in [ROADMAP.md](ROADMAP.md)
- **No video content is planned for the near term.** This is a deliberate,
  current decision — effort is going into deepening the written modules
  first (see [video/README.md](video/README.md)).
- **Actually tested**, not just written: every script in `scripts/bash/` and
  `scripts/python/`, and the labs attached to the completed modules above —
  see [tests/TEST_LOG.md](tests/TEST_LOG.md) for exactly what was run and
  what its output was, including the few systemd/cron commands (Module 07)
  that could only be verified against official documentation rather than
  live-executed, due to the build environment lacking a real `systemd` init.

This structure exists so contributors can extend the course module-by-module
using a proven template, rather than everyone guessing at format. See
[CONTRIBUTING.md](CONTRIBUTING.md).

## Who This Is For

- **Level 0:** You've never opened a terminal.
- **Level 1:** You know some Linux, want structured networking + sysadmin fundamentals.
- **Level 2:** You know Linux/networking, want a real security vocabulary before touching tools.
- **Level 3:** You want hands-on, legal, reproducible labs with Kali tools.
- **Level 4:** You want automation, methodology, and how to keep going after this course.

Start at Module 00 regardless of level — it's short, and it sets the ground rules for every lab that follows.

## Learning Path

| # | Module | Status |
|---|---|---|
| 00 | [Orientation](modules/00-orientation/README.md) | ✅ Complete |
| 01 | [Linux Fundamentals](modules/01-linux-fundamentals/README.md) | ✅ Complete |
| 02 | [Kali Linux Fundamentals](modules/02-kali-fundamentals/README.md) | ✅ Complete |
| 03 | [Terminal & Bash](modules/03-terminal-and-bash/README.md) | ✅ Complete |
| 04 | [Filesystem & Permissions](modules/04-filesystem-and-permissions/README.md) | ✅ Complete |
| 05 | [Users, Groups & Processes](modules/05-users-groups-processes/README.md) | ✅ Complete |
| 06 | [Package Management](modules/06-package-management/README.md) | ✅ Complete |
| 07 | [Services & System Administration](modules/07-services-and-sysadmin/README.md) | ✅ Complete |
| 08 | [Networking Fundamentals](modules/08-networking-fundamentals/README.md) | ✅ Complete |
| 09 | [Network Troubleshooting](modules/09-network-troubleshooting/README.md) | ✅ Complete |
| 10 | [Security Fundamentals](modules/10-security-fundamentals/README.md) | ✅ Complete |
| 11 | [Reconnaissance Concepts](modules/11-reconnaissance-concepts/README.md) | ✅ Complete |
| 12 | [Network Enumeration](modules/12-network-enumeration/README.md) | ✅ Complete |
| 13 | [Traffic Analysis](modules/13-traffic-analysis/README.md) | 🚧 Scaffold |
| 14 | [Web Security Fundamentals](modules/14-web-security-fundamentals/README.md) | 🚧 Scaffold |
| 15 | [Vulnerability Assessment](modules/15-vulnerability-assessment/README.md) | 🚧 Scaffold |
| 16 | [Authentication & Password Security](modules/16-authentication-and-passwords/README.md) | 🚧 Scaffold |
| 17 | [Defensive Security](modules/17-defensive-security/README.md) | 🚧 Scaffold |
| 18 | [Digital Forensics Fundamentals](modules/18-digital-forensics-fundamentals/README.md) | 🚧 Scaffold |
| 19 | [Wireless Security Concepts](modules/19-wireless-security-concepts/README.md) | 🚧 Scaffold |
| 20 | [Exploitation Concepts in Safe Labs](modules/20-exploitation-concepts-safe-labs/README.md) | 🚧 Scaffold |
| 21 | [Automation with Bash](modules/21-automation-with-bash/README.md) | ✅ Complete |
| 22 | [Security Automation with Python](modules/22-security-automation-with-python/README.md) | ✅ Complete |
| 23 | [CTF & Practice Methodology](modules/23-ctf-and-practice-methodology/README.md) | 🚧 Scaffold |
| 24 | [Vulnerability Research Fundamentals](modules/24-vulnerability-research-fundamentals/README.md) | 🚧 Scaffold |
| 25 | [Reporting Security Findings](modules/25-reporting-security-findings/README.md) | 🚧 Scaffold |
| 26 | [Building Your Own Security Lab](modules/26-building-your-own-lab/README.md) | ✅ Complete |
| 27 | [Advanced Kali Workflows](modules/27-advanced-kali-workflows/README.md) | 🚧 Scaffold |
| 28 | [Final Practical Projects](modules/28-final-practical-projects/README.md) | 🚧 Scaffold |
| 29 | [Career & Further Learning](modules/29-career-and-further-learning/README.md) | 🚧 Scaffold |

## Repository Structure

```text
kali-linux-free-course/
├── README.md, LICENSE, CONTRIBUTING.md, CODE_OF_CONDUCT.md,
│   SECURITY.md, ROADMAP.md, CHANGELOG.md
├── modules/                # the 30-module curriculum (this is the course)
├── docs/                   # glossary, ethics/legal, cross-cutting topics
├── labs/                   # shared lab data/fixtures used by module labs
├── scripts/
│   ├── bash/                # tested Bash utilities (Module 21)
│   └── python/               # tested Python utilities (Module 22)
├── exercises/               # (reserved for standalone exercise sets)
├── projects/                # (reserved for capstone/final projects)
├── resources/                # (reserved for curated external references)
├── assets/                   # images/diagrams/screenshots
├── tests/                    # validation scripts + the actual test log
└── video/                    # video/documentation mapping template
```

## Safety & Legal — Non-Negotiable

Every lab in this course uses systems you own or deliberately vulnerable
training software (Metasploitable, DVWA, Juice Shop, WebGoat) inside an
**isolated** virtual network (Module 26). Full policy:
[docs/getting-started/ethics-and-legal.md](docs/getting-started/ethics-and-legal.md).

Commands with real-world risk are always marked:

> ⚠️ **LAB ONLY** — Run this command only against systems you own or have explicit authorization to test.

## Contributing

This course is intentionally built to be extended by contributors, using
the exact format the completed modules already follow. See
[CONTRIBUTING.md](CONTRIBUTING.md) for the lesson format and how to submit
a new or improved module.

## FAQ

**Do I need a paid Kali/security course after this?** No — that's the point. If something here is unclear, that's a bug in the course, not a reason to pay for the same information elsewhere.

**Do I need real hardware?** No. A laptop that can run one or two virtual machines is enough (Module 02, Module 26).

**Is this legal to practice with?** Yes, as long as you stay inside your own isolated lab and the deliberately vulnerable training targets named above — see the ethics/legal document.

**Why aren't all 30 modules finished yet?** See "Project Status" above — this is an honest, incrementally-built open-source project, not a marketing claim.

## License

[MIT](LICENSE) for the course materials. Third-party tools and training applications retain their own licenses.
