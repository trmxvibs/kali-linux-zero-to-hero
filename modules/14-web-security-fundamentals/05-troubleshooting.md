# Troubleshooting — Module 14

**`python3 -m http.server` says "Address already in use"** — another process is already using that port; pick a different port number (`python3 -m http.server 8124`) or find and stop the other process (Module 05's `ps`/`kill`).

**SQL injection payload "doesn't work" as expected** — read `03-practical-lab.md`'s Part 3 carefully: SQL syntax details (like operator precedence and comment markers) matter enormously, and a payload that looks right can silently fail for a subtle reason. Print the exact constructed query (as the demo script does) to see precisely what's being sent.

**`curl -I` shows no `Server` header** — some servers deliberately omit or genericize this header as a hardening measure (Module 17) — this is a defender doing exactly what this lesson suggests, not a broken command.

**Following along in a browser instead of `curl` and not seeing headers** — use the browser's Developer Tools (F12) → Network tab, then click any request to see its full headers, which `curl -I` only shows in the terminal.
