# Security Notes — Module 01

These fundamentals matter for security because:

- **File listing and permissions (`ls -la`)** is the first thing both attackers and auditors check on any system — misconfigured permissions are one of the most common real vulnerabilities (Module 04).
- **`ps aux` / process listing** is how you spot something that shouldn't be running — both as a defender doing a health check, and as an attacker doing situational awareness after gaining access (Module 17 covers the defensive side in depth).
- **`grep` on log files** (`/var/log/auth.log`, etc.) is the backbone of manual log analysis, long before you reach dedicated SIEM/analysis tooling (Module 13, Module 17).
- **`find -perm -4000`** (SUID discovery) is a standard privilege-escalation *and* hardening-audit step — the same command, two different intents, depending on who's authorized to run it and why.

> ⚠️ **LAB ONLY** — none of the commands in this module are dangerous by themselves, but running `find` or `grep` against systems you do not own to gather information about them without authorization is itself a form of unauthorized reconnaissance. Keep every exercise inside your own environment.
