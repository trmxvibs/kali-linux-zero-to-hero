# Lab 12 — Enumerating Your Metasploitable Target

**Environment:** Kali VM + isolated Metasploitable 2 VM (Module 26).

## Part 1 — Banner Grabbing (verify the technique locally first)

Before touching your lab VM, confirm you understand the mechanic on your own Kali machine with a throwaway local listener:

```bash
# Terminal A:
printf "FAKE-SERVICE-BANNER-1.0\r\n" | nc -l -p 9000
# Terminal B:
nc localhost 9000
```
Confirm Terminal B prints the banner from Terminal A — this exact mechanic (connect, read what's offered) is what you're about to do against real services.

## Part 2 — Real Enumeration Against Metasploitable

> ⚠️ **LAB ONLY** — target your isolated Metasploitable VM exclusively.

1. Banner-grab FTP and SSH:
   ```bash
   nc <metasploitable-ip> 21
   nc <metasploitable-ip> 22
   ```
   Record both banners exactly.
2. Run Nmap's default script set against your target:
   ```bash
   nmap -sV --script=default -T2 <metasploitable-ip>
   ```
3. Specifically test for anonymous FTP:
   ```bash
   nmap --script=ftp-anon -p 21 <metasploitable-ip>
   ```
4. Enumerate SMB shares:
   ```bash
   smbclient -L //<metasploitable-ip> -N
   ```
5. Run a broader SMB enumeration:
   ```bash
   enum4linux -a <metasploitable-ip>
   ```
6. Check for NFS exports:
   ```bash
   showmount -e <metasploitable-ip>
   ```

## Expected Result

A short written table: for each service (FTP, SSH, SMB, NFS), record what was discoverable without any credentials — this table becomes direct input for Module 15 (Vulnerability Assessment).

## Next Step

[Module 13 — Traffic Analysis](../13-traffic-analysis/README.md)
