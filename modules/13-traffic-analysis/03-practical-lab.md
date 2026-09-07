# Lab 13 — Capturing and Reading Real Traffic

**Environment:** Your Kali VM (this lab requires real `tcpdump`/Wireshark and a real network interface — it cannot be done in most minimal containers/sandboxes; see the testing note in `04-commands.md`).

> ⚠️ **LAB ONLY** — capture only on your own Kali VM's interface, ideally while it's on the isolated lab network from Module 26, or your own home network that you administer.

## Steps

1. Start a capture, writing to a file, while you generate some traffic yourself:
   ```bash
   sudo tcpdump -i eth0 -w lab13.pcap -c 200
   ```
2. In another terminal (or another action on the same machine), generate traffic to capture:
   ```bash
   ping -c 4 <your-gateway-ip>
   curl -I http://example.com
   ```
3. Once the capture finishes (200 packets, or press Ctrl+C early), read it back:
   ```bash
   sudo tcpdump -r lab13.pcap -n | head -20
   ```
4. Open the same file in Wireshark and apply a display filter:
   ```
   icmp
   ```
   Confirm you can see your `ping` requests and replies.
5. Filter for the HTTP request instead:
   ```
   http
   ```
   Right-click the request → Follow → HTTP Stream, and read the full plaintext request/response.
6. Repeat step 2's `curl` against an HTTPS URL instead (`curl -I https://example.com`), re-capture, and apply the `tls` filter in Wireshark. Confirm you can see the TLS handshake, but **cannot** read the HTTP content the way you could in step 5 — this is Lesson 13.1's encryption point, made concrete.

## Expected Result

- Step 4: ICMP echo request/reply pairs visible, matching your `ping` command exactly
- Step 5: the full plaintext HTTP request (including headers) readable via "Follow HTTP Stream"
- Step 6: TLS handshake visible, but no readable HTTP content — confirming encryption is doing its job

## Next Step

[Module 14 — Web Security Fundamentals](../14-web-security-fundamentals/README.md)
