# Exercises — Module 22

1. Use `file_hash_generator.py` to hash the same file with all three supported algorithms and note how digest length differs between MD5 (128-bit), SHA-1 (160-bit), and SHA-256 (256-bit).
2. Extend `log_parser.py` to also report the *earliest* and *latest* timestamp seen per IP (hint: you'll need to extract and parse the timestamp with an additional regex).
3. Write a short Python script `url_validator.py` that takes a string and prints whether it's a syntactically valid URL, using Python's `urllib.parse`.

## Self-Check

You should be able to explain why `file_hash_generator.py` reads files in chunks (`chunk_size`) instead of `f.read()` all at once.
