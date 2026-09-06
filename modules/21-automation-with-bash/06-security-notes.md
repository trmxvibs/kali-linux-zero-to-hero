# Security Notes — Module 21

- Both scripts provided in this module (`system_info_collector.sh`, `log_analyzer.sh`) only read local information — they don't reach out to any other host, so there's no scope/authorization question for running them on your own machine.
- If you extend `log_analyzer.sh` to run against real production logs, remember it's still just reading — but the *log data itself* may be sensitive (usernames, IPs, sometimes more). Treat log files you analyze with the same care as any other sensitive data: don't commit real logs to a public repository, and redact before sharing findings.
- Automated tooling that reaches out to *other* hosts (as Nmap does — Module 11) always inherits that module's authorization requirements, even when wrapped in a "helper script."
