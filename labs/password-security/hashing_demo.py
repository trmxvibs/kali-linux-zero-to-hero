#!/usr/bin/env python3
"""
hashing_demo.py

Purpose: Demonstrate, concretely, why plain fast hashing (e.g. bare
SHA-256) is unsuitable for password storage, and why salting matters.

Used in: Module 16 (Authentication & Password Security)

This script only ever hashes fabricated demo passwords locally — no real
credentials, no network, no external service.
"""

import hashlib
import os
import time


def demo_no_salt_reveals_matches():
    print("=== Demo 1: identical passwords produce identical hashes without a salt ===")
    pw = "password123"
    h1 = hashlib.sha256(pw.encode()).hexdigest()
    h2 = hashlib.sha256(pw.encode()).hexdigest()
    print(f"  Hash 1: {h1}")
    print(f"  Hash 2: {h2}")
    print(f"  Identical: {h1 == h2}")
    print("  Problem: if two users share a password, this leaks that fact")
    print("  directly from the stored hashes, even without cracking anything.\n")


def demo_salting_fixes_that():
    print("=== Demo 2: a per-user random salt hides that fact ===")
    pw = "password123"
    salt1 = os.urandom(16).hex()
    salt2 = os.urandom(16).hex()
    h1 = hashlib.sha256((salt1 + pw).encode()).hexdigest()
    h2 = hashlib.sha256((salt2 + pw).encode()).hexdigest()
    print(f"  Hash 1 (salt {salt1[:8]}...): {h1}")
    print(f"  Hash 2 (salt {salt2[:8]}...): {h2}")
    print(f"  Identical: {h1 == h2}")
    print("  The same password now produces completely different stored")
    print("  values, because each user's salt is different.\n")


def demo_fast_hash_is_crackable():
    print("=== Demo 3: a fast general-purpose hash is trivially brute-forceable ===")
    target_password = "letmein"
    target_hash = hashlib.sha256(target_password.encode()).hexdigest()
    wordlist = ["password", "123456", "letmein", "qwerty", "admin"]

    start = time.time()
    found = None
    for word in wordlist:
        if hashlib.sha256(word.encode()).hexdigest() == target_hash:
            found = word
            break
    elapsed = time.time() - start

    print(f"  Target hash: {target_hash}")
    print(f"  Cracked password: {found!r} in {elapsed:.6f} seconds")
    print("  against a wordlist of only 5 entries.")
    print("  Real attacks use lists of millions of entries; SHA-256 alone")
    print("  computes fast enough that this remains cheap at scale.")
    print("  This is exactly why password-specific hashing (bcrypt, scrypt,")
    print("  Argon2) is deliberately slow and tunable — see 01-concepts.md.\n")


if __name__ == "__main__":
    demo_no_salt_reveals_matches()
    demo_salting_fixes_that()
    demo_fast_hash_is_crackable()
