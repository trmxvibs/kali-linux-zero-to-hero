# Lesson 11.3 — Nmap Basics

## Nmap

**What it is:** The de facto standard network scanner — probes hosts and ports and reports what's reachable and (optionally) what's running.
**Why it exists:** Manually testing thousands of ports with raw sockets doesn't scale; Nmap automates the handshake-based detection from Lesson 11.1 across many hosts and ports at once.
**Category:** Active reconnaissance / enumeration.

**When to use:** Once you have explicit authorization and a defined scope (an IP, range, or hostname you're permitted to test).
**When NOT to use:** Against anything outside your authorized scope — including "just checking" a public website you don't own.

### Basic syntax

```bash
nmap <target>
```

### Safe lab example

```bash
nmap -sV -T2 <metasploitable-ip>
```
- `-sV` — attempt to detect service *versions*, not just open/closed state
- `-T2` — "polite" timing template: slower, less likely to disrupt a fragile target (Metasploitable is deliberately fragile)

**Expected output (abridged):**
```
PORT     STATE SERVICE     VERSION
21/tcp   open  ftp         vsftpd 2.3.4
22/tcp   open  ssh         OpenSSH 4.7p1
80/tcp   open  http        Apache httpd 2.2.8
```

**Interpreting output:**
- `STATE open` — a service accepted the handshake.
- The `VERSION` column is what makes this list actionable in Module 15 (Vulnerability Assessment) — specific old versions (like the `vsftpd 2.3.4` shown above) map to publicly known, documented vulnerabilities. Recognizing the version is the link between recon and assessment.

**Common errors:**
- `Note: Host seems down` — often means ICMP is blocked; try `-Pn` to skip the host-discovery ping and scan anyway.
- Extremely slow scans — you probably scanned all 65535 ports (`-p-`) with default timing; start with the default top-1000 ports.

**Defensive perspective:** The same scan run against your *own* infrastructure is exactly how you'd audit your own exposed attack surface (Module 17). Many organizations run scheduled internal Nmap scans specifically to catch services that were exposed by accident.

> ⚠️ **LAB ONLY** — run every example in this file only against your isolated Metasploitable target.

## Further Reading

- [Nmap Reference Guide](https://nmap.org/book/man.html)
