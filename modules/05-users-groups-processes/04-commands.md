# Lesson 05.2 — User, Group, and Process Commands

## `useradd`, `usermod`, `userdel`

```bash
sudo useradd -m alice              # create user 'alice' with a home directory (-m)
sudo usermod -aG sudo alice         # add alice to the 'sudo' group (-a = append, don't replace existing groups!)
sudo userdel -r alice                # delete alice AND her home directory (-r)
```
> ⚠️ **`usermod -G` without `-a` REPLACES all of a user's supplementary groups** — always use `-aG` (append) unless you specifically intend to wipe existing memberships. This is a well-known, easy-to-make mistake.

## `groupadd`, `groupdel`

```bash
sudo groupadd developers
sudo groupdel developers
```

## `id` and `groups`

```bash
id alice                # UID, GID, and all group memberships for alice
groups alice              # just the group names
```

## `passwd`

```bash
sudo passwd alice          # set/change alice's password (prompts interactively)
```

## `sudo` and `visudo`

```bash
sudo whoami                 # run a single command as root
sudo -l                      # list what commands you're allowed to run with sudo
sudo visudo                   # safely edit /etc/sudoers (validates syntax before saving)
```
**Never edit `/etc/sudoers` directly with a normal text editor** — a syntax error can lock out `sudo` entirely; `visudo` checks syntax before committing.

## `ps aux`

**Expected output columns:** USER, PID, %CPU, %MEM, VSZ, RSS, TTY, STAT, START, TIME, COMMAND.
**Reading `STAT`:** `S` sleeping, `R` running, `Z` zombie (finished but not yet cleaned up by its parent — worth investigating if you see many), `T` stopped.

## `kill`, signals, and job control

```bash
sleep 300 &          # run in background, "&" returns control to the shell immediately
jobs                  # list background jobs in this shell
kill %1                # kill job number 1 (as shown by `jobs`)
kill 1234               # send SIGTERM (default, "please stop") to PID 1234
kill -9 1234              # send SIGKILL (cannot be caught or ignored — last resort)
fg                        # bring the most recent background job to the foreground
```
**Tested and confirmed during this course's build:** a plain `kill` cleanly stops a `sleep` process; `kill -9` immediately removes it with no cleanup opportunity — both verified by checking `ps` before and after.

## `top` / `htop`

```bash
top             # live view, press 'q' to quit
htop            # nicer interactive version (may need: sudo apt install htop)
```

## Further Reading

- `man useradd`, `man usermod`, `man sudo`, `man 7 signal`
