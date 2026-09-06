# Exercises — Module 07

1. On your Kali VM, pick any service and determine, using only `systemctl`, whether it is (a) active and enabled, (b) active but not enabled, (c) enabled but not active, or (d) neither.
2. Explain why a security-conscious administrator would want to periodically run `systemctl list-unit-files --state=enabled` even on a system they believe they know well.
3. Write a valid crontab line that runs a script every day at 3:30 AM, and another that runs every Monday at 9:00 AM.
4. Find, using `journalctl`, the most recent failed SSH login attempt on your system (if any exist) — what unit did you query?
