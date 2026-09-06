# Security Notes — Module 08

- Every reconnaissance and enumeration technique in Modules 11–13 is built directly on the concepts here: an "open port" is meaningful only because you understand the TCP handshake; a "scan range" is meaningful only because you understand CIDR.
- **Defender view:** `ss -tulpn` run periodically on your own systems is a basic but genuinely useful check — "is anything listening that I didn't intend to expose?" This is one of the simplest, highest-value defensive habits in this entire course.
- **NAT and private ranges are not a security boundary by themselves.** A common beginner misconception is that being on a private/NAT'd network makes a machine "safe." NAT hides addressing, it does not authenticate or authorize anything — a compromised machine on your LAN can usually reach other machines on that same LAN freely.

> ⚠️ **LAB ONLY** — scanning, pinging, or otherwise probing any network you do not own or have explicit authorization to test is out of scope for this entire course, regardless of whether the range is "private" (e.g. `192.168.x.x`) — private addressing does not imply it's yours to test.
