# Lesson 12.2 — Enumeration Commands

> ⚠️ **Testing note:** this course's build sandbox has no network access and no Metasploitable VM to enumerate. The banner-grabbing technique using `nc` **was** verified locally against a simulated service. The specific service-enumeration tools below (`enum4linux`, `smbclient`, `showmount`, Nmap NSE scripts) are documented from official tool documentation and are standard, well-established Kali tooling, but were **not live-executed** during this build — see `tests/TEST_LOG.md`. Verify against your own Metasploitable lab (Module 26).

## Banner Grabbing with `nc`

```bash
nc <target> 21          # connect and read whatever the service announces
nc <target> 22
```
**Tested and confirmed during this course's build** (against a local simulated service): connecting with plain `nc` and reading the first line returned is banner grabbing — no special tool needed for this basic technique.

## Nmap Scripting Engine (NSE) for deeper enumeration

**What/why:** Nmap isn't just a port scanner — its Scripting Engine runs additional probes against detected services for much deeper information than a basic scan.

```bash
nmap -sV --script=default <target>            # run Nmap's default safe script set alongside version detection
nmap --script=ftp-anon <target> -p 21           # specifically test for anonymous FTP access
nmap --script=smb-enum-shares <target> -p 445     # enumerate SMB shares
```
**Reading output:** NSE script results appear as extra lines under each port's entry, prefixed with `|`. A result like `ftp-anon: Anonymous FTP login allowed` is a direct, actionable finding.

## SMB Enumeration — `smbclient` and `enum4linux`

```bash
smbclient -L //<target> -N           # list shares, -N = no password (anonymous attempt)
enum4linux -a <target>                 # broad SMB enumeration: shares, users, OS info, groups
```

## NFS Enumeration — `showmount`

```bash
showmount -e <target>          # list NFS exports offered by a target
```

## Further Reading

- [Nmap NSE — official script documentation](https://nmap.org/nsedoc/)
- `man smbclient`, `man showmount`
- [enum4linux — GitHub](https://github.com/portcullislabs/enum4linux) (or its actively maintained fork, `enum4linux-ng`)
