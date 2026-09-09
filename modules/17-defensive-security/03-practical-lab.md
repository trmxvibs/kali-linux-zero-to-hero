# Lab 17 — Self-Auditing Your Own Kali VM

**Environment:** Your Kali VM. This lab has no external target — it's entirely self-directed against your own system.

## Steps

1. **Listening port audit:**
   ```bash
   ss -tulpn
   ```
   List every port shown. For each, answer: do I know what this service is, and should it be listening?

2. **Service boot-time audit:**
   ```bash
   systemctl list-unit-files --state=enabled
   ```
   Identify any enabled service you don't recognize or don't intentionally need.

3. **SUID binary audit:**
   ```bash
   find / -perm -4000 -type f 2>/dev/null
   ```
   For at least three results, look up (via `man` or `dpkg -S`) why that binary legitimately needs SUID — e.g., `passwd` (Module 04/05), `sudo`, `su`.

4. **Log review:**
   ```bash
   ./scripts/bash/log_analyzer.sh /var/log/auth.log "Failed password"
   ```
   Report: how many failed attempts are there? Are any IPs repeated?

5. **World-writable file check:**
   ```bash
   find / -perm -0002 -type f 2>/dev/null | grep -v /proc | head -20
   ```
   Identify any world-writable files that seem unexpected.

6. **Write a one-paragraph "security posture note"** from what you found — not a formal report (that's Module 25), just a plain-language summary of: one thing that's configured correctly, and one thing you'd change or investigate further.

## Expected Result

A self-assessment you can refer back to. There's no single "correct" answer — the quality measure is whether you can explain the reason for what you found, not just list it.

## Next Step

[Module 18 — Digital Forensics Fundamentals](../18-digital-forensics-fundamentals/README.md)
