# Security Notes — Module 09

- The distinction between "connection refused" (fast, port closed) and "timeout" (likely firewalled/filtered) is not just a troubleshooting detail — it's the exact same distinction Nmap uses to report `closed` vs. `filtered` in Module 11. Learning to read it manually with `nc` here makes Module 11's scanner output far less mysterious.
- `nc` itself is a genuinely dual-use tool: the identical "connect to a port and send/receive raw data" capability used here for legitimate troubleshooting is also usable to manually interact with services during authorized testing (Module 12 onward) — same tool, and the same authorization rules from Module 00 apply the moment it's pointed at something you don't own.
- A host that responds to `nc -zv` on unexpected ports (services you didn't intentionally expose) is worth investigating from a defensive standpoint (Module 17) — this simple check is a real, cheap part of a self-audit.

> ⚠️ **LAB ONLY for anything beyond localhost/your own systems** — the port-checking techniques in this module are the same techniques covered by Module 00's authorization rules the moment they're pointed at a host you don't own.
