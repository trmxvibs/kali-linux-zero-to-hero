# Security Notes — Module 05

- **Auditing for unexpected UID-0 accounts** (`awk -F: '$3 == 0 {print $1}' /etc/passwd` — tested during this course's build, correctly shows only `root` on a clean system) is a simple, real check for a classic backdoor technique: an attacker with root access creating a second account with UID 0, which then looks like an ordinary username but has full root privileges.
- **Overly broad `sudo` rules** (e.g., `ALL=(ALL) NOPASSWD: ALL` for a low-privilege account) are a common real-world misconfiguration found in security audits — always prefer the narrowest `sudo` grant that accomplishes the actual need.
- **Zombie processes** (`Z` state in `ps aux`) are usually benign but worth noticing in bulk — a parent process failing to clean up many children can itself indicate a bug or, rarely, something worth investigating further.

> ⚠️ Every account and process created in this module's lab is local, temporary, and cleaned up at the end — no other system is involved.
