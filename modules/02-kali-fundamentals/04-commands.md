# Lesson 02.3 — First Commands on a Fresh Kali System

These build directly on Module 01 — nothing new syntactically, just applied to a fresh Kali install specifically.

## `uname -a`

**What/why:** Prints kernel name, version, and architecture — the fastest way to confirm what you're actually running.
```bash
uname -a
```
**Expected output (example):**
```
Linux kali 6.6.0-kali1-amd64 #1 SMP PREEMPT_DYNAMIC ... x86_64 GNU/Linux
```

## `lsb_release -a` / `cat /etc/os-release`

```bash
cat /etc/os-release
```
**Expected output (example):**
```
PRETTY_NAME="Kali GNU/Linux Rolling"
NAME="Kali GNU/Linux"
```
**Why it matters:** confirms exact OS identity — useful when following any tutorial or troubleshooting guide that's version-sensitive.

## `apt update && apt full-upgrade`

Covered in depth in Module 06 — the two commands you should run immediately and periodically:
```bash
sudo apt update
sudo apt full-upgrade -y
```

## `whoami` and `id`

```bash
whoami      # your username
id           # your username, UID, GID, and group memberships
```
**Reading `id` output:**
```
uid=1000(kali) gid=1000(kali) groups=1000(kali),27(sudo)
```
The `groups=` list matters immediately: membership in `sudo` (or `wheel` on some distros) is what lets a user run `sudo` at all — this is revisited in depth in Module 05.

## `sudo`

**What/why:** Runs a single command with elevated (root) privileges, instead of logging in as root directly — the standard, safer pattern on modern Kali.
```bash
sudo apt update
```
**Common mistake:** Running everything with `sudo` "just in case." Only elevate when a command actually needs it (e.g., installing packages, editing system config) — running your whole session as root defeats the least-privilege model Module 05 and Module 17 build on.

> ⚠️ Every `apt`/package command above modifies your own Kali VM only — no target/authorization concerns apply to these, unlike Module 11's active scanning commands.

## Further Reading

- [Kali Linux — Update, upgrade & distribution upgrade](https://www.kali.org/docs/general-use/updating-kali/)
