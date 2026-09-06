# Lesson 08.1 — How Networks Actually Work

## Learning Objectives

- Explain IP addresses, ports, and the difference between them
- Explain the TCP three-way handshake vs. UDP
- Explain DNS resolution end to end
- Explain private vs. public addresses and NAT
- Read a basic subnet/CIDR notation

## Prerequisites

Module 01–07 (you should be comfortable with the terminal and `ip`/`ss` commands from Module 01).

## Concept

### Addresses: how a computer is found

**Plain language:** An IP address is like a street address for a computer — it says *where* on a network something is. A MAC address is more like a serial number burned into your network card — it identifies a specific piece of hardware on the *local* network segment, not the wider internet.

**Technical:** IPv4 addresses are 32-bit numbers written as four decimal octets (`192.168.1.10`). IPv6 addresses are 128-bit, written in hex groups (`2001:db8::1`), created because IPv4's ~4.3 billion addresses ran out. MAC addresses are 48-bit hardware identifiers (`aa:bb:cc:dd:ee:ff`) used only within a local network segment — routers strip and replace them as traffic crosses networks, but the IP address in the packet stays the same end to end.

### Ports: how a *service* is found on that computer

An IP address gets you to a machine; a **port** (0–65535) gets you to a specific service on it. Port 22 is conventionally SSH, 80 is HTTP, 443 is HTTPS, 53 is DNS — but these are conventions, not laws; anything can run on any port.

### TCP vs UDP

**TCP** is connection-oriented and reliable: before data flows, two sides perform a **three-way handshake**:
```
Client                     Server
  | ---- SYN ----------->    |
  | <--- SYN-ACK --------    |
  | ---- ACK ----------->    |
  |        [data flows]      |
```
This handshake is *why* a port scanner can tell if a port is open without a full application-level connection — see Module 11/12.

**UDP** is connectionless: packets are sent with no handshake and no guarantee of delivery or order. DNS queries, video streaming, and online games often use UDP because speed matters more than guaranteed delivery.

### DNS: names to addresses

Humans use names (`example.com`); computers route on IP addresses. DNS is the lookup system that converts one to the other:
```
You type example.com
   → your resolver asks a DNS server
   → DNS server replies: 93.184.216.34
   → your computer connects to that IP
```
Test this yourself in Module 08's lab with `dig`.

### Private vs Public Addresses, and NAT

Certain IP ranges are reserved for private/internal use and are never routed on the public internet:

| Range | Common use |
|---|---|
| `10.0.0.0/8` | Large private networks |
| `172.16.0.0/12` | Private networks |
| `192.168.0.0/16` | Home/small networks |
| `127.0.0.0/8` | Loopback (`localhost`) |

**NAT (Network Address Translation)** is how many devices on a private network (e.g., your home Wi-Fi, all `192.168.1.x`) share one public IP address to reach the internet — your router rewrites the source address of outgoing packets and tracks the mapping so replies come back to the right device.

### CIDR notation

`192.168.1.0/24` means: the first 24 bits are the fixed network portion, leaving 8 bits (256 addresses, 254 usable) for hosts. This notation is used constantly when scoping a network scan (Module 11–12) — scanning `/24` vs `/16` is the difference between 254 hosts and 65,534 hosts.

## Why It Matters

Nearly every security concept from Module 10 onward assumes you understand this. "Port 22 is open" is meaningless unless you know a port is a service address, not a physical thing. "Scan the /24" is meaningless without CIDR. This lesson is the foundation for the entire reconnaissance and enumeration track.

## Common Mistakes

- Believing an open port always means a vulnerability — it means a service is *listening*, nothing more (Module 12 covers why).
- Assuming private IP ranges (`192.168.x.x`) are inherently safe to scan without permission — if it's not *your* network, it's still not authorized.
- Confusing DNS *resolution* (name → IP) with the target actually being reachable — DNS can resolve a name to an address that's unreachable or firewalled.

## Security Perspective

Attackers and defenders both live in this layer constantly:
- **Attacker view:** which ports are open, what's listening, what network segment am I on, can I reach other segments?
- **Defender view:** which ports *should* be open, is anything listening that shouldn't be, is NAT/firewall configuration doing its job, are internal ranges actually isolated from the internet?

## Exercise

Before the lab, write down: what is the CIDR notation for a network with exactly 16 usable host addresses? (Hint: work backwards from 256, 128, 64, 32, 16.)

## Further Reading

- RFC 791 (IPv4), RFC 793 (TCP), RFC 1035 (DNS) — the original specifications
- [DigitalOcean: Understanding IP Addresses, Subnets, and CIDR Notation](https://www.digitalocean.com/community/tutorials/understanding-ip-addresses-subnets-and-cidr-notation-for-networking)
