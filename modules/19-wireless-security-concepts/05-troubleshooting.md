# Troubleshooting — Module 19

**`airmon-ng start wlan0` says "no such device"** — your VM may not have passed through the wireless interface; check the hypervisor's USB device passthrough settings for the wireless adapter.

**`airodump-ng` shows no networks** — confirm you're actually in monitor mode (`iw dev` should show `type monitor`), and that you're not filtering to a specific channel/BSSID too narrowly before confirming your target's actual channel.

**"Handshake" never appears in airodump-ng** — wait longer (a reconnect needs to happen), or force a device to reconnect (in your own lab, you can disconnect and reconnect a device manually).

**`aircrack-ng` says "0 handshakes"** — the capture file didn't capture a full 4-way handshake; the airodump-ng line showing "WPA handshake: ..." must appear before you can run aircrack-ng against the capture.
