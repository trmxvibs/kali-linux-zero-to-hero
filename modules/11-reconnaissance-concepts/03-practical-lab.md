# Lab 11 — First Authorized Scan

**Environment:** Kali VM + isolated Metasploitable 2 VM (Lesson 11.2).

## Steps

1. Confirm your scope: you should know the exact IP address of your Metasploitable VM and nothing else is in scope.
2. Run a conservative scan:
   ```bash
   nmap -T2 <metasploitable-ip>
   ```
3. Re-run with service detection:
   ```bash
   nmap -sV -T2 <metasploitable-ip>
   ```
4. Record, in a simple table, every open port, its service name, and its reported version.
5. Pick one service version from your table and look up (via the vendor's own advisories or the NVD) whether it has any publicly documented vulnerabilities — do not exploit anything yet; this is purely a recon-to-research exercise, continued properly in Module 15.

## Expected Result

A table with at least 3 rows (Metasploitable exposes many intentionally vulnerable services), e.g.:

| Port | Service | Version |
|---|---|---|
| 21 | ftp | vsftpd 2.3.4 |
| 22 | ssh | OpenSSH 4.7p1 |
| 80 | http | Apache httpd 2.2.8 |

## Troubleshooting

See `05-troubleshooting.md`.

## Next Step

[Module 12 — Network Enumeration](../12-network-enumeration/README.md)
