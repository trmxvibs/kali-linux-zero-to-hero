# Lab 21 — Running and Extending the Bash Toolkit

**Scripts used:** [`scripts/bash/system_info_collector.sh`](../../scripts/bash/system_info_collector.sh), [`scripts/bash/log_analyzer.sh`](../../scripts/bash/log_analyzer.sh)

Both scripts were written and tested as part of this course (see `tests/` in the repo root for the test log).

## Steps

1. Make both scripts executable and run the system info collector:
   ```bash
   cd scripts/bash
   chmod +x system_info_collector.sh log_analyzer.sh
   ./system_info_collector.sh
   ```
2. Save the report to a file instead of printing it:
   ```bash
   ./system_info_collector.sh /tmp/my_report.txt
   ```
3. Run the log analyzer against the provided sample log:
   ```bash
   ./log_analyzer.sh ../../labs/log-analysis/sample.log "Failed password"
   ```
4. **Extend it:** modify `log_analyzer.sh` to also report the *single* IP address with the most total lines (not just top 10) as its own summary line at the end. Test your change against the sample log.

## Expected Result

Step 3 should show `203.0.113.5` with 3 matches for "Failed password" against the provided sample log — this is a fixed, deterministic test fixture, so your output should match exactly.

## Troubleshooting

- `bash: ./script.sh: Permission denied` → run `chmod +x script.sh` first.
- `set -u` causing "unbound variable" after your edit → you referenced a variable that was never assigned; check for typos.

## Next Step

[Module 22 — Security Automation with Python](../22-security-automation-with-python/README.md)
