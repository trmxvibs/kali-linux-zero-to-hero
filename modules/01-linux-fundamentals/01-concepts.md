# Lesson 01.1 — The Linux Mental Model

## Learning Objectives

- Explain what an operating system kernel does, in plain terms
- Understand "everything is a file" and why it matters
- Understand the shell vs. the terminal vs. the kernel
- Understand the basic Linux directory layout

## Prerequisites

Module 00 completed.

## Concept

**Plain language first:** Your computer's operating system has two jobs: manage hardware (CPU, memory, disk, network card) and let programs run without stepping on each other. Linux is the "kernel" — the core program that does this. Everything else you associate with Kali (the terminal, the desktop, the tools) is software running *on top of* that kernel.

When you type a command, you're not talking to the kernel directly. You're talking to a **shell** (usually `bash`) — a program whose only job is to read what you type, figure out what you mean, and ask the kernel (or other programs) to do it. The **terminal** is just the window that lets you type into the shell.

**Technical explanation:** Linux follows a design philosophy where almost everything — regular files, directories, hardware devices (`/dev/sda`), running processes (`/proc/1234`), even network sockets — is represented and interacted with as a file. This is why a huge number of Linux tools just read and write files: there's one consistent interface instead of a different API for every kind of resource.

The filesystem is arranged in a single tree starting at `/` (root) — there's no concept of `C:\` and `D:\` like Windows. Key locations:

| Path | Purpose |
|---|---|
| `/` | Root of everything |
| `/home/<user>` | Your personal files |
| `/etc` | System-wide configuration files |
| `/bin`, `/usr/bin` | Programs (executables) |
| `/var` | Variable data — logs, caches, spool files |
| `/tmp` | Temporary files, often cleared on reboot |
| `/root` | The root (administrator) user's home directory |
| `/proc` | A virtual filesystem exposing running process info |

## Why It Matters

Kali Linux tools assume you understand this model. Log files live in `/var/log`. Configuration for services (like SSH) lives in `/etc`. When a tool "doesn't work," 80% of the time the fix is understanding *where* something lives and *why*, not memorizing a new command.

## Common Mistakes

- Assuming Linux has "drives" like Windows — it has one tree, and external drives get *mounted* into that tree (e.g., at `/media/usb`).
- Confusing the terminal (the window) with the shell (the program interpreting your commands) with the kernel (the thing actually doing the work).
- Editing files in `/etc` without understanding what reads them, then being surprised when nothing changes until a service restarts.

## Security Perspective

Because "everything is a file," a huge amount of Linux security comes down to controlling **who can read/write which files** — this is exactly what Module 04 (Filesystem & Permissions) and Module 05 (Users & Processes) cover. Attackers and defenders both spend enormous amounts of time thinking about file permissions, because misconfigured permissions are one of the most common real-world vulnerabilities.

## Exercise

Without running anything yet, predict: which of `/etc`, `/home`, `/tmp`, `/var/log` would you expect an attacker to check first after gaining access to a machine, and why? Write one sentence per directory.

## Further Reading

- [Filesystem Hierarchy Standard (FHS)](https://refspecs.linuxfoundation.org/FHS_3.0/fhs/index.html)
- `man hier` (run this once you have a Linux terminal — Lesson 01.2)
