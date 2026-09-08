# Troubleshooting — Module 16

**Demo 2's salts/hashes look different every time I run it** — this is correct and expected; `os.urandom()` generates a genuinely new random salt on every run, which is exactly the point (a fresh, unique salt per user/password).

**Confused why Demo 3 "cracking" a password doesn't mean SHA-256 is broken** — see the clarification in `03-practical-lab.md` Step 3: dictionary/wordlist attacks only succeed against passwords that are actually in the list being tried; SHA-256 remains cryptographically one-way (you can't reverse a hash back to its input directly) — the vulnerability being demonstrated is about *speed enabling attackers to try huge lists quickly*, not about reversing the hash function itself.

**`john`/`hashcat` not installed** — both are standard Kali tools; if missing, `sudo apt install john hashcat`.

**`pip install bcrypt` fails** — ensure you have a working internet connection and appropriate build tools (`sudo apt install python3-dev build-essential` if a compiled dependency fails); this wasn't testable in this course's own build sandbox for the same reason (see `tests/TEST_LOG.md`).
