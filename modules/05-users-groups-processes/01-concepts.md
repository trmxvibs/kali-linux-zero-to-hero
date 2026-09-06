# Lesson 05.1 — Users, Groups, and Who Can Do What

## Learning Objectives

- Understand how Linux identifies users (UID) and groups (GID)
- Understand `/etc/passwd`, `/etc/shadow`, and `/etc/group`
- Understand primary vs. supplementary groups
- Understand `sudo` vs. `su` vs. root

## Prerequisites

Module 04 (permissions) — this module explains the *who* behind the owner/group permission model you just learned.

## Concept

**Plain language:** Every process and every file has an owner. Module 04 explained *what* owners and groups can do to a file; this module explains *how* users and groups themselves are defined and managed.

**Technical:**

### `/etc/passwd` — the user database

```bash
cat /etc/passwd | head -3
```
Each line: `username:x:UID:GID:comment:home_directory:shell`. The `x` in the password field means the actual (hashed) password lives elsewhere — `/etc/shadow` — not in this world-readable file. UID `0` is always root, regardless of username.

### `/etc/shadow` — the actual password data

Readable only by root; contains the hashed password and password-aging policy. This separation exists specifically so ordinary users can look up account info (via `/etc/passwd`, which many tools need to be world-readable) without being able to see anyone's password hash.

### `/etc/group` — group definitions

```bash
cat /etc/group | head -3
```
Each line: `groupname:x:GID:comma_separated_member_usernames`. A user's **primary group** is set in `/etc/passwd` (the GID field); **supplementary groups** are additional memberships listed in `/etc/group`.

### `sudo` vs `su` vs root

- **`sudo command`** — run one command as root (or another user), then return to your normal user. The modern, recommended pattern.
- **`su`** — switch users entirely for the rest of the session (`su -` switches to root with root's environment). Leaves you in an elevated state until you explicitly exit.
- **Being root directly (logging in as root)** — the old pattern, actively discouraged today; there's no "undo" if you make a mistake, and you lose the audit trail `sudo` provides (it logs who ran what).

## Why It Matters

Nearly every privilege-escalation technique (Module 20) ultimately targets this exact system: tricking a process into running as a different, more privileged UID than intended. Understanding UID/GID as the actual mechanism — not "permissions" as an abstract concept — is what makes SUID (Module 04) and sudo misconfigurations (Module 17) comprehensible rather than magical.

## Common Mistakes

- Assuming `/etc/passwd` contains real passwords — it hasn't, on any modern Linux system, in decades; that's what `/etc/shadow` is for.
- Treating `sudo` and "being root" as identical in risk — `sudo` at least logs and scopes the elevation; a permanent root shell doesn't.
- Adding a user to a group and expecting it to take effect in their *current* session — group membership changes apply to new logins/sessions, not retroactively to already-open shells.

## Security Perspective

- Auditing `/etc/passwd` for unexpected UID-0 accounts (anything besides `root` with UID `0`) is a real, simple defensive check — a second UID-0 account is a classic backdoor technique.
- Auditing `sudo` configuration (`/etc/sudoers`, via `visudo`) for overly broad rules (e.g., a user allowed to run *any* command as root with no password) is standard hardening practice (Module 17).

## Exercise

Before the lab, run `cat /etc/passwd | wc -l` on any Linux system you have and predict: are most of these real human user accounts, or something else? (Hint: look at the low UID numbers.)

## Further Reading

- `man 5 passwd`, `man 5 shadow`, `man 5 group`
- [Debian wiki — Users and Groups](https://wiki.debian.org/UserManagement)
