# Lesson 10.2 — Seeing Encryption and Hashing Work

These commands make the abstract concepts (confidentiality via encryption, integrity via hashing) concrete. All examples on this page were actually executed during this course's build using `openssl`.

## Hashing — for integrity, not secrecy

**What/why:** A hash function takes input of any size and produces a fixed-size fingerprint. The same input always produces the same hash; changing even one character produces a completely different hash (Module 22 covered this as the "avalanche effect"). Hashing is **one-way** — you can't recover the original input from the hash.

```bash
echo -n "hello world" | openssl dgst -sha256
```
**Tested output:**
```
SHA2-256(stdin)= b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9
```
**Common mistake:** Calling hashing "encryption" — it isn't; there's no key and no way to reverse it. Password *storage* (Module 16) uses specialized, deliberately slow hashing (bcrypt/Argon2), not general-purpose hashes like SHA-256, for reasons Module 16 explains.

## Symmetric Encryption — one shared secret

**What/why:** The same key both encrypts and decrypts. Fast, but requires securely sharing that key with everyone who needs to decrypt.

```bash
echo "secret message" | openssl enc -aes-256-cbc -pbkdf2 -salt -pass pass:testpass123 -out encrypted.bin
openssl enc -d -aes-256-cbc -pbkdf2 -salt -pass pass:testpass123 -in encrypted.bin
```
**Tested and confirmed:** decrypting with the correct password reproduces `secret message` exactly; decrypting with a wrong password fails cleanly with a `bad decrypt` error and a non-zero exit code — confirmed directly during this course's build. This failure mode (immediate, obvious failure with a wrong key) is intentional and desirable — silent wrong output would be far worse.

## Asymmetric Encryption — two different keys

**What/why:** A **public key** (shareable with anyone) encrypts; only the matching **private key** (kept secret) can decrypt. This solves symmetric encryption's key-sharing problem — you never need to transmit a secret key at all. This is the foundation of TLS/HTTPS (Module 08, Module 14).

```bash
openssl genrsa -out private.pem 2048
openssl rsa -in private.pem -pubout -out public.pem
echo "hello" | openssl pkeyutl -encrypt -pubin -inkey public.pem -out encrypted.bin
openssl pkeyutl -decrypt -inkey private.pem -in encrypted.bin
```
**Tested and confirmed:** the message encrypted with the public key was correctly recovered using only the private key — the public key alone cannot decrypt its own output, which is the entire point.

## Why This Matters for Later Modules

- Module 14 (Web Security): HTTPS/TLS uses asymmetric encryption to establish a connection, then switches to fast symmetric encryption for the actual data — understanding both pieces here demystifies "why does HTTPS need a certificate at all."
- Module 16 (Password Security): explains why passwords are *hashed*, never *encrypted*, and why that distinction matters even though both sound similar.
- Module 18 (Forensics): file hashing (already used in Module 22's `file_hash_generator.py`) is this exact same one-way hash concept, applied to integrity verification instead of passwords.

## Further Reading

- `man openssl`, `man openssl-dgst`, `man openssl-enc`
- [NIST — Cryptographic Standards and Guidelines](https://csrc.nist.gov/projects/cryptographic-standards-and-guidelines)
