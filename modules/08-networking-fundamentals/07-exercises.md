# Exercises — Module 08

1. Given a network `10.10.10.0/28`, how many usable host addresses does it have? Show your reasoning.
2. Explain in your own words why a TCP port scanner can determine "open" vs "closed" without ever completing a full application-level connection.
3. Run `dig` against two different domains and compare their `TTL` (time to live) values in the answer section — what does a low TTL suggest about how often that record might change?
4. On your own Kali VM, run `ss -tulpn` before and after starting an SSH server (`sudo systemctl start ssh`), and note the difference in output.

## Self-Check

You should be able to explain, without notes, the difference between an IP address and a port, and why NAT is not a security control.
