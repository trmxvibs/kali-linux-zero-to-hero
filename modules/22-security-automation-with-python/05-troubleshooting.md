# Troubleshooting — Module 22

**"ModuleNotFoundError"** — both scripts use only the Python standard library, so this shouldn't happen unless you're on a very unusual Python install; confirm with `python3 --version` (3.8+ expected).

**Hash doesn't match what you expected** — confirm you're comparing the *same* algorithm (`sha256sum file.txt` vs. `--algo sha256`, not `--algo md5`).

**`log_parser.py` shows "No matching SSH login lines found"** — the regex expects OpenSSH's standard "Failed password" / "Accepted password|publickey ... from <ip>" phrasing; a different log format will need an adjusted regex (this is a good extension exercise).

**argparse "invalid choice" error** — you passed something not in the allowed list (e.g. `--algo` only accepts `md5`, `sha1`, `sha256`); run `--help` to see valid options.
