# Lesson 06.2 — Package Commands

## `apt update` / `apt upgrade` / `apt full-upgrade`

```bash
sudo apt update              # refresh package index — always run this first
sudo apt upgrade              # upgrade installed packages
sudo apt full-upgrade -y        # upgrade + resolve any package changes needed
```

## `apt install` / `apt remove` / `apt purge`

```bash
sudo apt install nmap            # install a package (and dependencies)
sudo apt remove nmap               # remove it, keep config files
sudo apt purge nmap                  # remove it AND its config files
sudo apt autoremove                    # clean up now-unneeded dependency packages
```

## `apt search` and `apt show`

```bash
apt search "port scanner"       # search package names/descriptions
apt show nmap                     # detailed info about a specific package
```

## `apt-cache policy`

**What/why:** Shows installed vs. candidate (available) version — useful for confirming whether an update is actually available before you upgrade.
```bash
apt-cache policy bash
```
**Expected output shape (tested during this course's build):**
```
bash:
  Installed: 5.2.21-2ubuntu4
  Candidate: 5.2.21-2ubuntu4
  Version table:
 *** 5.2.21-2ubuntu4 500
```
**Reading it:** if `Installed` and `Candidate` differ, an upgrade is available.

## `dpkg -l`, `dpkg -L`, `dpkg -S`

```bash
dpkg -l                      # list ALL installed packages
dpkg -l | grep nmap            # check if a specific package is installed
dpkg -L nmap                    # list every FILE a package installed
dpkg -S /usr/bin/bash             # find which package owns a given file
```
**Tested and confirmed during this course's build:** `dpkg -S` needs the file's *real* path — if the path you give is a symlink (e.g. `/bin/bash` on systems where it's a symlink to `/usr/bin/bash`), resolve it first with `realpath` or query the real path directly, or `dpkg -S` will report "no path found."

## `apt list --installed`

```bash
apt list --installed          # similar info to dpkg -l, in a different format
apt list --upgradable           # what has updates available
```

## Further Reading

- `man apt`, `man dpkg`
