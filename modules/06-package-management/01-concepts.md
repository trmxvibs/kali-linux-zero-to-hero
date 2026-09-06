# Lesson 06.1 — How Software Gets Onto Your System

## Learning Objectives

- Understand what a package manager solves that manual installation doesn't
- Understand the relationship between `apt` and `dpkg`
- Understand repositories and `sources.list`
- Understand dependency resolution

## Prerequisites

Module 02 (Kali/Debian relationship).

## Concept

**Plain language:** Installing software by hand means downloading it, figuring out what else it needs to run, installing those things too, and somehow tracking all of this so you can update or remove it later. A package manager does all of that for you, consistently, for your entire system.

**Technical — two layers:**

- **`dpkg`** is the low-level tool that actually installs/removes individual `.deb` package files and tracks what's installed. It doesn't know how to fetch anything or resolve dependencies on its own.
- **`apt`** is the higher-level tool built on top of `dpkg` — it knows about **repositories** (remote servers hosting collections of packages), resolves and installs dependencies automatically, and handles upgrades cleanly.

Almost everything in this course uses `apt`; `dpkg` is used for lower-level inspection (see `04-commands.md`) or when you have a standalone `.deb` file to install directly.

### Repositories and `sources.list`

`apt` doesn't know where to find packages until you tell it — that list of sources lives in `/etc/apt/sources.list` and `/etc/apt/sources.list.d/`. Kali's default sources point at Kali's own repositories; this is why you should never casually add third-party or "improve my Kali" scripts that add unknown repositories — an untrusted repository is effectively unrestricted code execution on your system, since `apt` runs installer scripts with elevated privileges.

### Dependency resolution

If you `apt install nmap`, and Nmap needs library X which needs library Y, `apt` figures out the full chain and installs all of it in the correct order — this is what "dependency hell" looked like before package managers existed, and what `apt` exists specifically to prevent.

### The apt workflow

```
apt update        →  refresh apt's local knowledge of what's available (does NOT install/upgrade anything itself)
apt upgrade         →  upgrade already-installed packages to newer available versions
apt full-upgrade      →  like upgrade, but will also add/remove packages if needed to complete upgrades cleanly
apt install <pkg>       →  install a new package (and its dependencies)
apt remove <pkg>          →  remove a package, keep its configuration files
apt purge <pkg>            →  remove a package AND its configuration files
apt autoremove               →  remove packages that were installed as dependencies but are no longer needed by anything
```

## Why It Matters

Module 02's very first real task (`apt update && apt full-upgrade`) only makes sense once you understand this model. Later, when Module 20 discusses vulnerable software versions, "which version is installed" and "how do I know if it's current" are both `dpkg`/`apt` questions.

## Common Mistakes

- Running `apt install` without first running `apt update` recently — you might install an outdated version, or the install might fail because your local package index is stale.
- Confusing `apt remove` (keeps config files) with `apt purge` (removes them too) — matters if you plan to reinstall later and want a truly clean slate.
- Adding random third-party repositories found in forum posts without verifying their trustworthiness — a real, documented supply-chain risk.

## Security Perspective

Package management IS a security control, not just a convenience: it's how security patches actually reach your system. A large fraction of real-world compromises trace back to unpatched, known-vulnerable software — keeping packages current (Module 02, revisited in Module 17) is one of the single highest-value defensive habits that exists, more impactful than most specific tools taught later in this course.

## Exercise

Before the lab, run `dpkg -l | wc -l` on any Debian-based system you have access to, and think about what it would take to track and update that many packages by hand.

## Further Reading

- [Debian — apt user manual](https://manpages.debian.org/apt)
- [Kali Linux — Package Management](https://www.kali.org/docs/general-use/)
