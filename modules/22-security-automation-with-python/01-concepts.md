# Lesson 22.1 — Python for Security Tasks

## Learning Objectives

- Know when Python is a better fit than Bash (and vice versa)
- Understand the core building blocks: variables, lists, dicts, functions, loops, files, exceptions
- Understand `argparse` for building real command-line tools
- Understand regex basics for text extraction

## Prerequisites

Module 21 (Bash automation), basic programming comfort is helpful but not assumed — this lesson explains from the ground up.

## Concept

**Plain language:** Bash is excellent for gluing existing commands together. Python is better once you need real data structures (not just text), error handling, or logic more complex than a few conditionals — like parsing structured log data into counts per IP, as `log_parser.py` does in this module's lab.

**Technical — the building blocks used across every script in this module:**

```python
# Variables and data structures
name = "kali"
ports = [22, 80, 443]                 # list
counts = {"192.0.2.1": 3}             # dict

# Functions
def greet(who):
    return f"Hello, {who}"

# Loops
for port in ports:
    print(port)

# Files (always use `with` — it guarantees the file is closed)
with open("file.txt") as f:
    for line in f:
        print(line.strip())

# Exceptions — handle expected failure explicitly
try:
    with open("missing.txt") as f:
        pass
except FileNotFoundError:
    print("file not found")

# argparse — turns a script into a real CLI tool with --help for free
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("target")
parser.add_argument("--verbose", action="store_true")
args = parser.parse_args()

# Regex — extracting structured data from unstructured text
import re
match = re.search(r"(\d{1,3}(?:\.\d{1,3}){3})", "connection from 192.0.2.1 port 22")
if match:
    print(match.group(1))   # "192.0.2.1"
```

## Why It Matters

Every Python script in `scripts/python/` in this repository (`file_hash_generator.py`, `log_parser.py`) uses exactly these building blocks — nothing more exotic. Security automation is rarely about clever code; it's about correct, well-tested handling of real-world messy input (files that don't exist, logs with unexpected formats, permission errors).

## Common Mistakes

- Not handling `FileNotFoundError` / `PermissionError` explicitly — a script that just crashes with a raw traceback is unusable by anyone but its author.
- Writing a regex that's *too* greedy or too narrow, silently missing or misparsing lines — always test against a known sample with a known expected answer (see `03-practical-lab.md`).
- Loading an entire large file into memory (`f.read()`) when it should be streamed line by line or in chunks (see `hash_file()` in `file_hash_generator.py` for the chunked approach).

## Security Perspective

`file_hash_generator.py` exists specifically because file integrity checking (Module 18, forensics) depends on being able to compute and compare hashes reliably — a single-character difference in a file produces a completely different hash, which is exactly why hashes are used to prove (or disprove) that evidence hasn't been tampered with.

## Exercise

Before the lab, predict: if you hash the same file twice with SHA-256, will you get the same digest both times? What would have to change about the file for the digest to change?

## Further Reading

- [Python official tutorial](https://docs.python.org/3/tutorial/)
- [Python `hashlib` docs](https://docs.python.org/3/library/hashlib.html)
- [Python `re` (regex) docs](https://docs.python.org/3/library/re.html)
