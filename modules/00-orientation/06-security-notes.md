# Lesson 00.2 — The Rules That Apply to the Entire Course

> ⚠️ **Read this before Module 01.** These rules apply to every lab, every script, and every tool in this repository — they are not repeated in full elsewhere, only referenced.

## The One Rule

**Only test systems you own, or systems you have explicit, documented, written authorization to test.**

"It looked open" is not authorization. "I was just curious" is not authorization. A friend saying "sure, go ahead" over chat, for a system they don't own or control, is not authorization either.

## What Counts as a Safe Target in This Course

Every lab in this repository uses one of the following:

- A virtual machine you created and control (e.g., your own Kali VM, your own Metasploitable VM)
- Software deliberately published as an intentionally vulnerable training target: **OWASP Juice Shop, DVWA, WebGoat, Metasploitable 2/3**, or similar
- Your own home network hardware, where you are the owner/administrator
- `localhost` / a host-only or NAT virtual network with no route to the internet or to systems you don't control

If a lesson ever asks you to point a tool at anything else, that is a bug in the course — please open an issue.

## Why Isolation Matters (Not Just Legality)

Beyond the legal reason, an isolated lab network protects you from two very real risks:

1. **Accidental scope creep** — a scan or exploit meant for your lab VM hitting your home router, your neighbor's Wi-Fi, or a shared network at school/work.
2. **Damaging the very thing you're learning from** — intentionally vulnerable apps like DVWA are *fragile by design*. Running the wrong tool against the wrong host, or forgetting which VM is which, is the most common way beginners cause real (if minor) legal exposure by accident.

Module 26 ("Building Your Own Security Lab") teaches you how to build a network where this mistake is close to impossible.

## Responsible Disclosure (If You Ever Find a Real Vulnerability)

If, in the course of learning, you discover a real vulnerability in software or a service you do *not* own:

- Do not exploit it beyond the minimum needed to confirm it exists
- Do not access, copy, or modify data that isn't yours
- Report it through the vendor's official security contact or a recognized program (e.g., a bug bounty platform)
- Never demand payment as a condition of disclosure — that can cross into extortion
- When in doubt, don't act — read Module 25 (Reporting) and Module 24 (Vulnerability Research Fundamentals) first, and consult a lawyer if the situation is ambiguous

See `docs/getting-started/ethics-and-legal.md` for the full policy document.

## What This Course Will Never Ask You to Do

- Attack a system you don't own or lack authorization for
- Steal, guess, or crack real people's credentials
- Deploy anything resembling real malware
- Bypass authentication on a live, third-party service
- Deny service to a real system
- Evade detection for malicious purposes

Any command with real-world risk is marked:

> ⚠️ **LAB ONLY** — Run this command only against systems you own or have explicit authorization to test.

If you ever see a lesson in this repository that seems to violate its own rules, that's a documentation bug — please report it via `CONTRIBUTING.md`.
