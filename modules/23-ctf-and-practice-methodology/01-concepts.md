# Lesson 23.1 — CTF Methodology and Structured Practice

## Learning Objectives

- Understand what a CTF (Capture The Flag) is and how it differs from real security work
- Apply a structured methodology to CTF challenges instead of guessing
- Know the major CTF categories and which modules of this course prepared you for each
- Know the best free platforms for ongoing practice

## Prerequisites

Modules 00–22 (the entire technical curriculum — this module synthesises it all into a practice context).

## Concept

**Plain language:** A CTF is a structured, legal, intentionally-designed puzzle competition where participants solve security challenges to find a "flag" — a specific string proving you solved the challenge. CTFs are one of the best ways to practice skills from this course in an environment that is always authorized, always scoped, and always has a known correct answer.

**Technical — how CTFs work:**

A flag is typically a string in a known format, e.g. `FLAG{some_text_here}` or `CTF{md5hash}`. You find it by solving a challenge — which could be anything from decoding a file, to exploiting a web app, to reversing a binary. Some CTFs are "Jeopardy-style" (pick challenges from a board, solve in any order) and some are "Attack-Defense" (teams both attack and defend live systems simultaneously, more advanced).

### The Five Major CTF Categories → Course Coverage

| Category | What it tests | This course's preparation |
|---|---|---|
| **Web** | HTTP, injection flaws, auth bypasses, OWASP Top 10 | Module 14 (Web Security), Module 20 (exploitation) |
| **Forensics** | File analysis, steganography, log analysis, packet captures | Module 13 (Traffic Analysis), Module 18 (Forensics) |
| **Cryptography** | Encryption/hashing weaknesses, protocol flaws | Module 10 (crypto concepts), Module 16 (password hashing) |
| **Reverse Engineering** | Binary analysis, `strings`, understanding compiled code | Module 18 (`strings`, `file`) |
| **Networking/Recon** | Enumeration, service analysis, packet inspection | Modules 08–12 |

### The CTF Methodology — four steps before giving up

1. **Enumerate** — what is given? What format is it? What tools might apply? (Module 12's enumeration mindset)
2. **Research** — has this specific challenge type appeared before? Look for write-ups (after the competition ends) or related techniques
3. **Hypothesis-test** — pick the most likely approach, apply it, observe the result, adjust — don't randomly try tools
4. **Document as you go** — what you tried, what failed, what worked — this habit directly transfers to real assessment reporting (Module 25)

## Why It Matters

CTFs provide the one thing no course can fully replicate: completely authorized, consequence-free practice on real-feeling challenges with immediate feedback on whether your approach was correct. The skills atrophy without use; CTFs keep them sharp.

## Common Mistakes

- Reaching for tools before understanding what type of challenge it is — tool-first thinking produces random results
- Not reading write-ups after a competition ends — write-ups are where you learn techniques you didn't know existed
- Treating CTF skills as identical to real assessment skills — CTFs are gamified, with guaranteed solvability and known flags; real assessments are messier, open-ended, and have no answer key

## Further Reading

- [CTFtime.org](https://ctftime.org/) — calendar and archive of CTF events worldwide
- [picoCTF](https://picoctf.org/) — beginner-friendly, always available
- [HackTheBox](https://www.hackthebox.com/) — intermediate/advanced, retired machines have write-ups
- [TryHackMe](https://tryhackme.com/) — beginner-friendly guided rooms
