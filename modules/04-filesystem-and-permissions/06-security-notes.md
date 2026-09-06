# Security Notes — Module 04

- **SUID binaries are a classic privilege-escalation target.** If an SUID-root binary can be manipulated into running arbitrary commands (e.g., via a shell escape, or by pointing it at attacker-controlled input), the attacker inherits root privileges. Module 20 covers this as a controlled, lab-only exercise. Auditing your own systems with `find / -perm -4000` periodically is a legitimate, valuable defensive habit (Module 17).
- **World-writable files/directories** are a common, boring, and very real vulnerability — a config file or script that anyone can modify is a path to privilege escalation or persistence for an attacker who's gained any foothold at all.
- **The sticky bit on `/tmp`** exists specifically so that a multi-user (or multi-process) system doesn't let one user delete or tamper with another's temporary files — a small but genuine security control baked into a directory most people never think about.

> ⚠️ Everything in this module operates on files you own, in your own environment — no external target is involved.
