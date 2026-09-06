# Challenge — Module 21

Build a "Basic Recon Report Generator" script that combines concepts from Modules 08, 11, and 21:

- Takes a single IP address as an argument
- Runs `ping -c 2` and reports reachability
- If reachable, runs a conservative Nmap scan (`-T2 -sV`) against it
- Writes a combined, timestamped report to a file
- Uses proper exit codes: 0 if the report was generated, 1 if the argument was missing, 2 if the host was unreachable

> ⚠️ **LAB ONLY** — test this only against your own Metasploitable VM or localhost.
