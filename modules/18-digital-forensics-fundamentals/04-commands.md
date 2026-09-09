# Lesson 18.2 — Forensic Analysis Commands

All commands on this page were actually executed during this course's build — see the exact output samples in `01-concepts.md`.

## `sha256sum` / `md5sum` — evidence integrity

```bash
sha256sum evidence.file                    # hash the file
sha256sum evidence.file >> chain.txt         # append to a chain-of-custody record
diff <(sha256sum original.file) <(sha256sum copy.file)  # compare two files directly
```
Use `sha256sum` (not MD5) for any integrity work where collision resistance matters — MD5 is cryptographically broken for this purpose (Module 10), though it remains fast and useful for quick non-security-critical checksums.

## `file` — type identification by content

```bash
file suspicious_file                   # report what the file actually is
file -i suspicious_file                  # MIME type output — useful in scripts
file /tmp/* 2>/dev/null                    # bulk-check everything in a directory
```

**Reading `file` output (tested during this course's build):**
- `ELF 64-bit LSB pie executable` → a compiled Linux program (not a document)
- `ASCII text` → plain text file
- `Bourne-Again shell script, ASCII text executable` → a bash script
- A fake PNG correctly identified as `ASCII text` → the content didn't match the PNG magic number, revealing the extension was misleading

## `strings` — extract human-readable content

```bash
strings binary_or_unknown_file
strings -n 8 file          # only strings of 8+ characters (reduces noise)
strings file | grep -i "password\|key\|secret\|http"   # grep for interesting patterns
```

## `stat` — full timestamp and inode information

```bash
stat filename
```
**Tested output (abbreviated):**
```
File: /etc/passwd
Size: 1164   Blocks: 8   IO Block: 4096   regular file
Access: 2026-09-08 02:53:58
Modify: 2026-09-08 02:53:58
Change: 2026-09-08 02:53:58
Birth:  2026-09-08 02:53:58
```

## `find` with timestamps (timeline reconstruction)

```bash
find / -newer /tmp/reference_file -type f 2>/dev/null    # files modified AFTER a reference point
find / -mtime -1 -type f 2>/dev/null                       # files modified in the last 24 hours
```

## Using `file_hash_generator.py` (Module 22 — reused here)

```bash
python3 scripts/python/file_hash_generator.py evidence.file
python3 scripts/python/file_hash_generator.py evidence.file --algo sha256
```
Already built and tested in Module 22 — this is one of the explicit use cases it was designed for.

## Further Reading

- `man file`, `man strings`, `man stat`, `man find`
