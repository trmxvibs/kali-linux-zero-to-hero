# Troubleshooting — Module 08

**`dig: command not found`** — install with `sudo apt install dnsutils`.

**`ping` hangs forever** — you likely omitted `-c`; press `Ctrl+C` to stop it, then re-run with `-c 4`.

**`ping` fails but the site loads fine in a browser** — many hosts block ICMP (the protocol `ping` uses) while still serving normal traffic on other ports. A failed ping does not prove a host is unreachable — verify with `curl -I` on the actual service port/protocol instead.

**`ss -tulpn` shows no `Process` column info** — some process details require root; try `sudo ss -tulpn`.

**Confusing which IP is "yours"** — on a machine with multiple interfaces (e.g., a VM with both a NAT and a host-only adapter), run `ip addr show` and match the interface name to the network you expect to be using (Module 26 covers multi-adapter VM setups in depth).
