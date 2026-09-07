# Troubleshooting — Module 13

**"tcpdump: eth0: You don't have permission to capture on that device"** — packet capture needs elevated privileges; use `sudo`, or (more precisely) grant your user the `CAP_NET_RAW` capability if you want to avoid running the whole capture as root.

**Capture file is empty / no packets shown** — confirm you're capturing on the correct interface (`ip addr show` from Module 08 to list interfaces); a common mistake is capturing on `eth0` when the relevant traffic is on a different interface (VPN, loopback, wireless).

**Wireshark shows way more traffic than expected** — apply a display filter (Lesson 13.2) rather than trying to read everything; remember display filters don't lose data, so it's safe to narrow and widen freely while investigating.

**Can't find the request/response you expected in a capture** — confirm the traffic wasn't encrypted (check for `tls` instead of `http`, per Lesson 13.1), and confirm your capture filter (if any) didn't exclude it before it was ever recorded — this is unrecoverable, unlike a display filter.

**Capture shows "packets dropped by kernel" in statistics** — the capture couldn't keep up with traffic volume; consider a narrower capture filter, or capturing to a faster disk.
