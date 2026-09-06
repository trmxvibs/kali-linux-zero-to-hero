# Lab 02 — Fresh Kali Verification

**Environment:** Your newly-installed Kali VM (Lesson 02.2).

## Steps

1. Confirm OS identity:
   ```bash
   cat /etc/os-release
   uname -a
   ```
2. Confirm your user and group memberships:
   ```bash
   whoami
   id
   ```
3. Update the system fully:
   ```bash
   sudo apt update
   sudo apt full-upgrade -y
   ```
4. Confirm a well-known security tool is pre-installed (it should be, on the standard Kali image):
   ```bash
   which nmap
   nmap --version
   ```
5. Take your `clean-updated-baseline` snapshot (Lesson 02.2, Step 6).

## Expected Result

- `/etc/os-release` shows `Kali GNU/Linux`
- `id` shows your user is a member of the `sudo` group
- `nmap --version` prints a version number without error
- A snapshot exists before you touch anything further

## Troubleshooting

See `05-troubleshooting.md`.

## Next Step

[Module 03 — Terminal & Bash](../03-terminal-and-bash/README.md)
