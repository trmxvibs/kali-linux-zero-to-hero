# Security Notes — Module 02

- Keeping Kali updated (`apt update && apt full-upgrade`) isn't just good hygiene — Kali ships real, working security tools, and outdated versions of *those* can themselves have vulnerabilities or bugs affecting your results.
- Never download Kali images from anywhere except `kali.org` — a modified/backdoored "Kali" image is a realistic and documented risk vector; always verify checksums where the official site provides them.
- The default non-root user model (Module 02.1) exists specifically so that a mistake in one tool doesn't automatically have full system privileges — don't casually work around it by `sudo su`-ing into a permanent root shell for convenience.

> ⚠️ Nothing in this module involves testing any other system — every command targets your own Kali VM.
