# Lesson 26.2 — Building the Lab Step by Step

## Requirements

- A hypervisor: VirtualBox (free) or VMware Workstation Player (free for personal use)
- Kali Linux VM (Module 02 covers installing this)
- Metasploitable 2 VM (Module 11 introduced this; full setup here)
- At least 8GB RAM on the host machine (4GB minimum per VM is tight but workable for these two)

## Steps

1. **Create the isolated network first**, before installing anything:
   - VirtualBox: File → Host Network Manager → Create a new Host-only network (e.g. `vboxnet0`).
   - VMware: Edit → Virtual Network Editor → add a Host-only or Custom (non-NAT) network.
2. **Install/import Kali** (Module 02) and set its network adapter to this new Host-only network.
3. **Import Metasploitable 2** and set its network adapter to the *same* Host-only network.
4. Boot both VMs.
5. On Kali, confirm your address is on the expected subnet:
   ```bash
   ip addr show
   ```
6. On Metasploitable, log in (`msfadmin`/`msfadmin`) and confirm its address:
   ```bash
   ip addr show
   ```
7. From Kali, confirm you can reach Metasploitable, and confirm you **cannot** reach the internet from Metasploitable:
   ```bash
   ping -c 2 <metasploitable-ip>      # should succeed
   ```
   On Metasploitable:
   ```bash
   ping -c 2 8.8.8.8                   # should FAIL — this is correct and expected
   ```
8. **Take a snapshot of both VMs now**, labeled clearly (e.g., "clean-baseline"). This is what you'll restore to before/after any lab that modifies system state.

## Verifying Isolation (Do Not Skip)

- Confirm neither VM's adapter is set to "Bridged."
- Confirm the Host-only/Internal network you created has no "Enable Network Address Translation" or similar internet-sharing option turned on for these VMs specifically.
- If your hypervisor's host-only network *does* provide DHCP/internet by default (some do), explicitly disable it, or use "Internal Network" mode instead, which never routes anywhere by design.

## Resetting the Environment

Whenever a lab leaves Metasploitable in a modified state (Module 20 especially), revert to your snapshot:
- VirtualBox: right-click VM → Snapshots → Restore.
- VMware: VM → Snapshot → Revert to Snapshot.

This is the "undo button" that makes repeated experimentation safe and consistent.
