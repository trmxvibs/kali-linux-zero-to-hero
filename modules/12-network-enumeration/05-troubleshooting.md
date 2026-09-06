# Troubleshooting — Module 12

**`nc <target> <port>` connects but shows nothing** — not every service sends a banner immediately; some wait for you to send something first (try pressing Enter, or sending a protocol-appropriate request like `HEAD / HTTP/1.0\r\n\r\n` for a web server).

**`smbclient -L` asks for a password despite `-N`** — some SMB configurations reject anonymous listing entirely; this itself is useful enumeration information (anonymous access is disabled), not a failure of your command.

**`enum4linux` output is overwhelming** — start by grepping for specific sections you care about (e.g., `enum4linux -a <target> | grep -A5 "Share Enumeration"`) rather than reading the entire dump at once.

**NSE scripts report "ERROR" or timeout** — some scripts need specific conditions (a particular port state, a specific service) to run at all; confirm the target port matches what the script expects, and that basic connectivity works first (Module 09's checklist).

**Nothing works and you suspect the VM isn't isolated correctly** — stop, and re-verify Module 26's isolation checklist before continuing; don't troubleshoot enumeration issues that are actually networking/isolation issues.
