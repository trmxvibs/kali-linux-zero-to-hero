# Lesson 17.2 — Defensive Commands

## System state check (Module 09 tools, reused with defensive intent)

```bash
ss -tulpn                        # what is actually listening right now?
ps aux                             # what is actually running?
who && last                          # who is or was logged in?
```

## Service audit

```bash
systemctl list-unit-files --state=enabled     # what starts at boot?
systemctl list-units --state=running            # what is running now?
```

## SUID/SGID audit (Module 04 command, defensive intent)

```bash
find / -perm -4000 -type f 2>/dev/null     # all SUID files
find / -perm -2000 -type f 2>/dev/null       # all SGID files
```

## Log investigation

```bash
journalctl -p err -b                             # errors from this boot
journalctl -u ssh --since today                    # SSH activity today
grep "Failed password" /var/log/auth.log             # failed login attempts
grep "Accepted" /var/log/auth.log                      # successful logins
last -F                                                   # login history with full timestamps
```

## File system changes

```bash
find / -newer /etc/passwd -type f 2>/dev/null         # files modified after passwd
find /tmp /var/tmp -type f 2>/dev/null                   # unexpected files in temp dirs
find / -perm -0002 -type f 2>/dev/null                     # world-writable files
```

## `ufw` — basic firewall (Uncomplicated Firewall)

> ⚠️ **Testing note:** `ufw` is a standard Kali tool, not available in this course's build sandbox.

```bash
sudo ufw status                  # current firewall state and rules
sudo ufw enable                    # activate the firewall
sudo ufw allow 22/tcp               # allow SSH inbound
sudo ufw deny 23/tcp                  # block Telnet
sudo ufw default deny incoming          # deny all inbound by default (enable first)
sudo ufw default allow outgoing
```

## Applying `log_analyzer.sh` (Module 21 — defensive usage)

```bash
./scripts/bash/log_analyzer.sh /var/log/auth.log "Failed password"
```
This already-built, already-tested tool from Module 21 is directly applicable here — defensive monitoring is one of the explicit use cases it was designed for.

## Further Reading

- [Debian — Securing Debian Manual](https://www.debian.org/doc/manuals/securing-debian-manual/)
- `man ufw`, `man journalctl`
