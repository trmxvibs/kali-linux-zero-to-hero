# Lab 04 — Hands-On Permission Bits

**Environment:** Any Linux terminal.

## Steps

1. Create a practice file and set it to `754` two different ways, confirming they match:
   ```bash
   mkdir -p ~/lab04 && cd ~/lab04
   touch script.sh
   chmod 754 script.sh
   ls -l script.sh
   chmod u=rwx,g=rx,o=r script.sh
   ls -l script.sh
   stat -c "%a" script.sh
   ```
2. Check your current umask, then create a file and directory and confirm their default permissions match what the umask predicts:
   ```bash
   umask
   touch defaultfile.txt
   mkdir defaultdir
   ls -ld defaultfile.txt defaultdir
   ```
3. Set SUID on a file that has no execute bit yet, and observe the uppercase `S`:
   ```bash
   touch suiddemo
   chmod u+s suiddemo
   ls -l suiddemo
   ```
   Now add execute and observe it become lowercase `s`:
   ```bash
   chmod u+x suiddemo
   ls -l suiddemo
   ```
4. Create a directory, set the sticky bit, and observe the `t` at the end of the permission string:
   ```bash
   mkdir stickytest
   chmod +t stickytest
   ls -ld stickytest
   ```
5. Search your own home directory for anything world-writable (a common misconfiguration to check for):
   ```bash
   find ~ -perm -0002 -type f 2>/dev/null
   ```

## Expected Result

Step 1's two `ls -l` outputs should be identical, and `stat -c "%a"` should print `754`.
Step 3 should show `-rwSr--r--` before adding execute, and `-rwsr--r--` after — this exact behavior was verified during this course's build.

## Cleanup

```bash
cd ~ && rm -rf ~/lab04
```

## Next Step

[Module 05 — Users, Groups & Processes](../05-users-groups-processes/README.md)
