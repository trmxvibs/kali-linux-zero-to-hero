#!/usr/bin/env python3
"""
log_parser.py

Purpose: Parse an SSH-style auth log and summarize failed vs. accepted
login attempts per source IP.
Used in: Module 22 (Security Automation with Python), Module 17 (Defensive Security)

This is intentionally simple: it demonstrates regex extraction, counting
with a dictionary, and clean CLI output — the concepts you need before
building anything more elaborate.

Usage:
    python3 log_parser.py <logfile>
    python3 log_parser.py <logfile> --json

⚠️ LAB ONLY reminder: only run against logs you own or are authorized to
analyze. A sample fabricated log is provided at labs/log-analysis/sample.log
"""

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

FAILED_RE = re.compile(r"Failed password.* from (\d{1,3}(?:\.\d{1,3}){3})")
ACCEPTED_RE = re.compile(r"Accepted (?:password|publickey).* from (\d{1,3}(?:\.\d{1,3}){3})")


def parse_log(path: Path) -> dict:
    stats = defaultdict(lambda: {"failed": 0, "accepted": 0})
    with open(path, "r", errors="replace") as f:
        for line in f:
            m = FAILED_RE.search(line)
            if m:
                stats[m.group(1)]["failed"] += 1
                continue
            m = ACCEPTED_RE.search(line)
            if m:
                stats[m.group(1)]["accepted"] += 1
    return dict(stats)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Summarize SSH auth log activity by source IP.")
    parser.add_argument("logfile", help="Path to the log file")
    parser.add_argument("--json", action="store_true", help="Output as JSON instead of a table")
    args = parser.parse_args(argv)

    path = Path(args.logfile)
    if not path.is_file():
        print(f"ERROR: file not found: {args.logfile}", file=sys.stderr)
        return 1

    stats = parse_log(path)

    if not stats:
        print("No matching SSH login lines found.")
        return 0

    if args.json:
        print(json.dumps(stats, indent=2))
        return 0

    print(f"{'IP Address':<20}{'Failed':<10}{'Accepted':<10}")
    print("-" * 40)
    # Sort by most failed attempts first — the most actionable view for a defender
    for ip, counts in sorted(stats.items(), key=lambda kv: kv[1]["failed"], reverse=True):
        print(f"{ip:<20}{counts['failed']:<10}{counts['accepted']:<10}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
