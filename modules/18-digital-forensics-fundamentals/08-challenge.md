# Challenge — Module 18

Build a small Python script `evidence_hasher.py` that:
- Takes a directory path as an argument
- Hashes every regular file in that directory with SHA-256
- Saves a manifest file (e.g., `manifest.sha256`) containing all filename+hash pairs
- On a second run, compares against the existing manifest and reports any new, missing, or changed files
- Handles missing directories, permission errors, and missing manifest gracefully

Test it against `labs/digital-forensics/sample-evidence/`, then against a directory where you modify one file between the first and second run. This is a simplified version of a real "file integrity monitor" — a key defensive tool (Module 17 referenced this concept).
