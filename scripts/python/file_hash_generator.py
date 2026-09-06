#!/usr/bin/env python3
"""
file_hash_generator.py

Purpose: Generate MD5/SHA1/SHA256 hashes for one or more files.
Used in: Module 22 (Security Automation with Python), Module 18 (Digital Forensics)

Why this matters: file hashes are the basis of integrity checking and
evidence handling in forensics — a hash lets you prove a file has (or
hasn't) changed, without storing a copy of the whole file.

Usage:
    python3 file_hash_generator.py <file1> [file2 ...]
    python3 file_hash_generator.py <file1> --algo sha256

Exit codes:
    0 - success
    1 - one or more files could not be read
    2 - bad arguments
"""

import argparse
import hashlib
import sys
from pathlib import Path

SUPPORTED_ALGOS = ("md5", "sha1", "sha256")


def hash_file(path: Path, algo: str, chunk_size: int = 65536) -> str:
    """Return the hex digest of `path` using `algo`, reading in chunks
    so large files don't need to be loaded fully into memory."""
    h = hashlib.new(algo)
    with open(path, "rb") as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Generate file hashes.")
    parser.add_argument("files", nargs="+", help="One or more files to hash")
    parser.add_argument(
        "--algo",
        default="sha256",
        choices=SUPPORTED_ALGOS,
        help="Hash algorithm to use (default: sha256)",
    )
    args = parser.parse_args(argv)

    had_error = False
    for file_arg in args.files:
        path = Path(file_arg)
        if not path.is_file():
            print(f"ERROR: not a file or does not exist: {file_arg}", file=sys.stderr)
            had_error = True
            continue
        try:
            digest = hash_file(path, args.algo)
        except (OSError, PermissionError) as exc:
            print(f"ERROR: could not read {file_arg}: {exc}", file=sys.stderr)
            had_error = True
            continue
        print(f"{args.algo.upper()}  {digest}  {file_arg}")

    return 1 if had_error else 0


if __name__ == "__main__":
    sys.exit(main())
