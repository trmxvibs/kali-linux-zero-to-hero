# Lesson 11.2 — Setting Up the Lab Target (Metasploitable 2)

> ⚠️ **LAB ONLY.** Metasploitable 2 is deliberately, extremely insecure. Never expose it to any network beyond an isolated, host-only virtual network with no internet access.

## What You Need

- Kali VM (from Module 02) with a hypervisor (VirtualBox, VMware, etc.)
- Metasploitable 2 virtual disk image (freely distributed for security training; see Module 26 for full lab-network setup)
- A **host-only** or **internal** virtual network shared only between your Kali VM and the Metasploitable VM

## Steps (Summary — full detail in Module 26)

1. Download Metasploitable 2 from a source you trust (official Rapid7/SourceForge distribution).
2. Import it into your hypervisor as a new VM.
3. Set its network adapter to the same **host-only/internal** network as your Kali VM — not "Bridged" and not "NAT with internet."
4. Boot it. Default login is `msfadmin` / `msfadmin` (this is intentional — it's a training target).
5. From Kali, confirm connectivity:
   ```bash
   ping -c 2 <metasploitable-ip>
   ```
6. Take a VM snapshot now, before running anything against it, so you can always reset to a clean state.

## Verifying Isolation Before Continuing

Confirm the Metasploitable VM's network adapter has **no route to the internet** and is **not** on the same network as any other real device. This is the single most important setup step in this entire module.

Full network-isolation architecture: [Module 26 — Building Your Own Security Lab](../26-building-your-own-lab/README.md).
