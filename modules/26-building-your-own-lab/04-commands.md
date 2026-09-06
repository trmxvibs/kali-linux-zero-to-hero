# Commands — Module 26

This module is primarily about hypervisor configuration (GUI-driven), not
new terminal commands. The verification commands used are ones you already
know from Module 08:

```bash
ip addr show          # confirm each VM's assigned address
ping -c 2 <ip>          # confirm/deny reachability, per the isolation checklist in 03-practical-lab.md
```

Hypervisor-specific commands for scripted VM/snapshot management (e.g.,
VirtualBox's `VBoxManage`) are intentionally out of scope for this lesson —
the GUI workflow in `02-installation.md` is more reliable for beginners
setting this up for the first time.
