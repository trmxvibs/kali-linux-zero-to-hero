# Security Notes — Module 16

- **Password reuse compounds every other weakness in this module.** Even a well-hashed, well-salted password becomes worthless the moment it's reused on a service that gets breached elsewhere and the plaintext leaks — this is why password managers and unique passwords per service are standard, widely recommended defensive advice.
- **MFA is one of the highest-value defensive controls available**, precisely because it doesn't rely on the password being strong at all — even a guessed or leaked password is insufficient alone if a second factor is required.
- **Account lockout / rate limiting policies** (Module 17 revisits this) are what actually stop the "billions of guesses per second" math from Lesson 16.1 in a real login system — even a fast hash matters less if the login endpoint itself throttles or locks out repeated failed attempts.
- **This module's cracking demonstration used only fabricated, self-generated test data.** Running `john`/`hashcat` against real password hashes requires the exact same authorization standard as any other tool in this course (Module 00) — obtained hashes from a system you don't own or lack explicit authorization for are off-limits, full stop.

> ⚠️ **LAB ONLY** — every hash cracking exercise in this course, including Module 20's follow-up, uses fabricated or explicitly authorized test data only.
