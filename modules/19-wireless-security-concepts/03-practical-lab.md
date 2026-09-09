# Lab 19 — Wireless Concepts in Your Own Lab

**Environment:** Kali VM with a wireless card that supports monitor mode. This lab cannot be reproduced without appropriate hardware — see `01-concepts.md`'s testing note.

> ⚠️ **LAB ONLY** — conduct this against your own wireless router/access point only, not any neighbor's network.

## Steps (Conceptual walk-through — verify your hardware first)

1. Confirm your wireless interface supports monitor mode:
   ```bash
   iw list | grep -A5 "Supported interface modes"
   ```
   If "monitor" appears, continue. If not, this lab requires different hardware.

2. Identify your own AP's BSSID and channel (visible in your router's admin page, or from `airodump-ng`'s initial passive scan).

3. Set up a **packet capture against your own AP** (not sending any traffic, just receiving):
   ```bash
   sudo airmon-ng start wlan0
   sudo airodump-ng --channel <your_channel> --bssid <your_AP_BSSID> --write ~/mytest wlan0mon
   ```

4. Connect/reconnect a device to your own AP — watch for "WPA handshake: <BSSID>" in the airodump-ng header, confirming a handshake was captured.

5. Run an offline dictionary attack against the capture using a wordlist that **includes your own AP's actual password** (modify `rockyou.txt` or use a custom list):
   ```bash
   aircrack-ng -w ~/test_wordlist.txt ~/mytest-01.cap
   ```
   Confirm it finds the password when the password is in the list.

6. Repeat step 5 with a wordlist that does NOT include your password — confirm it fails, demonstrating that password quality is the actual control.

## Expected Result

Step 5 succeeds (password found) — demonstrating the offline-dictionary vulnerability.
Step 6 fails (password not found) — demonstrating that a long, random, unique password is the defense against this specific attack.

## Next Step

[Module 20 — Exploitation Concepts in Safe Labs](../20-exploitation-concepts-safe-labs/README.md)
