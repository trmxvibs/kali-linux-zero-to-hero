# Lesson 19.2 — Wireless Commands

> ⚠️ **Testing note:** every command in this file requires real wireless hardware with monitor-mode capability. Not live-tested during this course's build — see `tests/TEST_LOG.md`. These are standard, well-documented `aircrack-ng` suite commands.

> ⚠️ **LAB ONLY** — every command here is only legal and ethical on wireless networks you own or have explicit authorization to test.

## Check wireless interface capabilities

```bash
iw list                       # list all wireless interfaces and their capabilities
iw dev                          # show current wireless devices and modes
```
Look for "monitor" in the `Supported interface modes` section — if it's absent, this chipset won't work for packet capture.

## Enable monitor mode

```bash
sudo airmon-ng check kill      # stop processes that might interfere
sudo airmon-ng start wlan0       # put wlan0 into monitor mode (creates wlan0mon)
```

## Scan for networks (passive — does NOT interact with them)

```bash
sudo airodump-ng wlan0mon                  # scan all channels, show visible APs and clients
sudo airodump-ng --channel 6 wlan0mon        # focus on channel 6
```

## Capture a WPA2 4-way handshake

```bash
sudo airodump-ng --channel 6 --bssid AA:BB:CC:DD:EE:FF --write capture wlan0mon
```
**Lab only:** the target BSSID must be an AP you own or are explicitly authorized to test. A handshake is captured when a client connects or reconnects — you wait, or (in an authorized pentest) use a deauthentication frame to force a reconnect.

## Offline dictionary attack against a captured handshake

```bash
aircrack-ng -w /usr/share/wordlists/rockyou.txt capture-01.cap
```
**What this does:** for each word in the wordlist, derives the PMK (pairwise master key) from the AP's SSID and the candidate word, then checks whether the cryptographic material in the capture is consistent — entirely offline, no further interaction with the real network.

## Return to normal mode

```bash
sudo airmon-ng stop wlan0mon
sudo systemctl start NetworkManager
```

## Further Reading

- [aircrack-ng — official documentation](https://www.aircrack-ng.org/documentation.html)
- `man iw`, `man airmon-ng`, `man airodump-ng`
