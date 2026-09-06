# Troubleshooting — Module 07

**"System has not been booted with systemd as init system"** — you're in an environment (often a container) where `systemd` isn't PID 1; this module's lab needs a real Kali VM, not a minimal container. This exact message was encountered and documented during this course's build — see `tests/TEST_LOG.md`.

**"Disabled" a service but it's still running** — `disable` only affects *future* boots; you also need `stop` to affect the current running state (Lesson 07.1's core distinction).

**`journalctl` shows nothing for a unit** — confirm the unit name is exact (`systemctl list-units` to check spelling), and that the service has actually been started at least once since the last boot/journal rotation.

**`crontab -e` opens an unfamiliar editor** — it uses your `$EDITOR` environment variable, or a system default (often `nano` on Kali); set `export EDITOR=nano` (or your preferred editor) if the default is unfamiliar.

**Cron job "isn't running"** — check `/var/log/syslog` or `journalctl -u cron` for cron's own logs, and confirm your crontab syntax with `crontab -l` — a stray typo in the schedule fields is the most common cause.
