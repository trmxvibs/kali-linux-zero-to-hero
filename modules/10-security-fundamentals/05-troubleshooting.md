# Troubleshooting — Module 10

**Terminal looks garbled/corrupted after a command** — you likely printed raw binary output directly to the terminal (e.g., a failed decrypt attempt, as noted in `03-practical-lab.md`). Type `reset` and press Enter (even if you can't read what you're typing) to restore the terminal.

**`openssl enc` warns about deprecated options or asks about the `-pbkdf2` flag** — different OpenSSL versions have changed defaults around key derivation; the `-pbkdf2` flag used in this module's examples is the modern, recommended approach and should work on any reasonably current OpenSSL.

**Wrong-password decrypt doesn't fail** — double check you actually changed the password string between encrypt and decrypt; if both commands used the same password, success is correct and expected.

**RSA key generation seems slow** — 2048-bit RSA key generation can take a few seconds depending on system entropy/CPU; this is normal.
