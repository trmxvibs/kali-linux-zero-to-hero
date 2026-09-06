#!/usr/bin/env bash
#
# system_info_collector.sh
#
# Purpose: Collect basic system information into a single readable report.
# Used in: Module 21 (Automation with Bash)
#
# Usage:
#   ./system_info_collector.sh [output_file]
#
# If output_file is omitted, prints to stdout.
#
# ⚠️ LAB ONLY reminder: this script only reads information about the LOCAL
# machine it runs on. It does not touch any other host.

set -euo pipefail

OUTPUT="${1:-/dev/stdout}"

collect() {
    echo "===== System Information Report ====="
    echo "Generated: $(date)"
    echo

    echo "--- Hostname & OS ---"
    echo "Hostname: $(hostname)"
    if [ -f /etc/os-release ]; then
        # shellcheck disable=SC1091
        . /etc/os-release
        echo "OS: ${PRETTY_NAME:-unknown}"
    fi
    echo "Kernel: $(uname -r)"
    echo

    echo "--- CPU & Memory ---"
    if command -v nproc >/dev/null 2>&1; then
        echo "CPU cores: $(nproc)"
    fi
    if [ -f /proc/meminfo ]; then
        awk '/MemTotal|MemAvailable/' /proc/meminfo
    fi
    echo

    echo "--- Disk Usage ---"
    df -h --output=source,size,used,avail,pcent,target 2>/dev/null | grep -Ev "tmpfs|overlay" || df -h
    echo

    echo "--- Logged-in Users ---"
    who || echo "who: not available"
    echo

    echo "--- Top 5 Processes by Memory ---"
    ps aux --sort=-%mem 2>/dev/null | head -6 || ps aux | head -6
    echo

    echo "===== End of Report ====="
}

collect > "$OUTPUT"

if [ "$OUTPUT" != "/dev/stdout" ]; then
    echo "Report written to: $OUTPUT"
fi
