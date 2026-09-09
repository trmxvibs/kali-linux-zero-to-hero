# Troubleshooting — Module 17

**`find / -perm -4000` is very slow** — it's scanning the entire filesystem; `2>/dev/null` suppresses permission errors but the search still takes time; restrict to `/usr /bin /sbin /opt` if you want a faster partial result.

**`ufw status` shows "inactive"** — `ufw` is installed but not enabled; `sudo ufw enable` activates it (but do this deliberately — enabling it with default-deny rules before allowing SSH will lock you out of SSH if that's how you're connected).

**`journalctl` says "No entries"** — confirm the service name is correct (`systemctl status <service>` first), or broaden to `journalctl --since today` without a specific `-u` filter.

**`log_analyzer.sh` reports 0 matches on auth.log** — confirm the file path exists (`ls /var/log/auth.log`); on some Kali configurations, auth logging is handled by `journalctl` rather than written to a flat file.
