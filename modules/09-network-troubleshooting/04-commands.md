# Lesson 09.2 — Troubleshooting Commands

> ⚠️ **Testing note:** `ip`, `ping`, and `dig` require a real network stack this course's build sandbox doesn't have (see `tests/TEST_LOG.md` — same limitation noted in Module 08). `nc` (netcat) **was** available and every `nc` example below was actually executed and its exact output captured.

## Step 1-2: Interface and gateway (from Module 08, applied here)

```bash
ip addr show           # confirm you have an IP at all
ip route show            # find your default gateway
ping -c 2 <gateway-ip>     # can you reach it?
```

## Step 3: DNS resolution

```bash
dig example.com +short
```
No output / `NXDOMAIN` / timeout at this step, while step 2 succeeded, isolates the problem to DNS specifically — not general connectivity.

## Step 4: Direct IP reachability (bypassing DNS)

```bash
ping -c 2 93.184.216.34      # use a known IP directly, skipping name resolution entirely
```
If this works but step 3 didn't, you've confirmed the network path is fine and the problem is purely DNS.

## Step 5: Port-level connectivity — `nc -zv`

**What/why:** `ping` only tells you a *host* responds; it says nothing about whether a specific *service* is listening. `nc -z` (zero-I/O mode) attempts a real TCP connection to a specific port without sending data — the most direct way to answer "is this port actually open?"

```bash
nc -zv <host> <port>
```

**Tested and confirmed during this course's build**, against a real local listener:
```
$ nc -zv -w 2 localhost 8888
Connection to localhost (127.0.0.1) 8888 port [tcp/*] succeeded!
```
against a closed port:
```
$ nc -zv -w 2 localhost 44444
nc: connect to localhost (127.0.0.1) port 44444 (tcp) failed: Connection refused
```
**Reading it:** "succeeded" = a service accepted the TCP handshake (Module 08) on that port. "Connection refused" = nothing is listening there — the host *itself* is reachable (this is a fast, immediate refusal, not a timeout), it's specifically that port with nothing behind it. A *timeout* instead of a fast refusal usually means a firewall is silently dropping the packets — a third, distinct outcome worth telling apart from both of the above.

## Step 6: Application-layer check

```bash
curl -I http://<host>              # is HTTP actually responding correctly?
nc <host> <port>                    # manually send/receive raw data, for protocols curl doesn't speak
```

## Further Reading

- `man nc`, `man ping`, `man dig`
- [RFC 793 — TCP](https://www.rfc-editor.org/rfc/rfc793) (background on what a "handshake" and "refused" connection actually mean at the protocol level)
