# Lesson 00.1 — What This Course Is (and Isn't)

## Learning Objectives

By the end of this lesson you will understand:

- The difference between "tool memorization" and "security understanding"
- Why every lesson in this course follows the same fixed structure
- How Level 0 → Level 4 progression works
- What you need before you start Module 01

## Prerequisites

None. This is the starting point.

## Concept

**Plain language first:** Most free "Kali Linux tutorials" show you a command, tell you to copy it, and move on. You end up able to type `nmap -sV target` without knowing what a port is, why the scan works, or what to do if it fails. That's not a skill — it's a script you'll forget in a week.

This course does the opposite. Every tool is introduced only after you understand the concept it depends on. You will not run `nmap` until you already understand IP addresses, ports, and the TCP handshake — because otherwise the tool's output is just noise.

**Technical explanation:** The course is organized as a dependency graph, not a tool list. Linux fundamentals (Modules 01–07) exist so that networking (08–09) makes sense. Networking exists so that reconnaissance and enumeration (11–13) make sense. Security fundamentals (10) exist so that vulnerability assessment (15) and exploitation labs (20) are understood as *methodology*, not magic. Automation (21–22) comes after you've done things manually enough times to know what's worth automating.

## Why It Matters

In real security work — offensive or defensive — the tool is the easy part. The hard part is knowing *why* a result matters, whether it's a false positive, what it would mean to a defender, and whether testing it is even legal. A course that skips straight to tools produces people who can run scanners but can't explain a finding, which is not a hireable or a safe skill.

## How Every Module Is Structured

Each module folder contains up to 8 files, always in this order:

1. `01-concepts.md` — the idea, explained simply first, then technically
2. `02-installation.md` — anything you need to set up (skipped if nothing to install)
3. `03-practical-lab.md` — a reproducible, hands-on exercise
4. `04-commands.md` — the actual commands/tools, each with 10+ points of context (see below)
5. `05-troubleshooting.md` — fixes for the errors beginners actually hit
6. `06-security-notes.md` — legal, ethical, and defensive context
7. `07-exercises.md` — practice tasks (no answers given immediately)
8. `08-challenge.md` — a harder, more open-ended task

Every command or tool that appears in `04-commands.md` is covered from these angles: what it is, why it exists, what problem it solves, how it works conceptually, basic usage, a practical example, expected output, how to read that output, common mistakes, troubleshooting, defensive implications, and the legal/ethical boundary for using it.

## The Four Levels

- **Level 0 (Modules 00–02):** You've never opened a terminal. Start here regardless of your background.
- **Level 1 (Modules 03–09):** Core Linux and networking skills, no security content yet.
- **Level 2 (Module 10):** Security vocabulary and mental models, before any tool use.
- **Level 3 (Modules 11–20):** Hands-on labs using Kali tools, always against systems built for this purpose.
- **Level 4 (Modules 21–29):** Automation, methodology, reporting, and where to go after this course.

You cannot skip Level 0 and succeed at Level 3 — the labs assume you're comfortable with the terminal, permissions, and networking basics.

## Common Mistakes

- Skipping to Module 11 (reconnaissance) because it "sounds more interesting" than filesystem permissions. You will not understand the output of the tools without Modules 01–09.
- Treating exercises as optional. The exercises are where the actual learning happens — reading a lesson is not the same as doing the lab.
- Running lab commands against a real, non-lab target "just to see." Don't. See `06-security-notes.md`.

## Troubleshooting

If a module's exercises feel too easy, do the challenge in `08-challenge.md` before moving on — it's designed to expose gaps the base exercise doesn't catch.

If a module feels too hard, go back one module. The dependency graph is real: most confusion at Level 3 traces back to a shaky Level 1 concept.

## Security Perspective

The entire course is built around one rule, spelled out fully in `06-security-notes.md`: **only test systems you own or are explicitly authorized to test.** This isn't a legal disclaimer bolted on afterward — it shapes which labs exist at all. Every vulnerable target used in this course (Metasploitable, DVWA, Juice Shop, WebGoat) is software deliberately built and published for this exact purpose.

## Exercise

Before moving to Module 01, write down (in a notes file, not submitted anywhere) one sentence answering: "What do I want to be able to do after finishing this course?" Keep it. Revisit it at Module 28.

## Further Reading

- [Kali Linux official documentation](https://www.kali.org/docs/)
- [OWASP](https://owasp.org/)
