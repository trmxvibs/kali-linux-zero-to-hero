# Lesson 09.1 — A Method for Diagnosing Network Problems

## Learning Objectives

- Apply a layered, systematic approach to "the network doesn't work"
- Distinguish connectivity, DNS, and service-level failures from each other
- Know which Module 08 tool answers which specific question

## Prerequisites

Module 08 (Networking Fundamentals) — this module is applied troubleshooting, not new theory.

## Concept

**Plain language:** "The network is broken" is almost never one problem — it's one of several *different* possible problems that happen to look identical from the outside (nothing loads). Effective troubleshooting means checking each layer in order, from closest to you outward, instead of guessing.

**Technical — a layered checklist**, from most local to most remote:

```
1. Is my network interface even up, with an IP address?      → ip addr show
2. Can I reach my default gateway?                               → ping <gateway>
3. Can I resolve DNS names to IP addresses?                        → dig example.com
4. Can I reach the destination IP directly (skip DNS)?               → ping <IP>
5. Is the SPECIFIC PORT/SERVICE reachable, not just the host?          → nc -zv <IP> <port>
6. Is the service actually responding correctly at the application layer? → curl -I, or the app's own client
```

Each step isolates a different possible failure:

- Failing at step 1 → local misconfiguration, nothing beyond your own machine is involved yet
- Failing at step 2 but not step 1 → local network/gateway issue
- Failing at step 3 but not step 2 → **DNS problem specifically** — the network itself is fine
- Failing at step 4 but working at step 3 (or vice versa) → tells you whether the problem is name resolution or actual reachability
- Failing at step 5 but not step 4 → the host is up, but the specific service/port isn't listening or is firewalled
- Failing at step 6 but not step 5 → the port is open, but the application behind it is misbehaving (wrong response, wrong protocol, etc.)

## Why It Matters

This exact checklist is what separates "I don't know, I just restarted it and it worked" from being able to say precisely what was wrong and why the fix worked. In security work specifically, distinguishing "port closed" from "port filtered" from "port open but service unresponsive" (Module 11) uses this same layered thinking.

## Common Mistakes

- Jumping straight to "restart everything" without isolating which layer actually failed — wastes time and teaches you nothing for next time.
- Testing DNS resolution and reachability together (e.g., only ever using a hostname) — you can't tell if a failure is DNS or connectivity unless you test the resolved IP directly too (step 4).
- Assuming a failed `ping` means the host is down — many hosts/firewalls block ICMP deliberately while everything else works fine (Module 08 covers this); always confirm with a port-level check (step 5) before concluding a host is unreachable.

## Security Perspective

This same layered method is exactly how a defender investigates "why can't the monitoring server reach the web server" or "why did an alert say a service was down" — troubleshooting and defensive investigation use identical reasoning, just with a different question motivating it.

## Exercise

Before the lab, write out — from memory — the 6-step checklist above in your own words, without looking back at this lesson.

## Further Reading

- [RFC 1123 — Requirements for Internet Hosts](https://www.rfc-editor.org/rfc/rfc1123) (background reference)
- `man ping`, `man dig`, `man nc`
