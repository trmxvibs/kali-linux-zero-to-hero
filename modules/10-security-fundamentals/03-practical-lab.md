# Lab 10 — Feeling the CIA Triad, Hands-On

**Environment:** Any Linux terminal with `openssl` (pre-installed on Kali and most Linux systems).

## Part 1 — Integrity (Hashing)

```bash
mkdir -p ~/lab10 && cd ~/lab10
echo "Original security policy v1" > policy.txt
sha256sum policy.txt
echo "Original security policy v2" > policy.txt
sha256sum policy.txt
```
Confirm the two hashes are completely different despite the file changing by only one character — this is integrity checking in action (Module 18 uses this exact idea for evidence handling).

## Part 2 — Confidentiality (Symmetric Encryption)

```bash
echo "Confidential: budget is 50000" | openssl enc -aes-256-cbc -pbkdf2 -salt -pass pass:"CorrectHorse123" -out secret.enc
openssl enc -d -aes-256-cbc -pbkdf2 -salt -pass pass:"CorrectHorse123" -in secret.enc
```
Confirm you get the original message back.

Now try the wrong password:
```bash
openssl enc -d -aes-256-cbc -pbkdf2 -salt -pass pass:"WrongPassword" -in secret.enc > /tmp/wrong_attempt.bin
echo "exit code: $?"
```
> ⚠️ **Redirect this output to a file rather than printing it directly** — a failed decrypt attempt can write a few bytes of raw binary garbage to stdout before erroring, which can visually corrupt your terminal display. This isn't dangerous, just annoying — redirecting avoids it, and was specifically how this exact command was tested during this course's build.

Confirm the exit code is non-zero and check for a "bad decrypt" message on screen (this part goes to stderr, so it prints normally even with stdout redirected).

## Part 3 — Confidentiality Without Sharing a Secret (Asymmetric Encryption)

```bash
openssl genrsa -out priv.pem 2048
openssl rsa -in priv.pem -pubout -out pub.pem
echo "Top secret finding" | openssl pkeyutl -encrypt -pubin -inkey pub.pem -out msg.enc
openssl pkeyutl -decrypt -inkey priv.pem -in msg.enc
```
Confirm the message comes back correctly — and notice you never had to transmit `priv.pem` anywhere to make this work; only `pub.pem` needs to be shareable.

## Cleanup

```bash
cd ~ && rm -rf ~/lab10 /tmp/wrong_attempt.bin
```

## Expected Result

- Part 1: two completely different SHA-256 hashes
- Part 2: correct password recovers the message exactly; wrong password fails with a non-zero exit code and a clear error
- Part 3: message recovered correctly using only the private key, having encrypted with only the public key

## Next Step

[Module 11 — Reconnaissance Concepts](../11-reconnaissance-concepts/README.md) (if not already completed) or [Module 12 — Network Enumeration](../12-network-enumeration/README.md).
