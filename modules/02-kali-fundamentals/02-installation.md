# Lesson 02.2 — Installing Kali in a Virtual Machine

## Hardware Requirements (Guest VM)

| Resource | Minimum | Recommended for this course |
|---|---|---|
| RAM | 2 GB | 4 GB+ |
| Disk | 20 GB | 40 GB+ |
| CPU | 1 core | 2 cores |

(Your physical host needs enough headroom above this to also run Metasploitable later — Module 26 — so 8 GB+ host RAM is a realistic baseline.)

## Step 1 — Choose a Hypervisor

- **VirtualBox** (free, cross-platform) — used in this course's examples
- **VMware Workstation Player** (free for personal use) — equally valid; steps are conceptually identical

## Step 2 — Get Kali

Download the official Kali VM image or ISO from **kali.org/get-kali** only — never a third-party mirror. Two common choices:

- **Pre-built VM image** (`.ova`/`.vmx`) — fastest, just import it
- **Installer ISO** — more control, walks through a normal OS install

This course assumes the pre-built VM image for simplicity.

## Step 3 — Import and First Boot

1. In VirtualBox: File → Import Appliance → select the downloaded `.ova` file.
2. Review the allocated RAM/CPU/disk against the table above; adjust if needed.
3. **Before first boot**, set the network adapter — leave it on the default (NAT) for now; Module 26 will change this to Host-only/Internal once you're building the isolated lab.
4. Boot the VM. Default credentials for the official Kali VM images are documented on kali.org (they change occasionally between releases — always check the current official page rather than relying on a memorized username/password).

## Step 4 — Update Immediately After First Boot

```bash
sudo apt update
sudo apt full-upgrade -y
```
Full explanation of these commands is in Module 06 — for now, just run them. This ensures you're not learning against a stale, possibly-vulnerable-to-unrelated-things snapshot of the OS itself.

> ⚠️ This step requires internet access on the Kali VM — keep its network adapter on NAT (internet-capable) for this step only. Module 26 explains why you'll change this before running lab exercises.

## Step 5 — Verify Basic Functionality

```bash
uname -a          # confirm you're on Linux, see kernel version
whoami             # confirm your username
ip addr show       # confirm network configuration (Module 08)
```

## Step 6 — Take a Snapshot

Once updated and verified working, take a VM snapshot labeled `clean-updated-baseline`. This becomes your recovery point before Module 26 changes networking, and before any lab that modifies system state.

## Troubleshooting Installation

See `05-troubleshooting.md`.
