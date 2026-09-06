# Challenge — Module 12

Building on Module 21 (Bash automation), write a script `banner_grab.sh` that:
- Takes a target host and a list of ports (e.g., `21 22 25 80`)
- For each port, attempts a banner grab with a short timeout using `nc`
- Prints a clean summary: port number, whether a banner was received, and the banner text if any
- Handles unreachable/closed ports gracefully (per Module 09's connection-refused vs. timeout distinction) rather than hanging

Test it against your own Kali VM's own open ports first (localhost), then — with authorization — against your Metasploitable VM.
