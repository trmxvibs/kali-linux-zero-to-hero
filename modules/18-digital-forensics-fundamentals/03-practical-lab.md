# Lab 18 — Basic Evidence Analysis

**Environment:** Any Linux terminal with `file`, `strings`, `stat`, `sha256sum` (standard on Kali; tested and working in this course's own build sandbox).

**Sample evidence:** `labs/digital-forensics/sample-evidence/` — three fabricated files with no connection to real events or real people.

## Steps

1. **Establish hashes before any analysis:**
   ```bash
   sha256sum labs/digital-forensics/sample-evidence/*
   ```
   Record every hash. This is your baseline — you can now prove whether any file changes during your analysis.

2. **File type analysis — catch the misnamed file:**
   ```bash
   file labs/digital-forensics/sample-evidence/document.pdf
   file labs/digital-forensics/sample-evidence/binary_stub
   ```
   Confirm that `document.pdf` is NOT actually a PDF (tested: `file` reports `ASCII text`), and that `binary_stub` *is* treated as a binary (ELF magic bytes, even though the rest of the content is fabricated). The extension mismatches are deliberate.

3. **Timestamp analysis:**
   ```bash
   stat labs/digital-forensics/sample-evidence/document.pdf
   ```
   Record all four timestamps. Note the difference between `Access` (last read) and `Modify` (last written). Ask yourself: what would you need to know to trust these timestamps as evidence of when something actually happened?

4. **String extraction from the binary:**
   ```bash
   strings labs/digital-forensics/sample-evidence/binary_stub
   ```
   **Tested output (from this course's build):**
   ```
   ELFFABRICATED-EVIDENCE-BINARY
   /tmp/.hidden_dir
   connect_to=198.51.100.99:4444
   user_agent=Suspicious-Tool/1.0
   ```
   Grep for interesting patterns:
   ```bash
   strings labs/digital-forensics/sample-evidence/binary_stub | grep -i "connect\|hidden\|user_agent"
   ```

5. **Log analysis:**
   ```bash
   cat labs/digital-forensics/sample-evidence/log_snippet.txt
   python3 scripts/python/log_parser.py labs/digital-forensics/sample-evidence/log_snippet.txt
   ```

6. **Re-hash to confirm nothing changed:**
   ```bash
   sha256sum labs/digital-forensics/sample-evidence/*
   ```
   Confirm every hash matches Step 1 exactly.

## Expected Result

- Step 2: `document.pdf` identified as `ASCII text` (not PDF) — file content wins over extension
- Step 4: strings output shows embedded path `/tmp/.hidden_dir` and `connect_to=198.51.100.99:4444` — fabricated to resemble the kind of strings that would be suspicious in a real investigation
- Steps 1 and 6: identical hashes — your analysis left no evidence of modification

## Next Step

[Module 19 — Wireless Security Concepts](../19-wireless-security-concepts/README.md)
