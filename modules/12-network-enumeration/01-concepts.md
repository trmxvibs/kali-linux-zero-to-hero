# Lesson 12.1 — From "What's Open" to "What's Actually There"

## Learning Objectives

- Distinguish enumeration from the reconnaissance covered in Module 11
- Understand banner grabbing as a concept
- Understand what service enumeration reveals: versions, configurations, sometimes usernames/shares
- Know which Module 12 tools map to which common services

## Prerequisites

Module 11 (Reconnaissance Concepts) — enumeration is the deeper, more detailed follow-up to a scan's initial results.

## Concept

**Plain language:** Module 11's Nmap scan tells you *that* port 445 is open and *maybe* what's running there. Enumeration means going further into that specific service: what shares does it expose? What version exactly, down to the patch level? Does it leak usernames? Enumeration is the difference between "there's a door" and "the door has three locks, here's their brand, and one of them has a known bypass."

**Technical — banner grabbing**, the simplest enumeration technique: many services announce their own identity when you connect, before you've even sent a real request.

```bash
nc <target> 22
```
An SSH server will typically respond immediately with a line like `SSH-2.0-OpenSSH_8.9p1`. **Tested and confirmed during this course's build**, using a local test service — connecting with plain `nc` and reading the first line returned is exactly how banner grabbing works, no special tool required, just Module 09's `nc` applied with enumeration intent instead of troubleshooting intent.

### Common services and what enumerating them reveals

| Port/Service | What enumeration might reveal |
|---|---|
| 21 (FTP) | Anonymous login allowed? Version? Directory listing? |
| 22 (SSH) | Exact version (banner), sometimes supported auth methods |
| 80/443 (HTTP/S) | Full tech stack — covered in depth in Module 14 |
| 139/445 (SMB) | Shared folders, sometimes usernames, OS version |
| 3306 (MySQL) | Version banner, sometimes whether auth is required at all |

### Why enumeration is riskier than a basic scan

Enumeration typically involves *more* interaction with a service than a simple port scan — sending real protocol-level requests, sometimes attempting anonymous/guest access. This means more chances to disrupt a fragile service, and it's a more clearly "active testing" activity than a scan — the authorization bar (Module 00) applies just as firmly, but the *stakes* of getting scope wrong are higher.

## Why It Matters

Vulnerability assessment (Module 15) depends entirely on knowing *exactly* what's running — not "some web server" but "Apache 2.2.8, unpatched since 2010." Enumeration is what produces that specificity.

## Common Mistakes

- Assuming a banner is always accurate — some administrators deliberately change or hide version banners (a technique called banner obfuscation), so a missing or generic banner doesn't necessarily mean nothing is there.
- Treating enumeration output as a finding by itself — "SMB shares are listable" is a fact; whether it's a *problem* depends on what's actually shared and who can reach it (Module 15 territory).
- Running enumeration tools with default/aggressive settings against fragile lab targets without first trying a conservative approach.

## Security Perspective — Attacker View vs Defender View

**Attacker:** What can I learn about this service beyond "it's open"? Are there default credentials, anonymous access, or informative error messages?
**Defender:** What does *my* service reveal to someone doing exactly this? Banner obfuscation and disabling anonymous access are both real, common hardening steps (Module 17).

> ⚠️ **LAB ONLY** — this entire module (and Modules 13–20) continues to use your isolated Metasploitable VM from Module 26.

## Exercise

Before the lab, predict what you'd expect an anonymous FTP login attempt to reveal on a *properly configured* production FTP server, versus a deliberately vulnerable one like Metasploitable.

## Further Reading

- [OWASP Testing Guide — Information Gathering](https://owasp.org/www-project-web-security-testing-guide/)
- [Nmap Scripting Engine (NSE) documentation](https://nmap.org/book/nse.html)
