# Lesson 11.1 — What Reconnaissance Actually Is

## Learning Objectives

- Explain passive vs. active reconnaissance
- Explain what a port scanner is actually doing (built on Module 08's TCP handshake)
- Understand why reconnaissance is the most legally sensitive phase of security testing
- Set up the lab target used for the rest of this module

## Prerequisites

Modules 01–10 completed, especially Module 08 (Networking) and Module 10 (Security Fundamentals).

## Concept

**Plain language:** Reconnaissance ("recon") is the information-gathering phase before any testing happens — figuring out what exists, what's reachable, and what's running, before deciding what (if anything) to test further.

**Technical:** Recon splits into two categories:

- **Passive recon** — gathering information without directly interacting with the target: WHOIS records, public DNS records, search engine results, certificate transparency logs, social media, job postings (which often leak internal tech stack details). The target never sees this traffic.
- **Active recon** — directly interacting with the target: port scanning, banner grabbing, sending crafted packets. The target's logs *can* show this traffic.

A **port scanner** (like `nmap`) automates the TCP handshake you learned in Module 08: it sends a SYN packet to a port and interprets the response:

```
SYN sent → SYN-ACK received  → port is OPEN
SYN sent → RST received      → port is CLOSED
SYN sent → no response       → FILTERED (likely a firewall dropping it silently)
```

This is why Module 08 had to come first — without understanding the handshake, "SYN scan" and "filtered" are just jargon.

## Why It Matters

Recon determines the entire rest of an assessment. A missed open port is a missed finding. An overly aggressive scan can crash a fragile service or trigger a client's incident response team unnecessarily — which is why scope and authorization (Module 00, Module 10) come before any tool.

## Common Mistakes

- Treating "filtered" and "closed" as the same thing — filtered usually means a firewall is present and silently dropping packets, which is itself useful information.
- Scanning aggressively (`-T5`, all 65535 ports, from the very start) against fragile or unknown targets instead of starting conservatively.
- Confusing "port is open" with "service is vulnerable" — an open port just means something is listening (Module 15 covers what comes next).

## Security Perspective — Attacker View vs Defender View

**Attacker view:** What's exposed? What can I learn without triggering alerts?
**Defender view:** What does *my own* attack surface look like from the outside? What would recon reveal about my organization that I didn't intend to expose (Module 17 revisits this)?

> ⚠️ **LAB ONLY** — this entire module (and Modules 12–20) uses a deliberately vulnerable target you control: **Metasploitable 2**, run in an isolated, host-only virtual network. Setup instructions are in `02-installation.md`.

## Exercise

Before touching any tool, write down: if you were defending a small company's public-facing web server, what are three pieces of information you'd want to know are (or aren't) discoverable about it via passive recon alone?

## Further Reading

- [Nmap Reference Guide (official)](https://nmap.org/book/man.html)
- [OWASP Testing Guide — Information Gathering](https://owasp.org/www-project-web-security-testing-guide/)
