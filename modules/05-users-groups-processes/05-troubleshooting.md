# Troubleshooting — Module 05

**`usermod -G` wiped a user's other group memberships** — you forgot `-a` (append); re-add the missing groups with `usermod -aG`.

**"sudo: command not found" or "user is not in the sudoers file"** — the account isn't a member of the `sudo` group (Debian/Kali) — an existing admin needs to run `usermod -aG sudo <user>`.

**Password change doesn't seem to apply** — confirm you're editing the account you think you are; `passwd` with no argument changes *your own* password, `sudo passwd <user>` changes someone else's.

**Group membership change "isn't working"** — remember it applies to new sessions, not your currently open shell; log out and back in, or use `newgrp <groupname>` to pick it up immediately in the current shell.

**`kill` doesn't stop a process** — plain `kill` sends SIGTERM, which a process *can* ignore or handle specially; escalate to `kill -9` (SIGKILL, which cannot be ignored) only if the process genuinely doesn't respond.
