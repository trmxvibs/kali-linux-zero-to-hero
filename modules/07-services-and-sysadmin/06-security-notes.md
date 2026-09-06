# Security Notes — Module 07

- **Reviewing your actual running/enabled service footprint** (`systemctl list-units --state=running`, `list-unit-files --state=enabled`) is one of the simplest, most direct ways to answer "what's my attack surface, really?" — an unused service you forgot about is exactly the kind of thing an attacker (or an auditor) finds first.
- **Logs (`journalctl`) are a primary defensive tool.** Reviewing service logs for unexpected restarts, failed authentication attempts, or unusual activity is standard practice, covered further in Module 17.
- **Cron jobs are a documented persistence technique.** An attacker who gains access sometimes adds a cron job to maintain access even after their original foothold is fixed — periodically reviewing `crontab -l` (for your user) and system-wide cron locations (`/etc/cron.d/`, `/etc/crontab`) for unrecognized entries is a real, simple check.

> ⚠️ Everything in this module manages services and schedules on your own system — no other host is involved.
