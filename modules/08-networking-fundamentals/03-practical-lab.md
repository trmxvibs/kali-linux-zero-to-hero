# Lab 08 — Mapping Your Own Network

**Environment:** Your Kali VM (or any Linux machine on a network you control).

> ⚠️ **LAB ONLY** — every command here targets your own machine or your own local network. Do not point these at networks you don't control.

## Goal

Move from theory to observation: see your own IP configuration, routing, DNS, and listening services.

## Steps

1. Find your own IP address and subnet:
   ```bash
   ip addr show
   ```
   Write down your IP and CIDR prefix (e.g., `192.168.1.23/24`).

2. Find your default gateway:
   ```bash
   ip route show
   ```

3. Test reachability to your gateway:
   ```bash
   ping -c 4 <your-gateway-ip>
   ```

4. Resolve a domain name and compare it to a direct IP connection:
   ```bash
   dig example.com +short
   curl -I https://example.com
   ```

5. See what's listening on your own machine right now:
   ```bash
   ss -tulpn
   ```
   Identify at least one TCP and, if present, one UDP listener. For each, note: local port, and the process name in the last column.

6. Calculate, on paper, how many usable hosts exist in your subnet based on the CIDR prefix you found in step 1 (e.g., `/24` → 254 usable addresses).

## Expected Result

You should be able to produce a short table:

| Item | Value |
|---|---|
| Your IP | ... |
| Subnet size | ... |
| Gateway | ... |
| A listening TCP port on your machine | ... |

## Troubleshooting

- `dig: command not found` → install `dnsutils` (`sudo apt install dnsutils`).
- No listeners shown by `ss -tulpn` → try without `sudo`; some processes only show their details to root, but the port itself should still be visible.

## Next Step

[Module 09 — Network Troubleshooting](../09-network-troubleshooting/README.md)
