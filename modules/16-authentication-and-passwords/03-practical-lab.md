# Lab 16 — Feeling Why Password Hashing Is Different

**Environment:** Any Linux terminal with `python3` (standard library only — no internet or VM required).

## Steps

1. Run the full demonstration:
   ```bash
   python3 labs/password-security/hashing_demo.py
   ```
   Read all three demos' output carefully.

2. Confirm Demo 1's finding yourself by hashing the same string twice manually:
   ```bash
   python3 -c "import hashlib; print(hashlib.sha256(b'password123').hexdigest())"
   python3 -c "import hashlib; print(hashlib.sha256(b'password123').hexdigest())"
   ```
   Confirm both lines print the identical hash.

3. **Test the prediction from `01-concepts.md`'s exercise directly:**
   ```bash
   python3 << 'PYEOF'
   import hashlib, secrets
   target_password = secrets.token_hex(10)  # random 20-character password
   target_hash = hashlib.sha256(target_password.encode()).hexdigest()
   wordlist = ["password", "123456", "letmein", "qwerty", "admin"]
   found = None
   for word in wordlist:
       if hashlib.sha256(word.encode()).hexdigest() == target_hash:
           found = word
   print(f"Target password: {target_password}")
   print(f"Found in wordlist: {found}")
   PYEOF
   ```
   Confirm the random password is **not** found — a dictionary attack only ever succeeds against passwords that are actually in the dictionary; a hash algorithm's speed doesn't matter if the real password was never guessed at all. This is an important nuance: Demo 3 showed a *fast* hash being *quickly matched against a guess already in the list* — it did not show that SHA-256 itself is "broken." The vulnerability is about **speed at scale against likely passwords**, not about SHA-256 being reversible.

4. Time how long a much larger, realistic dictionary attack would take by extrapolation: if checking 5 words took ~0.000007 seconds, estimate (by simple multiplication, not by actually running it) roughly how long 10 million words would take on this same hardware. Compare that to how long the same 10 million attempts would take against a deliberately slow algorithm computing at, say, 100 hashes/second instead.

## Expected Result

Step 2: identical hashes both times (no randomness involved when there's no salt).
Step 3: `Found in wordlist: None` — confirmed and tested during this course's build.
Step 4: a dramatic, multiple-orders-of-magnitude difference between the two extrapolated times — this is the entire point of deliberately slow password hashing algorithms.

## Next Step

[Module 17 — Defensive Security](../17-defensive-security/README.md)
