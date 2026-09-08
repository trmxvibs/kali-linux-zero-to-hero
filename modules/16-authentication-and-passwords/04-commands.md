# Lesson 16.2 — Running the Password Security Demonstrations

## This Course's Hashing Demo (tested and runnable now)

```bash
python3 labs/password-security/hashing_demo.py
```
**Tested output, exactly as produced during this course's build** (abridged):
```
=== Demo 1: identical passwords produce identical hashes without a salt ===
  Hash 1: ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f
  Hash 2: ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f
  Identical: True

=== Demo 2: a per-user random salt hides that fact ===
  Hash 1 (salt 724283dc...): e42282037165841ff88f059fa4a3c2c3c1c7bd042efaec8ac764516719a8319f
  Hash 2 (salt 51600bd0...): 8205cf36de8b09a9332ac9355e17839bcca199a2878a1c713ed3188143355133
  Identical: False

=== Demo 3: a fast general-purpose hash is trivially brute-forceable ===
  Cracked password: 'letmein' in 0.000007 seconds
```
(Your own run will show different salt values and a slightly different timing, since salts are randomly generated each run — the *pattern*, not the exact numbers, is what matters.)

## `john` (John the Ripper) — Kali's built-in password cracker

> ⚠️ **Testing note:** `john` is a standard pre-installed Kali tool, not available in this course's build sandbox. Documented from official usage; not live-executed.

```bash
john --wordlist=/usr/share/wordlists/rockyou.txt hashes.txt      # dictionary attack against a hash file
john --show hashes.txt                                              # show any hashes already cracked
```
> ⚠️ **LAB ONLY** — only ever run this against hashes you own or have explicit authorization to test (e.g., your own fabricated test hashes, or an authorized engagement's confirmed-in-scope data). Module 20 covers this properly in a controlled lab context.

## `hashcat` — GPU-accelerated password cracking

```bash
hashcat -m 0 -a 0 hashes.txt wordlist.txt        # -m 0 = MD5, -a 0 = dictionary attack mode
```
Full mode/hash-type reference: [hashcat wiki](https://hashcat.net/wiki/).

## Python's `hashlib` for your own experiments (tested, standard library only)

```python
import hashlib
hashlib.sha256(b"some password").hexdigest()
```
Already demonstrated fully in `labs/password-security/hashing_demo.py` above.

## Further Reading

- [John the Ripper — official documentation](https://www.openwall.com/john/doc/)
- [Hashcat — official wiki](https://hashcat.net/wiki/)
- `man hashlib` (Python) — actually `python3 -c "help('hashlib')"` since it's a Python module, not a shell command
