#!/usr/bin/env python3
"""
validate_links.py

Scans all Markdown files in the repository for relative links
(`[text](path)`) and reports any that point to a file that doesn't exist.
Skips external links (http/https) and in-page anchors (#section).

Usage:
    python3 tests/validate_links.py
"""

import re
import sys
from pathlib import Path
from urllib.parse import urlparse

REPO_ROOT = Path(__file__).resolve().parent.parent
LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")

SKIP_DIRS = {".git", "node_modules", "__pycache__"}


def iter_markdown_files():
    for path in REPO_ROOT.rglob("*.md"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        yield path


def is_external_or_anchor(link: str) -> bool:
    if link.startswith("#"):
        return True
    parsed = urlparse(link)
    return bool(parsed.scheme)  # http, https, mailto, etc.


def main() -> int:
    broken = 0
    checked = 0
    files_scanned = 0

    for md_file in iter_markdown_files():
        files_scanned += 1
        text = md_file.read_text(errors="replace")
        for match in LINK_RE.finditer(text):
            link_text, link_target = match.group(1), match.group(2).strip()

            if not link_target or is_external_or_anchor(link_target):
                continue

            # Strip a trailing in-page anchor like path.md#section
            target_path_part = link_target.split("#", 1)[0]
            if not target_path_part:
                continue

            checked += 1
            resolved = (md_file.parent / target_path_part).resolve()
            if not resolved.exists():
                print(f"[BROKEN] {md_file.relative_to(REPO_ROOT)} -> "
                      f"'{link_target}' (resolved: {resolved})")
                broken += 1

    print()
    print(f"Markdown files scanned: {files_scanned}")
    print(f"Relative links checked: {checked}")
    print(f"Broken links found: {broken}")

    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main())
