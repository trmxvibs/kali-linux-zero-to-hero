# Lab 05 — Managing a User End to End

**Environment:** Your Kali VM or any Linux system where you have `sudo`.

> ⚠️ This lab creates and deletes a **local test account only** — nothing here touches any other system.

## Steps

1. Create a test user with a home directory:
   ```bash
   sudo useradd -m labuser
   sudo passwd labuser
   ```
2. Confirm the account exists and inspect its default group:
   ```bash
   id labuser
   grep labuser /etc/passwd
   ```
3. Create a group and add `labuser` to it correctly (append, don't replace):
   ```bash
   sudo groupadd labgroup
   sudo usermod -aG labgroup labuser
   id labuser
   ```
4. Confirm the append behavior by adding a second group and checking that the first one wasn't lost:
   ```bash
   sudo groupadd labgroup2
   sudo usermod -aG labgroup2 labuser
   id labuser
   ```
   `labuser` should now show **both** `labgroup` and `labgroup2`.
5. Start a background process, find its PID, and terminate it:
   ```bash
   sleep 120 &
   ps aux | grep "sleep 120" | grep -v grep
   kill <PID-from-above>
   ```
6. Clean up the test account:
   ```bash
   sudo userdel -r labuser
   sudo groupdel labgroup
   sudo groupdel labgroup2
   ```

## Expected Result

Step 4's `id labuser` output should list both `labgroup` and `labgroup2` in the `groups=` section — if only the second one appears, you (or a previous step) forgot the `-a` flag, which is exactly the mistake this lab is designed to make obvious.

## Next Step

[Module 06 — Package Management](../06-package-management/README.md)
