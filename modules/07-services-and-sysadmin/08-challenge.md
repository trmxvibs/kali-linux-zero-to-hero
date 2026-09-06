# Challenge — Module 07

Combine this module with Module 21 (Bash automation, previewed here): write a script `service_audit.sh` that:
- Takes a list of expected-enabled service names (hardcode a small list, e.g. `ssh`, `cron`)
- For each, reports whether it matches your expectation (enabled+active) and flags any mismatch clearly
- Also lists any *other* currently-running services not in your expected list, so you can spot something unexpected

This is a small, real building block toward the kind of baseline-drift detection real defenders use (Module 17).
