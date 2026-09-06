# Security Notes — Module 22

- File hashing (`file_hash_generator.py`) is a foundational forensics technique (Module 18): before and after analyzing potential evidence, you hash it, so you can later prove you didn't alter it.
- MD5 and SHA-1 are considered cryptographically broken for security purposes (collision attacks exist) — they remain useful here purely for basic integrity/change-detection, not for anything requiring collision resistance (e.g., password storage, which is covered separately in Module 16).
- `log_parser.py` only reads log files you point it at — as with Module 21, the sensitivity lives in the *data*, not the script. Don't commit real production logs to a public repository.
