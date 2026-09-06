# Troubleshooting — Module 09

**`nc -l` works once, then subsequent connections fail** — this is expected, not a bug: by default `nc -l` exits after handling one connection. Start a new listener for each subsequent test (see the gotcha documented in `03-practical-lab.md`).

**`ping` fails but the layered checklist says everything else works** — many hosts and firewalls deliberately block ICMP; a failed `ping` alone never proves a host is down. Confirm with `nc -zv` against an actual expected-open port before concluding anything.

**`nc -zv` hangs for a long time instead of failing fast** — a "connection refused" happens quickly (the host actively said no); a hang usually means a firewall is silently dropping the packets rather than rejecting them — itself a meaningful, distinct diagnostic signal (Module 08/Module 17 revisit this from the defensive side).

**DNS resolution intermittently fails** — try a different, known-reliable DNS server temporarily (e.g., `dig @8.8.8.8 example.com`) to isolate whether the problem is your configured resolver specifically or something further upstream.
