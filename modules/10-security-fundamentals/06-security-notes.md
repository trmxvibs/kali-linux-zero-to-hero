# Security Notes — Module 10

- This entire module *is* the security-notes content for the rest of the course — the CIA triad, vulnerability/exploit/threat/risk, authentication/authorization, defense in depth, least privilege, and attack surface are the vocabulary every later module's security notes assume you already have.
- **A specific, common real-world mistake this module directly prevents:** treating every vulnerability scanner finding as equally urgent. Module 15 and Module 25 will hold you to actually assessing *risk* (likelihood × impact), not just reporting "a vulnerability was found."
- **Hashing vs. encryption confusion is a real, recurring security bug source** — systems that "encrypt" passwords (reversible) instead of hashing them (one-way) are a well-documented category of vulnerability; Module 16 revisits this directly.

> ⚠️ Every cryptographic example in this module operates on your own local test files — no external system or network transmission is involved.
