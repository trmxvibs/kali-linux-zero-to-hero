# Lesson 19.1 — Wireless Security Concepts

## Learning Objectives

- Understand 802.11 wireless networking fundamentals
- Understand why WEP is broken, WPA2 is better, and what WPA3 adds
- Understand what "monitor mode" means and why it requires specific hardware
- Know the primary wireless attack concepts (for defense and authorized testing only)

## Prerequisites

Module 08 (Networking Fundamentals), Module 10 (Security Fundamentals).

> ⚠️ **Testing note:** wireless security tools (aircrack-ng, airodump-ng, aireplay-ng) require a wireless interface in monitor mode and real wireless traffic to test. This course's build sandbox has no wireless hardware. This module is documented from authoritative sources (802.11 standards, aircrack-ng documentation, NIST guidelines) and marked not-live-tested — see `tests/TEST_LOG.md`.

> ⚠️ **LAB ONLY.** Everything in this module applies to **your own wireless network, or networks you have explicit authorization to test.** Capturing or deauthenticating traffic on someone else's wireless network — even to "just see what's there" — is unauthorized access and illegal in most jurisdictions.

## Concept

**Plain language:** Wi-Fi is radio — it's broadcast by nature, meaning anyone within range can receive (and potentially read or record) the signals. The security of a wireless network depends entirely on the encryption layer protecting those signals, and on how strong/well-implemented that layer is.

### Encryption Protocol History

| Protocol | Status | Why |
|---|---|---|
| **WEP** | Completely broken — do not use | RC4 stream cipher misuse; IV reuse allows full key recovery with enough captured packets; tools to do this are public and fast |
| **WPA/TKIP** | Deprecated; still weak | Patched WEP weaknesses, but TKIP was designed as a transitional solution and has its own vulnerabilities |
| **WPA2/CCMP** | Current minimum standard | AES-based; the pre-shared key (WPA2-PSK/WPA2-Personal) mode is vulnerable to offline dictionary attacks if a 4-way handshake is captured and the password is weak |
| **WPA3** | Recommended | Adds Simultaneous Authentication of Equals (SAE), replacing PSK; makes offline dictionary attacks much harder even if the handshake is captured |

### Monitor Mode

Normal wireless cards only process packets addressed to them. **Monitor mode** allows a wireless card to receive all packets on the channel, regardless of destination — equivalent to promiscuous mode on a wired network. Not all wireless chipsets support it; this is why wireless security testing often requires specific hardware (and why VMs using USB wireless adapters may have different capabilities than a native Kali install).

### The WPA2-Personal Weakness — Offline Dictionary Attack

1. An attacker (in an authorized test) positions to capture a **4-way handshake** — the authentication exchange that occurs when a client connects to an AP
2. The handshake contains enough cryptographic material that, offline, an attacker can test candidate passwords against it without further network interaction
3. A strong, long, random password makes this attack computationally infeasible; a short/common password makes it trivially fast

This is why "use a long, random Wi-Fi password" is not just boilerplate advice.

## Why It Matters

Wireless networks are the most accessible attack surface for physical-proximity attacks — anyone near your office or home can attempt to connect or capture traffic. Understanding the protocol-level weaknesses is what allows you to choose appropriate mitigations (WPA3, strong unique passwords, enterprise authentication) rather than just hoping the defaults are safe.

## Common Mistakes

- Assuming WPA2 is automatically secure regardless of password strength — the PSK mode's offline-dictionary vulnerability means password quality matters critically.
- Running wireless capture/injection tools without confirming the wireless card supports monitor mode — many cards don't, and you'll see empty captures rather than a useful error.
- Conducting any wireless test on a network you don't own or have explicit authorization for — nearby SSIDs are not authorization.

## Further Reading

- [IEEE 802.11 standard (overview)](https://www.ieee802.org/11/)
- [aircrack-ng — official documentation](https://www.aircrack-ng.org/documentation.html)
- [NIST SP 800-97 — Establishing Wireless Robust Security Networks](https://csrc.nist.gov/pubs/sp/800/97/final)
