# Lesson 07.1 — How Services Start, Run, and Get Managed

## Learning Objectives

- Understand what `systemd` is and why modern Linux uses it
- Understand units, especially services
- Understand enabled vs. active, and why they're different questions
- Understand where scheduled tasks (cron) fit in

## Prerequisites

Module 05 (processes) — a service is, at its core, a specially-managed long-running process.

## Concept

**Plain language:** When you boot a Linux machine, something has to start the network, start SSH so you can log in remotely, start any databases or web servers, and so on — in the right order, restarting things that crash, and letting you query "is X running?" cleanly. `systemd` is the modern Linux component that does this job on Kali, Ubuntu, Debian, and most current distributions.

**Technical:** `systemd` manages **units** — services, but also mount points, timers, sockets, and more. A **service unit** describes one long-running program: how to start it, stop it, restart it on failure, and what other units it depends on.

### Enabled vs. Active — two different questions

- **Active** = is it running *right now*?
- **Enabled** = will it start *automatically at boot*?

A service can be active-but-not-enabled (you started it manually, it won't survive a reboot), or enabled-but-not-active (it's set to start at boot, but you've stopped it for now, or it hasn't booted since being enabled). Confusing these two is one of the most common sysadmin mistakes — "I disabled it but it's still running" usually means you disabled (future boot behavior) without stopping (current state).

### Logs — `journalctl`

Modern systemd systems centralize logs into the **journal**, queried with `journalctl`, rather than (or in addition to) traditional flat files in `/var/log`. This is the primary tool for both troubleshooting a service and, defensively, reviewing what a service has been doing (Module 17).

### Scheduled tasks — `cron`

Not everything is a long-running service — some things should run *at a specific time* or *on a schedule* (a nightly backup, an hourly cleanup script). `cron` is the traditional Linux scheduler for this; each user can have their own **crontab** (a list of scheduled commands), and there's also a system-wide crontab for admin-level scheduled tasks.

## Why It Matters

Nearly every "is this system exposed" question from Module 08/Module 11 onward eventually comes back to a *service* — SSH, a web server, a database — and services are exactly what this module teaches you to inspect and control. Module 17 (Defensive Security) builds directly on `systemctl status`/`journalctl` as core investigative tools.

## Common Mistakes

- Confusing `systemctl stop` (current session only) with `systemctl disable` (future boots only) — use both together if you want a service fully off now and forever.
- Assuming a service is safe just because it's "always been running" — an unused, unpatched service is exactly the kind of forgotten attack surface Module 17 teaches you to look for.
- Not checking logs (`journalctl -u <service>`) before assuming a service "just doesn't work" — the log almost always explains why.

## Security Perspective — Attacker View vs Defender View

**Attacker:** What services are running that shouldn't be? What can be learned about a system from its running/enabled services?
**Defender:** What's my actual service footprint? Is anything enabled that I don't remember intentionally turning on? (`systemctl list-unit-files --state=enabled` is the direct, practical answer to that question.)

## Exercise

Before the lab, write down (from memory, no lookup) what you predict `systemctl status ssh` will show on a system where SSH has never been explicitly started or enabled.

## Further Reading

- [systemd — official documentation](https://www.freedesktop.org/wiki/Software/systemd/)
- `man systemctl`, `man journalctl`, `man 5 crontab`
