# Lab 09 — Layered Troubleshooting, Hands-On

**Environment:** Any Linux terminal with `nc` (netcat) installed. Steps 1–4 need a real network (Kali VM); steps 5–7 work anywhere, including this course's own build sandbox — verified below.

## Steps

1. Confirm your interface and IP (Module 08):
   ```bash
   ip addr show
   ```
2. Ping your gateway:
   ```bash
   ip route show                    # find the gateway IP first
   ping -c 2 <gateway-ip>
   ```
3. Test DNS specifically:
   ```bash
   dig example.com +short
   ```
4. Test the same destination by IP directly, bypassing DNS:
   ```bash
   ping -c 2 93.184.216.34
   ```
5. **Port-level check — start a listener and confirm it's reachable, in two separate terminals (or two separate commands, one backgrounded):**
   ```bash
   # Terminal A:
   nc -l -p 7777
   # Terminal B:
   nc -zv -w 2 localhost 7777
   ```
6. **Now try to reuse the same listener for a data test — observe that it fails**, then understand why:
   ```bash
   # Terminal A (start a FRESH listener — the previous one already exited after step 5's connection):
   nc -l -p 7778 > received.txt
   # Terminal B:
   echo "diagnostic test payload" | nc -w 2 localhost 7778
   ```
   Check the result:
   ```bash
   cat received.txt
   ```
7. Confirm a closed port fails distinctly and immediately (not a timeout):
   ```bash
   nc -zv -w 2 localhost 55555
   ```

## Expected Result — and a Real Gotcha

Step 7 should print `Connection refused` immediately (this is a **fast refusal**, not a timeout — an important distinction from a firewall silently dropping packets, which would hang until the timeout).

**The gotcha in steps 5–6 is deliberate and was discovered during this course's own testing:** `nc -l` (listen mode) accepts exactly **one** connection and then exits. If you run the `-zv` check against a listener and then try to send it real data afterward, the second connection will fail — not because anything is broken, but because the listener from step 5 is already gone. **You must start a fresh listener for step 6.** This is exactly the kind of "worked once, then mysteriously stopped" confusion that Module 09's layered method is designed to help you diagnose methodically instead of guessing at.

## Next Step

[Module 10 — Security Fundamentals](../10-security-fundamentals/README.md)
