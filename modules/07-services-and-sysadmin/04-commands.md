# Lesson 07.2 — Service and Scheduling Commands

> ⚠️ **Testing note:** the exact output shapes below are based on official `systemd`/`cron` documentation and man pages, consistent with standard Debian/Kali behavior. Unlike most of this course's command references, these specific commands were **not executed live** during this course's build — the sandbox used to build this course does not run `systemd` as PID 1 (a common situation in containers) and returned `"System has not been booted with systemd as init system"` when tested. See `tests/TEST_LOG.md`. Verify against your own Kali VM, which does run systemd normally.

## `systemctl status`

```bash
systemctl status ssh
```
**Expected output shape:**
```
● ssh.service - OpenBSD Secure Shell server
     Loaded: loaded (/lib/systemd/system/ssh.service; enabled; vendor preset: enabled)
     Active: active (running) since ...
```
**Reading it:** `Loaded: ... enabled` tells you it will start at boot. `Active: active (running)` tells you it's running right now. These are the two independent facts from `01-concepts.md` — both are on this one output for convenience.

## `systemctl start` / `stop` / `restart` / `reload`

```bash
sudo systemctl start ssh          # start it now
sudo systemctl stop ssh            # stop it now
sudo systemctl restart ssh          # stop then start (brief downtime)
sudo systemctl reload ssh            # re-read config without dropping connections, where supported
```

## `systemctl enable` / `disable`

```bash
sudo systemctl enable ssh          # will start automatically at next boot
sudo systemctl disable ssh          # will NOT start automatically at next boot
```
> ⚠️ **`enable`/`disable` do not affect whether the service is running right now** — combine with `start`/`stop` if you want to change both current and future state. This is the single most common point of confusion covered in `01-concepts.md`.

## `systemctl is-active` / `is-enabled`

```bash
systemctl is-active ssh        # prints "active" or "inactive" — good for scripts
systemctl is-enabled ssh         # prints "enabled" or "disabled"
```

## `systemctl list-units` / `list-unit-files`

```bash
systemctl list-units --type=service --state=running     # what's actually running right now
systemctl list-unit-files --state=enabled                  # what's set to start at boot
```
**Defensive use case (Module 17 revisits this):** periodically reviewing `list-unit-files --state=enabled` against what you *expect* to be enabled is a simple, real hardening check.

## `journalctl`

```bash
journalctl -u ssh                # all logs for the ssh unit
journalctl -u ssh -f                # follow live, like `tail -f`
journalctl -u ssh --since today       # only today's entries
journalctl -p err -b                    # only error-priority-or-higher entries, current boot
```

## `crontab`

```bash
crontab -l                # list your own scheduled jobs
crontab -e                 # edit your own scheduled jobs (opens your default editor)
sudo crontab -u root -l      # list root's scheduled jobs (needs sudo to view another user's)
```
**Crontab line format:** `minute hour day-of-month month day-of-week command`
```
0 2 * * *  /home/kali/scripts/backup.sh      # run daily at 2:00 AM
*/15 * * * * /home/kali/scripts/check.sh       # run every 15 minutes
```

## Further Reading

- `man systemctl`, `man journalctl`, `man 5 crontab`
- [systemd unit files — official documentation](https://www.freedesktop.org/software/systemd/man/systemd.unit.html)
