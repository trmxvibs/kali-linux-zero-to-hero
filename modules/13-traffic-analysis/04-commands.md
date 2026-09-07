# Lesson 13.2 — Capture and Filter Commands

> ⚠️ **Testing note:** this course's build sandbox has no `tcpdump`, `tshark`, or packet-capture library available, and no network access. Every command below is written against official `tcpdump`/Wireshark documentation and standard, well-established syntax, but was **not live-executed** during this build — see `tests/TEST_LOG.md`. Verify against your own Kali VM.

## `tcpdump` — command-line capture

```bash
sudo tcpdump -i eth0                       # capture on interface eth0, print summaries live
sudo tcpdump -i eth0 -w capture.pcap         # write raw capture to a file instead of printing
sudo tcpdump -r capture.pcap                   # read back a previously saved capture
sudo tcpdump -i eth0 -n                          # -n: don't resolve hostnames/ports (faster, avoids DNS traffic contaminating your own capture)
```

### Capture filters (Berkeley Packet Filter syntax)

```bash
sudo tcpdump -i eth0 port 80                  # only HTTP traffic
sudo tcpdump -i eth0 host 192.168.1.50          # only traffic to/from a specific host
sudo tcpdump -i eth0 'port 80 or port 443'        # HTTP or HTTPS
sudo tcpdump -i eth0 -c 100 -w sample.pcap          # capture exactly 100 packets then stop
```
**Reading it:** these expressions decide what's written to the file at all (Lesson 13.1's capture-vs-display distinction) — anything not matching is never recorded.

## Wireshark — GUI capture and analysis

Basic workflow (GUI-driven, described here for reference):
1. Launch Wireshark, select the interface to capture on
2. Apply a **display filter** in the filter bar, e.g. `http`, `tcp.port == 22`, `ip.addr == 192.168.1.50`
3. Right-click a packet → "Follow → TCP Stream" to reconstruct an entire conversation, not just one packet at a time

### Common display filters

```
http                      # only HTTP traffic
tls                        # only TLS/HTTPS handshake traffic
tcp.port == 22               # only traffic on TCP port 22
ip.addr == 192.168.1.50        # only traffic to/from a specific IP
http.request.method == "POST"    # only HTTP POST requests
```

## `tshark` — command-line Wireshark

```bash
tshark -i eth0                           # live capture, text output
tshark -r capture.pcap -Y "http"            # read a file, apply a display filter
tshark -r capture.pcap -T fields -e ip.src -e ip.dst -e tcp.port    # extract specific fields, useful for scripting
```

## Further Reading

- [tcpdump — official man page](https://www.tcpdump.org/manpages/tcpdump.1.html)
- [Wireshark — Display Filter Reference](https://www.wireshark.org/docs/dfref/)
- [pcap-filter syntax](https://www.tcpdump.org/manpages/pcap-filter.7.html)
