# Python Scripts

Utilities built and taught in [Module 22 — Security Automation with Python](../../modules/22-security-automation-with-python/README.md).

All scripts here have been compiled (`python3 -m py_compile`), run against
test data, and — for the hash generator — cross-checked against the
system's own `sha256sum`/`md5sum` output. See
[tests/TEST_LOG.md](../../tests/TEST_LOG.md).

| Script | Purpose |
|---|---|
| `file_hash_generator.py` | Generates MD5/SHA1/SHA256 hashes for one or more files |
| `log_parser.py` | Parses SSH-style auth logs into a per-IP failed/accepted summary |

## Usage

```bash
python3 file_hash_generator.py <file> [--algo md5|sha1|sha256]
python3 log_parser.py <logfile> [--json]
```

Requires Python 3.8+. No third-party dependencies — standard library only.

> ⚠️ Both scripts only read files you point them at. Neither contacts any
> other host. See Module 22's security notes for full context.
