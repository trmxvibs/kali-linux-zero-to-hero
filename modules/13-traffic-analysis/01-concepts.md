# Lesson 13.1 — Seeing What's Actually on the Wire

## Learning Objectives

- Understand what packet capture actually captures, and at what layer
- Understand the difference between capturing and filtering
- Understand why encrypted traffic looks different from plaintext traffic in a capture
- Know when traffic analysis is the right tool versus Module 09's connectivity checks or Module 12's enumeration

## Prerequisites

Module 08 (Networking Fundamentals) — this module directly inspects the packets that module described conceptually.

## Concept

**Plain language:** Every command so far in this course has asked a network *a question* and looked at the *answer* (ping, nc, nmap). Traffic analysis is different: instead of asking questions, you sit on the wire and watch everything that passes by, unfiltered, exactly as it travels. This gives you ground truth that no single tool's summary can fully replace — you see the actual bytes, not a tool's interpretation of them.

**Technical:** A **packet capture** (commonly called a "pcap," from the underlying `.pcap`/`.pcapng` file format) is a raw, chronological record of frames seen on a network interface. Two tools dominate this space on Kali:

- **`tcpdump`** — command-line, lightweight, ideal for quick capture or capturing on a remote/headless machine to analyze later
- **Wireshark** (and its command-line sibling **`tshark`**) — full graphical protocol analysis, stream reconstruction, and deep filtering

Both read/write the same file formats, so a common workflow is: capture with `tcpdump` on a server with no GUI, then open the resulting file in Wireshark on your desktop for deep analysis.

### Capturing vs. Filtering — two different moments

- **Capture filters** are applied *while capturing*, deciding what gets written to the file/buffer at all (e.g., "only capture traffic on port 80"). Anything not matching is gone forever — never recorded.
- **Display filters** are applied *after* capture, to a file/buffer that already contains everything — they only control what you're currently looking at; the underlying data is still all there if you change the filter.

This distinction matters: if you're not sure what you'll need, capture broadly and filter narrowly for viewing, rather than filtering too aggressively at capture time and losing something you needed.

### Why Encryption Changes What You See

Module 10 covered encryption conceptually; here's the practical consequence: capturing HTTPS traffic shows you the encrypted bytes (via TLS) — source/destination, timing, and packet sizes are visible, but the actual HTTP request/response content is not, by design. Capturing plaintext HTTP shows you everything, including credentials if any were sent in the clear — which is exactly why plaintext protocols are considered a security weakness (Module 17 revisits this).

### When to Reach for Traffic Analysis

| Situation | Better tool |
|---|---|
| "Is this specific port reachable?" | Module 09's `nc` |
| "What services/versions are running?" | Module 11/12's Nmap/enumeration |
| "What is actually being sent, byte for byte, and when?" | **This module** |
| "Why did this specific request fail at the protocol level?" | **This module** |

## Why It Matters

Modules 14 (Web Security) and 17 (Defensive Security) both return to packet-level evidence: confirming a web request's exact headers, or investigating what a compromised host actually communicated with. Traffic analysis is the ground-truth layer beneath both.

## Common Mistakes

- Capturing on the wrong interface (e.g., capturing on `eth0` when the traffic you care about is on a VPN or loopback interface) and concluding "nothing happened."
- Confusing a capture filter mistake (accidentally excluding relevant traffic permanently) with a display filter mistake (easily fixed by just changing the filter).
- Assuming a capture is complete when high traffic volume can cause packet drops if the machine can't keep up — checking capture statistics for "dropped" counts matters on busy networks.

## Security Perspective — Attacker View vs Defender View

**Attacker (in an authorized test):** Confirming exactly what a target application sends — are credentials sent in plaintext? Is sensitive data exposed in unencrypted form?
**Defender:** Traffic analysis is a core incident-response and monitoring technique — spotting unusual destinations, unexpected protocols, or data leaving where it shouldn't (Module 17).

> ⚠️ **LAB ONLY** — capture traffic only on networks/interfaces you own or are authorized to monitor. Capturing traffic on a shared network you don't control or administer (e.g., public Wi-Fi, a workplace network without authorization) can expose other people's private data and cross serious legal and ethical lines covered in Module 00.

## Exercise

Before the lab, predict: if you capture traffic while visiting an HTTPS website, will you be able to see the page's content in the capture? What about the domain name you connected to?

## Further Reading

- [Wireshark — official documentation](https://www.wireshark.org/docs/)
- `man tcpdump`
- [tcpdump/libpcap filter syntax (pcap-filter man page)](https://www.tcpdump.org/manpages/pcap-filter.7.html)
