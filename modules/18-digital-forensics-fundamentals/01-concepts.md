# Lesson 18.1 — Fundamentals of Digital Evidence

## Learning Objectives

- Understand why preserving evidence integrity comes before analyzing it
- Understand how `file` determines file type (magic bytes vs. file extension)
- Understand timestamps and what they do/don't prove
- Apply `strings`, `stat`, and hash tools to basic evidence examination

## Prerequisites

Module 10 (hashing = integrity verification), Module 22 (`file_hash_generator.py`).

## Concept

**Plain language:** Digital forensics is the disciplined process of finding, preserving, and analyzing digital evidence in a way that the results can be trusted — including by a court. The discipline around this exists because digital files are trivially modified, and without proof that a file hasn't changed since it was collected, the analysis is worthless.

**Technical — the integrity-first principle:** before anything else, hash the evidence. After anything else, hash it again. If the hashes match, you can prove the file is unchanged.

**Tested and confirmed during this course's build:**
```bash
sha256sum test.txt        →  a948904f... test.txt   (hash of "hello world\n")
# (make a bit-identical copy)
sha256sum test_copy.txt   →  a948904f... (identical — proof of exact match)
# (append one character)
sha256sum test_modified.txt → e9bc7863... (completely different — any change detected)
```

### `file` — type detection by content, not extension

**What/why:** File extensions lie. A file named `image.jpg` could contain Python code; a file named `document.pdf` could be a ZIP archive. The `file` command reads the first few bytes (called **magic bytes** or a **magic number**) to determine what a file actually is, independent of its name.

**Tested and confirmed during this course's build:**
```bash
file /bin/bash      →  ELF 64-bit LSB pie executable, x86-64...
file /etc/passwd    →  ASCII text
```
A fabricated PNG file (wrong magic bytes) was correctly identified as `ASCII text` rather than as an image — the extension would have been misleading, but the content analysis wasn't.

### Timestamps — what they actually mean

`stat` shows four timestamps per file. **Tested output:**
```
Access: 2026-09-08 10:24:55  (atime — last read)
Modify: 2026-09-08 10:24:55  (mtime — content last changed)
Change: 2026-09-08 10:24:55  (ctime — inode/metadata last changed)
Birth:  2026-09-08 10:24:55  (creation time, where filesystem supports it)
```
**Timestamps can be set to anything by the file's owner** (`touch -t`, `debugfs`). They're useful context, but not proof of when something actually happened — this is a genuine forensics subtlety, and presenting timestamps as definitive proof without corroboration is a documentation error.

### `strings` — finding human-readable text in binary files

```bash
strings /bin/ls | head -5
```
`strings` scans any file and prints sequences of printable characters it finds — sometimes revealing embedded paths, error messages, library dependencies, or even credentials in plaintext binaries, memory dumps, or disk images.

## Why It Matters

These techniques — hashing for integrity, `file` for true type identification, `stat` for timeline analysis, `strings` for content extraction — are the foundational layer beneath every more sophisticated forensics tool. Understanding them means understanding *why* the tools work, not just that they produce output.

## Common Mistakes

- Relying on file extensions for type identification in any security-relevant context — extensions are trivially changed.
- Presenting timestamps as definitive proof without noting they're modifiable.
- Analyzing evidence *before* establishing and recording a baseline hash — you can't prove integrity you didn't measure.

## Exercise

Before the lab, predict: if you run `file` on a JPEG image that has been renamed to `document.txt`, what will `file` report — the extension-based type, or the actual content-based type? Why?

## Further Reading

- [SANS — Introduction to Digital Forensics](https://www.sans.org/reading-room/whitepapers/incident/)
- `man file`, `man stat`, `man strings`
