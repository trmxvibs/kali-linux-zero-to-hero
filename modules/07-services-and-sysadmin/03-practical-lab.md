# Lab 07 — Controlling a Real Service

**Environment:** Your Kali VM (this lab requires a real `systemd` system — it will not work in most containers/sandboxes; see the note in `04-commands.md`).

## Steps

1. Check SSH's current state (it's installed by default on most Kali images, even if not running):
   ```bash
   systemctl status ssh
   ```
   Note both the `Loaded:` (enabled/disabled) and `Active:` (running/stopped) lines.
2. Start it, and re-check:
   ```bash
   sudo systemctl start ssh
   systemctl is-active ssh
   ```
3. Enable it so it survives a reboot, and confirm:
   ```bash
   sudo systemctl enable ssh
   systemctl is-enabled ssh
   ```
4. Look at its logs:
   ```bash
   journalctl -u ssh --since today
   ```
5. Demonstrate the enable/active distinction from `01-concepts.md` directly: stop it (without disabling) and confirm it's disabled-from-boot-perspective is unaffected:
   ```bash
   sudo systemctl stop ssh
   systemctl is-active ssh        # should show "inactive"
   systemctl is-enabled ssh         # should still show "enabled"
   ```
6. Create a simple personal cron job that appends a timestamp to a file every minute, let it run twice, then remove it:
   ```bash
   crontab -e
   # add this line, save, and exit:
   # * * * * * /bin/date >> /tmp/cron_test.log
   ```
   Wait ~2 minutes, then:
   ```bash
   cat /tmp/cron_test.log
   crontab -e     # remove the line you added
   rm /tmp/cron_test.log
   ```

## Expected Result

Step 5 is the key checkpoint: **active=inactive, enabled=enabled** — proving these are genuinely independent states, not two views of the same fact.

## Next Step

You've completed Linux Fundamentals (Modules 01–07). Continue to [Module 08 — Networking Fundamentals](../08-networking-fundamentals/README.md) if you haven't already, or [Module 09 — Network Troubleshooting](../09-network-troubleshooting/README.md).
