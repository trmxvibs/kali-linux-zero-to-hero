# Lesson 01.2 — Core Commands

Every command below follows the same breakdown: what it is, why it exists, how it works, basic usage, example, expected output, how to read it, common mistakes, and troubleshooting. Security implications are covered where relevant; full security context is in `06-security-notes.md`.

---

## `pwd` — print working directory

**What/why:** Shells track a "current directory." Since you can't see it visually like a file explorer, `pwd` tells you where you are.

```bash
pwd
```
**Expected output:** `/home/kali`
**Reading it:** This is an absolute path from `/`.

---

## `ls` — list directory contents

**What/why:** Shows what's in a directory. The single most-used command in Linux.

**Basic usage:**
```bash
ls -la
```
- `ls` — list files
- `-l` — "long" format: permissions, owner, size, modified date
- `-a` — include hidden files (those starting with `.`)

**Expected output:**
```
drwxr-xr-x  5 kali kali 4096 Sep  1 10:03 .
drwxr-xr-x 20 root root 4096 Aug 30 09:00 ..
-rw-r--r--  1 kali kali  220 Aug 30 09:00 .bash_logout
drwxr-xr-x  2 kali kali 4096 Sep  1 09:50 Documents
```
**Reading it:** First column is permissions (Module 04 explains this fully); then owner, group, size in bytes, modified date, and name.

**Common mistake:** Forgetting `-a` and assuming a directory is empty when it only contains hidden config files.

---

## `cd` — change directory

```bash
cd Documents      # relative path
cd /etc           # absolute path
cd ..             # up one level
cd ~              # home directory
cd -              # previous directory
```
**Common mistake:** Confusing `cd ..` (up one level) with `cd .` (stay here — usually a no-op, but relevant in scripts).

---

## `mkdir`, `touch`, `cp`, `mv`, `rm`

```bash
mkdir project        # create a directory
touch notes.txt       # create an empty file (or update its timestamp if it exists)
cp notes.txt backup.txt        # copy
mv backup.txt project/         # move (also used to rename)
rm project/backup.txt          # delete a file
rmdir project                  # delete an EMPTY directory
rm -r project                  # delete a directory and its contents — no undo
```

> ⚠️ **`rm -r` has no trash bin.** There is no confirmation and no recycle bin. Double-check the path before pressing enter, especially with `sudo`.

---

## `cat`, `less`, `head`, `tail`

```bash
cat file.txt          # print the whole file
less file.txt          # scroll through a file page by page (press q to quit)
head -n 5 file.txt     # first 5 lines
tail -n 5 file.txt     # last 5 lines
tail -f /var/log/syslog  # follow a file live as new lines are appended
```
**Why it matters for security:** `tail -f` on a log file is one of the most common ways to watch activity happen in real time — covered again in Module 17 (Defensive Security).

---

## `grep` — search text

**What/why:** Finds lines matching a pattern. Used constantly for filtering log files, command output, and source code.

```bash
grep "failed" /var/log/auth.log
grep -i "error" app.log       # -i = case-insensitive
grep -r "TODO" ./project      # -r = recursive through a directory
```
**Expected output:** the matching lines, printed as-is.
**Common mistake:** Forgetting that `grep` matches *substrings* by default — searching for `cat` will also match `concatenate`.

---

## `find` and `locate`

```bash
find /home -name "*.txt"          # search live, by name, under a directory
find / -perm -4000 2>/dev/null    # find SUID files (security-relevant, see below)
locate passwd                      # search a pre-built index (faster, may be outdated)
```
**Security note:** `find / -perm -4000` locates SUID binaries — programs that run with the file owner's privileges (often root) regardless of who runs them. This is a standard step in both privilege-escalation research and system hardening audits. It is safe to *run* (read-only), but understanding *why* a result matters requires Module 05 and Module 20.

---

## `which` and `whereis`

```bash
which python3     # shows the exact executable that would run
whereis python3    # shows binary, source, and man page locations
```

---

## `chmod` and `chown`

Covered in full in Module 04. Quick reference:

```bash
chmod 644 file.txt        # owner: read/write, group/others: read
chmod +x script.sh        # make a file executable
chown kali:kali file.txt  # change owner:group
```

---

## `ps`, `top`, `kill`

```bash
ps aux              # list all running processes
top                  # live, updating view of processes and resource usage
kill 1234            # ask process 1234 to terminate (SIGTERM)
kill -9 1234         # force-kill (SIGKILL) — last resort
```
**Reading `ps aux`:** columns include USER, PID (process ID), %CPU, %MEM, and COMMAND. The PID is what you pass to `kill`.

**Common mistake:** Reaching for `kill -9` immediately. `SIGKILL` doesn't let the process clean up (close files, save state) — try plain `kill` first.

---

## `systemctl` and `journalctl`

```bash
systemctl status ssh        # is the ssh service running?
systemctl start ssh
systemctl stop ssh
systemctl enable ssh        # start automatically on boot
journalctl -u ssh -f        # follow logs for the ssh service live
```
Full coverage in Module 07 (Services & System Administration).

---

## `ip` and `ss`

```bash
ip addr show          # show network interfaces and IP addresses
ip route show          # show routing table
ss -tulpn              # show listening TCP/UDP ports and the process using each
```
Full coverage in Module 08 (Networking Fundamentals) — this is where the security relevance (open ports, listening services) becomes important.

---

## `curl` and `wget`

```bash
curl -I https://example.com          # fetch just the HTTP headers
curl https://example.com             # fetch and print the page body
wget https://example.com/file.zip    # download a file
```
Revisited heavily in Module 14 (Web Security Fundamentals).

---

## `tar` and `gzip`

```bash
tar -czvf archive.tar.gz myfolder/   # compress a folder
tar -xzvf archive.tar.gz              # extract
gzip file.txt                          # compress a single file to file.txt.gz
gunzip file.txt.gz                     # decompress
```

---

## `apt`

Covered fully in Module 06 (Package Management).

```bash
sudo apt update          # refresh the list of available packages
sudo apt upgrade         # install available updates
sudo apt install nmap    # install a specific package
```

## Further Reading

- `man <command>` for any command above — the man page is always the authoritative reference
- [GNU Coreutils manual](https://www.gnu.org/software/coreutils/manual/coreutils.html)
