# Troubleshooting — Module 02

**VM won't boot / black screen** — confirm your hypervisor's virtualization extensions (VT-x/AMD-V) are enabled in your host machine's BIOS/UEFI; most import failures trace back to this.

**No internet access on the VM** — confirm the network adapter is set to NAT (Lesson 02.2, Step 3) for the update step; Host-only/Internal networks (Module 26) intentionally have no internet route.

**`apt update` fails with "could not resolve host"** — same cause as above: check the adapter mode, then confirm with `ping -c 2 8.8.8.8` (Module 08).

**`sudo` says "user is not in the sudoers file"** — you're likely on an account that wasn't set up with sudo access; check `id` for `sudo` group membership, or refer to Kali's official documentation for the default account for your specific image.

**VM is extremely slow** — check allocated RAM/CPU against the table in `02-installation.md`; also confirm your hypervisor is using hardware virtualization, not software emulation.
