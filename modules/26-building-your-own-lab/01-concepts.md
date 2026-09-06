# Lesson 26.1 — Designing an Isolated Security Lab

## Learning Objectives

- Understand why network isolation is the single most important lab-safety control
- Understand the difference between NAT, Host-only/Internal, and Bridged virtual networking modes
- Design a lab topology matching this course's needs
- Understand snapshots and why they matter for reproducibility

## Prerequisites

Module 02 (Kali Fundamentals), Module 08 (Networking).

## Concept

**Plain language:** A "lab" in this course means a small set of virtual machines that can talk to each other but **cannot reach, and cannot be reached by, anything outside that virtual network** — not your home Wi-Fi, not the internet, nothing. This single property is what makes every exercise in Modules 11–20 safe to run without needing to worry about accidentally scanning or exploiting a real system.

**Technical — virtual networking modes** (naming varies slightly by hypervisor, e.g., VirtualBox vs. VMware, but the concepts are universal):

| Mode | Can reach internet? | Can reach host machine? | Can reach other VMs on same virtual network? | Reachable from outside? |
|---|---|---|---|---|
| **NAT** | Yes (via host) | No (by default) | No (each VM gets its own NAT) | No |
| **Host-only / Internal** | No | Host-only: yes. Internal: no. | Yes | No |
| **Bridged** | Yes (as if a physical device on your LAN) | Yes | Yes | **Yes — avoid for lab targets** |

For this course's labs, the target architecture is:

```text
        [ Your physical machine / host ]
                     |
        (Host-only or Internal virtual network — no internet route)
                     |
        +------------+-------------+
        |                          |
  [ Kali VM ]              [ Metasploitable VM ]
  (attacker/tester)         (intentionally vulnerable target)
```

Both VMs' network adapters are set to the **same Host-only or Internal network**, and neither is Bridged to your physical network. This means:
- Kali can reach Metasploitable (needed for every lab)
- Metasploitable cannot reach the internet (it's deliberately full of old, vulnerable software — you don't want it exposed to anything)
- Nothing on your physical network, or the internet, can reach either VM

## Why It Matters

This is not a formality — it's the control that makes "just try it and see" pedagogically safe. Every lab in Modules 11–20 assumes this topology. Skipping it is the single most common way a beginner accidentally does something they didn't intend (e.g., accidentally scanning their home router or a shared network at work/school).

## Common Mistakes

- Setting a VM's adapter to "Bridged" for convenience (to get internet access "just this once") and forgetting to change it back before running an active lab.
- Assuming "private IP address" (`192.168.x.x`) automatically means isolated — a Bridged adapter can still get a private-looking address that's fully reachable by everything else on your real LAN.
- Not taking a snapshot before the first lab, then being unable to reset a target VM after a lab that intentionally leaves it in a broken/compromised state.

## Security Perspective

This module is where "authorization" (Module 00, Module 10) becomes a concrete network diagram instead of an abstract rule. If you can point to your lab's network settings and confirm no route exists to anything you don't own, you've operationalized the course's core ethical rule, not just agreed to it in principle.

## Exercise

Sketch (on paper) the network topology you'll build, labeling each VM's network adapter mode. Before your next lab, physically verify (in your hypervisor's settings, not from memory) that it matches what you sketched.

## Further Reading

- [VirtualBox networking modes (official docs)](https://www.virtualbox.org/manual/ch06.html)
- [Metasploitable 2 documentation](https://docs.rapid7.com/metasploit/metasploitable-2/)
