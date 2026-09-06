# Exercises — Module 21

1. Run `system_info_collector.sh` twice, five minutes apart, and diff the two reports (`diff report1.txt report2.txt`). What changed?
2. Modify `log_analyzer.sh` to accept a second keyword and report both counts side by side.
3. Write a new, small script `port_check.sh` that takes a port number as an argument and reports (using `ss`) whether anything is listening on it locally.

## Self-Check

You should be able to explain what `set -euo pipefail` does and why each of its three parts matters, without looking it up.
