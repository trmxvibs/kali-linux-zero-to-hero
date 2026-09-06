# Challenge — Module 09

Write a small Bash script `port_check.sh` (building on Module 21) that:
- Takes a host and a port as arguments
- Uses `nc -zv` internally
- Prints a clear, plain-English verdict: "open", "closed (connection refused)", or "no response (possibly filtered — timed out after Ns)"
- Uses a sensible timeout (don't let it hang forever on a filtered port)
- Returns a distinct exit code for each of the three outcomes

Test it against a definitely-open port (something listening locally), a definitely-closed port, and — if you have access to a firewalled host — a filtered one.
