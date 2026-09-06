# Ethics, Legal Boundaries & Responsible Use

This document is the full version of the rules summarized in
[Module 00 — Orientation](../../modules/00-orientation/06-security-notes.md).
Every lab, script, and lesson in this repository is built to comply with it.

## The Core Principle

**Security skills are dual-use.** Everything you learn here — port scanning, web
vulnerability testing, password auditing — can be used to protect systems or to
damage them. This course exists on the belief that broad access to this
knowledge, taught with a strong ethical foundation, produces more defenders
and fewer victims. That belief only holds if the ethical foundation is taken
seriously, not treated as boilerplate.

## Authorization

You may only test:

- Systems, applications, and networks **you personally own**
- Systems you have **explicit, documented, written** authorization to test (e.g.,
  a signed scope-of-work for professional engagements, or a bug bounty
  program's published scope)
- Deliberately vulnerable training software published for this purpose:
  **Metasploitable, DVWA, OWASP Juice Shop, WebGoat**, and similar, run in an
  isolated lab you control (Module 26)

Verbal permission from someone who doesn't own or administer the system does
not count as authorization. "It was publicly accessible" does not count as
authorization. Curiosity is not authorization.

## Scope Discipline

Even with authorization, stay inside the agreed scope:

- Test only the systems/IP ranges/applications explicitly listed
- Don't pivot to "nearby" systems out of curiosity
- Stop and re-confirm scope if you discover something unexpected (e.g., a
  shared hosting environment where your target shares infrastructure with
  systems that are *not* in scope)

## Responsible Disclosure

If you discover a real vulnerability in something you don't own, outside of
this course's labs:

1. Do the minimum necessary to confirm the vulnerability is real — don't go
   further than proof-of-concept.
2. Don't access, copy, exfiltrate, or modify data that isn't yours, even to
   "prove impact."
3. Report through the vendor's official security contact, a security.txt
   file, or a recognized bug bounty platform.
4. Give the vendor reasonable time to fix the issue before any public
   disclosure (commonly 90 days, but follow the vendor's or platform's stated
   policy).
5. Never demand payment as a condition of disclosure — that can constitute
   extortion, a serious crime, regardless of your intent.
6. If a situation feels legally ambiguous, stop and consult a lawyer before
   acting further. This course cannot give you legal advice, and laws vary
   significantly by country and state.

## Privacy

- Never use real people's private data in exercises. Sample data in this
  repository's labs is fabricated (fictional names, RFC 5737 documentation
  IP ranges like `203.0.113.0/24`, etc.).
- If a lab you build for yourself involves real logs or real data, treat it
  with the same care as any sensitive data in your professional life —
  don't commit it to a public repository.

## What This Course Will Never Teach

- How to attack a system you don't own or aren't authorized to test
- Credential theft or cracking against real accounts
- Malware development or deployment
- Techniques whose primary purpose is evading detection for malicious ends
- Denial of service against real infrastructure

## If You're Unsure

Ask: "If the system owner, a judge, and my own conscience were all watching
me do this right now, would I still do it?" If the answer isn't a clear yes,
stop.

## Reporting Problems With This Course

If you find guidance in this repository that seems to conflict with this
document, please open an issue — see [CONTRIBUTING.md](../../CONTRIBUTING.md).
That is a documentation bug we want to fix.
