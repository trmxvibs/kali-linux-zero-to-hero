# Lesson 08.2 — Networking Commands

## `ip addr show` (or `ip a`)

**What/why:** Shows every network interface and its assigned IP addresses. This is the modern replacement for the older `ifconfig`.

```bash
ip addr show
```
**Expected output (trimmed):**
```
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 ...
    inet 192.168.1.23/24 brd 192.168.1.255 scope global eth0
```
**Reading it:** `inet 192.168.1.23/24` is your IPv4 address and its CIDR prefix. `eth0` is the interface name (varies: `enp0s3`, `wlan0`, etc.).

**Common mistake:** Confusing the interface's assigned address with the network's broadcast address (`brd`) — you can't use the broadcast address as a normal host address.

---

## `ip route show`

```bash
ip route show
```
**Expected output:**
```
default via 192.168.1.1 dev eth0
192.168.1.0/24 dev eth0 scope link
```
**Reading it:** the `default via ...` line is your gateway (router) — where traffic goes when the destination isn't on your local subnet.

---

## `ping`

**What/why:** Sends ICMP echo requests to test basic reachability and measure latency.

```bash
ping -c 4 8.8.8.8
```
`-c 4` limits it to 4 packets (without `-c`, `ping` runs forever until you press Ctrl+C).

**Reading output:** `time=13.2 ms` is round-trip latency. `0% packet loss` in the summary means every request got a reply.

**Common mistake:** Assuming "ping fails = host is down." Many hosts and firewalls deliberately block ICMP while still running fully reachable services — a failed ping does not prove a host is offline.

> ⚠️ **LAB ONLY for anything beyond your own network** — pinging a host you don't control isn't dangerous, but treat scope the same as any other lab activity.

---

## `traceroute`

**What/why:** Shows the path (each router hop) packets take to a destination.

```bash
traceroute 8.8.8.8
```
**Reading output:** each numbered line is one hop; `* * *` means that hop didn't reply (often a firewall), not necessarily a broken path — later hops can still succeed.

---

## `dig` — DNS lookups

```bash
dig example.com
dig example.com +short      # just the answer, no verbose output
dig -x 8.8.8.8               # reverse lookup: IP to name
```
**Reading output:** the `ANSWER SECTION` shows the resolved IP address(es) and the record type (`A` for IPv4).

---

## `ss` — socket statistics

**What/why:** Modern replacement for `netstat`. Shows active connections and listening ports — this is a core defensive tool.

```bash
ss -tulpn
```
- `-t` TCP, `-u` UDP, `-l` listening sockets only, `-p` show the process, `-n` numeric ports (don't resolve service names)

**Expected output (trimmed):**
```
Netid State  Local Address:Port   Peer Address:Port  Process
tcp   LISTEN 0.0.0.0:22           0.0.0.0:*           users:(("sshd",pid=812,fd=3))
```
**Reading it:** `0.0.0.0:22` listening means SSH is accepting connections on *any* interface, port 22. This is the exact command a defender runs to answer "what's actually listening on this machine right now?" (Module 17).

---

## `curl -I`

```bash
curl -I https://example.com
```
Fetches only HTTP response headers — fast way to check a web server is responding and see its headers (Server, security headers, etc.) without downloading the page. Full coverage in Module 14.

## Further Reading

- `man ip`, `man ss`, `man dig`
- [RFC 1035 — DNS](https://www.rfc-editor.org/rfc/rfc1035)
