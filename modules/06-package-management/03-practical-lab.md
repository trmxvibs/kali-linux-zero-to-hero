# Lab 06 — Package Investigation

**Environment:** Any Debian-based system (Kali VM recommended). No internet needed for most of this lab except step 1.

## Steps

1. Refresh your package index (requires internet):
   ```bash
   sudo apt update
   ```
2. Count how many packages are currently installed on your system:
   ```bash
   dpkg -l | grep "^ii" | wc -l
   ```
3. Check whether a specific tool (e.g., `nmap`) is installed, and if not, install it:
   ```bash
   dpkg -l | grep nmap || sudo apt install -y nmap
   ```
4. List every file `nmap` installed:
   ```bash
   dpkg -L nmap | head -20
   ```
5. Pick one file from that list and confirm `dpkg -S` correctly reports it belongs to `nmap`:
   ```bash
   dpkg -S /usr/bin/nmap
   ```
6. Check if any upgrades are available without installing them yet:
   ```bash
   apt list --upgradable
   ```
7. Clean up: if you installed `nmap` just for this lab and don't want to keep it, remove it — otherwise, leave it (you'll want it for Module 11 anyway):
   ```bash
   sudo apt remove nmap    # optional
   ```

## Expected Result

Step 5 should print something like `nmap: /usr/bin/nmap`, confirming the file-to-package lookup works — this exact command was verified during this course's build (with `bash` as the test package instead of `nmap`, since the build sandbox has no internet to install new packages).

## Next Step

[Module 07 — Services & System Administration](../07-services-and-sysadmin/README.md)
