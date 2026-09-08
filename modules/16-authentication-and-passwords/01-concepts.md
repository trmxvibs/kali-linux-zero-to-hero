# Lesson 16.1 — Why Password Storage Is Harder Than It Looks

## Learning Objectives

- Explain why passwords must be hashed, never encrypted (Module 10 revisited)
- Explain salting and why it matters
- Explain why general-purpose fast hashes (SHA-256, MD5) are unsuitable for password storage specifically
- Understand password-specific hashing algorithms (bcrypt, scrypt, Argon2) conceptually
- Understand authentication factors and multi-factor authentication

## Prerequisites

Module 10 (hashing vs. encryption), Module 14 (authentication in a web context).

## Concept

**Plain language:** Module 10 established that passwords are *hashed*, not encrypted, because hashing is one-way. This lesson goes one level deeper: not all hashing is equally suitable for *this specific job* — and the reason why is entirely about speed.

**Technical — the core problem with fast hashes for passwords:** SHA-256 is *designed* to be fast — that's exactly right for verifying file integrity (Module 10, Module 22) but exactly wrong for password storage. If an attacker obtains a database of SHA-256 password hashes, a modern GPU can compute billions of SHA-256 hashes per second — meaning short or common passwords can be brute-forced or matched against precomputed lists (**rainbow tables**) almost instantly.

**Tested and confirmed during this course's build**, using `labs/password-security/hashing_demo.py`: a target password hashed with plain SHA-256 was matched against a 5-word test list in **0.000007 seconds**. A real attack scales this to billions of attempts per second against millions of leaked hashes — the arithmetic only gets worse for the defender as hardware improves.

### Salting

**Tested and confirmed**: hashing the identical password `"password123"` with two different random salts produced two completely different hashes. Without a salt, identical passwords produce identical hashes — meaning an attacker (or anyone with database access) can immediately see which users share a password, and a single precomputed rainbow table works against every user in the database at once. A unique, random salt per user defeats both problems: rainbow tables become useless (a table would need to be precomputed per salt), and identical passwords no longer look identical in storage.

### Why Password Hashing Algorithms Exist

**bcrypt**, **scrypt**, and **Argon2** are hashing algorithms specifically designed for password storage — deliberately **slow** and **tunable** (you can increase their cost factor as hardware gets faster), unlike SHA-256's deliberate speed. This single design choice — slow by intention — is the actual defense against the brute-force math above. A password hash that takes 200ms to compute instead of a few nanoseconds turns "billions of guesses per second" into a few per second, changing the economics of an attack entirely.

> ⚠️ **Testing note:** this course's build sandbox does not have `bcrypt` or `argon2` Python libraries installed (checked directly — see `tests/TEST_LOG.md`), so this lesson describes them conceptually and points to official documentation, rather than showing live output. Verify their behavior yourself on a system where you can `pip install bcrypt` or `pip install argon2-cffi`.

### Authentication Factors

- **Something you know** — a password, a PIN
- **Something you have** — a phone (for an SMS/app code), a hardware security key
- **Something you are** — a fingerprint, face recognition

**Multi-factor authentication (MFA)** combines two or more of these categories — critically, using two passwords is *not* MFA (both are "something you know"); a password plus an authenticator app code is.

## Why It Matters

Password-related failures remain one of the most common root causes of real-world breaches: weak hashing, no salting, no MFA, and password reuse across services all compound each other. This lesson's demonstrations make the "why" concrete rather than something to take on faith.

## Common Mistakes

- Using SHA-256 (or any general-purpose hash) "because it's a hash function" without recognizing password storage has different requirements than integrity checking (Module 10/22).
- Storing passwords with a single, global salt shared by every user — this defeats the entire purpose; each user needs their own unique salt.
- Treating a password reset question ("what's your mother's maiden name?") as a real second factor — it's still "something you know," often guessable or publicly discoverable.

## Security Perspective

This module connects directly to Module 20's lab-only password-cracking exercises (which will use this exact "fast hash + wordlist" mechanic against intentionally weak, fabricated hashes) and Module 17's defensive guidance on account lockout policies and MFA enforcement.

## Exercise

Before the lab, predict: if you switch `hashing_demo.py`'s Demo 3 target password from `"letmein"` to a random 20-character string, would the crack attempt against the same small wordlist succeed or fail? Why?

## Further Reading

- [OWASP — Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)
- [NIST SP 800-63B — Digital Identity Guidelines (Authentication)](https://pages.nist.gov/800-63-3/sp800-63b.html)
