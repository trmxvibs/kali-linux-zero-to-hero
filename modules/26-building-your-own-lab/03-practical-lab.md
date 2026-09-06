# Lab 26 — Verifying Your Lab Is Actually Isolated

This lab is a verification checklist, meant to be run *after* completing
the setup steps in [02-installation.md](02-installation.md).

## Steps

1. On Kali, confirm you can reach Metasploitable:
   ```bash
   ping -c 2 <metasploitable-ip>
   ```
   Expected: 0% packet loss.

2. On Metasploitable, confirm you **cannot** reach the internet:
   ```bash
   ping -c 2 8.8.8.8
   ```
   Expected: 100% packet loss / "Network unreachable." **This failure is correct and desired.**

3. On your physical host machine (not a VM), confirm you **cannot** directly reach Metasploitable's IP (if your host-only network is configured correctly, host-to-VM reachability depends on your chosen mode — verify against what you designed in `01-concepts.md`, and adjust to "Internal Network" mode if you need guaranteed no-host-access).

4. Take a snapshot of both VMs now, labeled `clean-baseline-<today's date>`.

5. Document your setup in a personal notes file: hypervisor used, network mode chosen, both VMs' IP addresses, and the date of your baseline snapshot.

## Expected Result

A short written record confirming: Kali ↔ Metasploitable connectivity works; Metasploitable ↔ internet is blocked; a baseline snapshot exists for both VMs.

## Next Step

You're ready for [Module 11 — Reconnaissance Concepts](../11-reconnaissance-concepts/README.md) if you haven't already completed it, or [Module 12 — Network Enumeration](../12-network-enumeration/README.md).
