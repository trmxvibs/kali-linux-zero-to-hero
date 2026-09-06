# Lab 22 — File Integrity and Log Parsing in Python

**Scripts used:** [`scripts/python/file_hash_generator.py`](../../scripts/python/file_hash_generator.py), [`scripts/python/log_parser.py`](../../scripts/python/log_parser.py)

Both scripts were written and tested as part of this course, including cross-checking hash output against the system `sha256sum` command (see `tests/` in the repo root).

## Part 1 — File Integrity

1. Create a test file and hash it:
   ```bash
   echo "important config" > config.txt
   python3 scripts/python/file_hash_generator.py config.txt
   ```
2. Record the SHA-256 digest shown.
3. Modify the file by a single character, then re-hash it:
   ```bash
   echo "important config!" > config.txt
   python3 scripts/python/file_hash_generator.py config.txt
   ```
4. Confirm the digest is *completely* different — this is the "avalanche effect" that makes hashes useful for integrity checking.

## Part 2 — Log Parsing

1. Run the log parser against the sample log:
   ```bash
   python3 scripts/python/log_parser.py labs/log-analysis/sample.log
   ```
2. Confirm `203.0.113.5` shows 3 failed attempts and 0 accepted — this is a fixed test fixture, so your output should match exactly.
3. Run it with `--json` and pipe the output into a file:
   ```bash
   python3 scripts/python/log_parser.py labs/log-analysis/sample.log --json > /tmp/summary.json
   ```
4. **Extend it:** add a `--min-failed N` flag that only prints IPs with at least `N` failed attempts.

## Expected Result

Part 1: two completely different 64-character hex digests for two nearly identical files.
Part 2: a table (or JSON) showing exactly 3 IPs, with `203.0.113.5` having the highest failed count.

## Next Step

[Module 23 — CTF & Practice Methodology](../23-ctf-and-practice-methodology/README.md)
