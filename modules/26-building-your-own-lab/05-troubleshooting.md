# Troubleshooting — Module 26

**Kali can't reach Metasploitable at all** — confirm both VMs' network adapters are attached to the *exact same* Host-only/Internal network (not two similarly-named but different networks — a common mistake when a hypervisor has been used for multiple projects).

**Metasploitable unexpectedly CAN reach the internet** — your "host-only" network may have NAT/internet-sharing enabled by default in your hypervisor; switch to "Internal Network" mode, which never routes anywhere, or explicitly disable internet sharing on the host-only network's settings.

**Snapshot restore doesn't seem to revert changes** — confirm you're restoring the VM to the snapshot (not just renaming/creating a new one), and that the VM was powered off (or the hypervisor supports live-restore) before restoring.

**Can't get Metasploitable to boot** — verify the downloaded image matches your hypervisor's expected format (VirtualBox `.ova`/`.vmdk` vs. VMware `.vmx`); most distributions provide conversion guidance if needed.
