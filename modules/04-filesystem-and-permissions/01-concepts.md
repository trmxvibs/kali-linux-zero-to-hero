# Lesson 04.1 — Permissions, Bit by Bit

## Learning Objectives

- Decode an `ls -l` permission string completely
- Understand the owner/group/other model
- Understand numeric (octal) permission notation
- Understand `umask`, SUID, SGID, and the sticky bit

## Prerequisites

Module 01 (basic `ls`/`chmod` exposure), Module 05 concepts help but aren't required yet — users/groups are explained fully in Module 05.

## Concept

**Plain language:** Every file and directory on Linux has three questions answered for three different audiences: can the **owner**, the **group**, and **everyone else** read it, write it, and execute it? That's the entire permission model — nine yes/no answers, displayed as ten characters.

**Technical — decoding `ls -l`:**

```
-rwxr-xr--  1 kali kali 220 Sep 1 10:00 script.sh
```

| Position | 1 | 2-4 | 5-7 | 8-10 |
|---|---|---|---|---|
| Meaning | file type | owner | group | other |
| Value | `-` (regular file) | `rwx` | `r-x` | `r--` |

- File type: `-` regular file, `d` directory, `l` symlink
- `r` = read, `w` = write, `x` = execute (for a directory, `x` means "can enter it / traverse it," not "run" it)
- A dash (`-`) in any position means that permission is denied for that audience

So `-rwxr-xr--` means: owner can read/write/execute; group can read/execute (not write); others can only read.

### Numeric (octal) notation

Each `rwx` triplet maps to a number: `r=4, w=2, x=1`, summed.

| Triplet | Sum | Meaning |
|---|---|---|
| `rwx` | 7 | read+write+execute |
| `rw-` | 6 | read+write |
| `r-x` | 5 | read+execute |
| `r--` | 4 | read only |
| `---` | 0 | nothing |

`-rwxr-xr--` becomes **754** (owner=7, group=5, other=4) — this is why `chmod 754 file` and `chmod u=rwx,g=rx,o=r file` produce the identical result.

### `umask`

New files don't start at `777`/`666` by default — `umask` subtracts permissions at creation time. The default umask (often `022`) is why new files typically come out as `644` (rw-r--r--) and new directories as `755` (rwxr-xr-x).

### SUID, SGID, and the Sticky Bit

Three special bits, shown as an extra character in `ls -l`:

- **SUID** (`chmod u+s`) — an executable runs with the *file owner's* privileges, not the invoking user's. Shown as a lowercase `s` in the owner's execute position when the owner-execute bit is also set (e.g., `-rwsr-xr-x`), or an **uppercase `S`** if SUID is set but owner-execute is *not* set (e.g., `-rwSr--r--` — a real, easy-to-verify distinction, not a typo). This is how `passwd` lets a normal user change their own password despite `/etc/shadow` being writable only by root.
- **SGID** (`chmod g+s`) — similar, but for the group; on a directory, it makes new files inherit the directory's group instead of the creating user's primary group.
- **Sticky bit** (`chmod +t`) — on a directory, restricts deletion so only the file's owner (or root) can delete/rename files inside it, even if others have write access to the directory. `/tmp` uses this — otherwise any user could delete any other user's temp files.

## Why It Matters

Misconfigured permissions are one of the most common real-world vulnerabilities — a world-writable configuration file, an SUID binary that shouldn't be SUID, or a private key readable by every user on the system. Module 20 (Exploitation Concepts) revisits SUID specifically as a classic privilege-escalation vector, and this lesson is the prerequisite for understanding why it works at all.

## Common Mistakes

- Confusing directory execute (`x`) with "run" — for directories, `x` means "can `cd` into it / access files inside by name," which trips up people expecting it to mean something like "double-click to open."
- Setting `chmod 777` on something "just to make an error go away" — this is a defensive anti-pattern; find the *actual* needed permission instead of opening everything to everyone.
- Confusing SUID (`s` in the owner slot) with a directory's execute bit being literally lowercase `x` — read the position carefully.

## Security Perspective — Attacker View vs Defender View

**Attacker:** Are there SUID binaries that shouldn't be SUID? Is a sensitive file world-readable? (`find / -perm -4000` from Module 01, revisited with real intent in Module 20.)
**Defender:** Audit your own systems for the same thing, proactively, on a schedule — this is one of the cheapest, highest-value hardening habits (Module 17).

## Exercise

Before the lab, convert `-rw-r-----` to its octal equivalent by hand, and explain what audience has what access.

## Further Reading

- `man chmod`, `man umask`
- [Linux Filesystem Permissions (Debian wiki)](https://wiki.debian.org/Permissions)
