# Troubleshooting — Module 11

**"Host seems down"** — Add `-Pn` to skip host discovery: `nmap -Pn -sV <target>`.

**Scan takes forever** — You're likely scanning all ports or using an aggressive/slow combination against a fragile target. Start with default top-1000 ports and `-T2`/`-T3`.

**"nmap: command not found"** — Kali ships with Nmap pre-installed; if missing, `sudo apt install nmap`.

**No route to host** — Confirm both VMs are on the same virtual network (Lesson 11.2) and that VM is powered on.
