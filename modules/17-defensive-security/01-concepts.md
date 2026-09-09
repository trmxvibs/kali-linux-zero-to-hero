# Lesson 17.1 — Defending the System You've Been Learning to Understand

## Learning Objectives

- Apply the "attacker view" from Modules 11–16 as a defender's checklist
- Understand Linux hardening as a set of concrete, actionable practices
- Understand log analysis as a detection skill, not just a troubleshooting one
- Understand the basic incident-response workflow

## Prerequisites

Modules 01–16 (this is the defensive synthesis of everything before it).

## Concept

**Plain language:** Every technique in Modules 11–16 has a mirror image. Reconnaissance (Module 11) has an answer: reduce your attack surface and information exposure. Enumeration (Module 12) has an answer: disable unnecessary services and remove anonymous access. Traffic analysis (Module 13) has an answer: use encrypted protocols. Web vulnerabilities (Module 14) have answers: parameterized queries, input validation, security headers. The pattern is consistent — understanding how something is found or exploited is exactly what tells you how to prevent or detect it.

**Technical — an "Attacker View → Defender Action" framework:**

| What an attacker/tester does | What a defender does in response |
|---|---|
| Port scan — finds open services (Module 11) | Run `ss -tulpn` regularly; close anything not deliberately needed |
| Banner grab — reads exact version info (Module 12) | Update software (Module 06); consider suppressing verbose version banners |
| Enumerate SMB/FTP — finds anonymous access (Module 12) | Disable anonymous access; audit share permissions |
| Traffic capture — reads plaintext credentials (Module 13) | Enforce encrypted protocols (HTTPS, SFTP, SSH instead of Telnet/FTP) |
| SQL injection — bypasses authentication (Module 14) | Use parameterized queries; least-privilege DB accounts |
| Password cracking — cracks weak/unsalted hashes (Module 16) | Use bcrypt/Argon2; enforce strong password policy; enable MFA |
| SUID binary abuse — escalates privileges (Module 04) | Audit SUID files: `find / -perm -4000 -type f 2>/dev/null` |

### The Core Hardening Habits (Priority-ordered)

1. **Keep software updated** — a known, unpatched vulnerability (Module 15) is the single most common real-world attack vector
2. **Close unnecessary services** — `systemctl disable` anything not actively needed
3. **Enforce least privilege** — users, processes, and services should have the minimum access they actually need (Module 05, Module 07)
4. **Monitor logs** — `journalctl`, `/var/log/auth.log`, and the Bash automation from Module 21 (`log_analyzer.sh`) are all you need to start
5. **Enable MFA** where possible (Module 16)
6. **Audit SUID/SGID binaries** and file permissions (Module 04) periodically

### Basic Incident Response Workflow

If you suspect something is wrong:

```
1. Don't panic and don't immediately reboot — you might destroy evidence
2. Identify: ps aux, ss -tulpn, last, who — what's running, what's connected?
3. Contain: isolate the affected system from the network if possible
4. Preserve: take a snapshot (Module 26) if in a VM; hash key files (Module 18)
5. Analyze: logs (journalctl, auth.log), changed files (find with -newer), new users
6. Remediate: fix the root cause, not just the symptom
7. Document: write down what you found and what you did (Module 25)
```

## Why It Matters

Offensive skills without defensive context produce people who can find problems but not explain or fix them. Every future employer, client, or colleague will expect you to answer "so how do we fix it?" — this module is that answer.

## Common Mistakes

- Treating hardening as a one-time event rather than an ongoing practice — new vulnerabilities appear constantly (Module 15), and a hardened system at deployment gets stale quickly.
- Disabling all logging "for performance" — logs are your only evidence of what happened, and their absence is itself evidence of tampering.
- Treating "we have a firewall" as complete security — defense in depth (Module 10) means no single control is sufficient.

## Security Perspective

This entire module *is* the security perspective — every section is the defender's answer to the previous modules' attacker techniques. The same tools (`ss`, `ps`, `grep` on logs) used for troubleshooting throughout the course are the primary instruments of defensive monitoring.

## Exercise

Using only tools from Modules 01–09, produce a "baseline report" for your own Kali VM: currently listening ports, running services, logged-in users, and recent failed login attempts (from `journalctl` or `/var/log/auth.log`). This is a real, legitimate self-audit — the same process defenders do on real systems.

## Further Reading

- [CIS Benchmarks (Linux)](https://www.cisecurity.org/cis-benchmarks) — industry-standard hardening guidelines
- [NIST SP 800-123 — Guide to General Server Security](https://csrc.nist.gov/pubs/sp/800/123/final)
