#!/usr/bin/env bash
#
# log_analyzer.sh
#
# Purpose: Summarize a log file — top IPs / patterns and simple keyword counts.
# Used in: Module 21 (Automation with Bash), Module 17 (Defensive Security)
#
# Usage:
#   ./log_analyzer.sh <logfile> [keyword]
#
# Example:
#   ./log_analyzer.sh /var/log/auth.log "Failed password"
#
# ⚠️ LAB ONLY reminder: only run against logs you own or are authorized to
# analyze. Sample logs for practice are in labs/log-analysis/sample.log

set -euo pipefail

if [ $# -lt 1 ]; then
    echo "Usage: $0 <logfile> [keyword]" >&2
    exit 1
fi

LOGFILE="$1"
KEYWORD="${2:-}"

if [ ! -f "$LOGFILE" ]; then
    echo "Error: file not found: $LOGFILE" >&2
    exit 1
fi

TOTAL_LINES=$(wc -l < "$LOGFILE")

echo "===== Log Analysis: $LOGFILE ====="
echo "Total lines: $TOTAL_LINES"
echo

echo "--- Top 10 IP addresses found ---"
grep -oE '([0-9]{1,3}\.){3}[0-9]{1,3}' "$LOGFILE" | sort | uniq -c | sort -rn | head -10 || echo "(no IP addresses found)"
echo

if [ -n "$KEYWORD" ]; then
    COUNT=$(grep -c -- "$KEYWORD" "$LOGFILE" || true)
    echo "--- Keyword search: \"$KEYWORD\" ---"
    echo "Matches: $COUNT"
    if [ "$COUNT" -gt 0 ]; then
        echo "First 5 matching lines:"
        grep -- "$KEYWORD" "$LOGFILE" | head -5
    fi
    echo
fi

echo "===== End of Analysis ====="
