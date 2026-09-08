# Challenge — Module 16

Extend `labs/password-security/hashing_demo.py` with a fourth demonstration:
- Generate 1,000 random fake "users," each with a randomly chosen password from a small set of 20 common passwords (so some collisions are guaranteed)
- Hash all of them without a salt, and count how many *distinct* hash values exist (should be ≤ 20, revealing the collisions directly, as Demo 1 predicted at small scale)
- Then hash all of them again, this time with a unique random salt per user, and confirm the distinct-hash count now equals 1,000 (no revealed collisions)
- Print both counts clearly, and explain in a comment why this scales the "reveals password reuse" problem from Demo 1 to a much more realistic, larger example

Test your script fully before considering it complete.
