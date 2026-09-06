# Bash Scripts

Utilities built and taught in [Module 21 — Automation with Bash](../../modules/21-automation-with-bash/README.md).

All scripts here have been syntax-checked (`bash -n`) and actually executed
against test data as part of building this course — see
[tests/TEST_LOG.md](../../tests/TEST_LOG.md).

| Script | Purpose |
|---|---|
| `system_info_collector.sh` | Collects local hostname/OS/CPU/memory/disk/process info into a report |
| `log_analyzer.sh` | Summarizes a log file: top IPs and keyword match counts |

## Usage

```bash
chmod +x system_info_collector.sh log_analyzer.sh
./system_info_collector.sh [output_file]
./log_analyzer.sh <logfile> [keyword]
```

A fabricated sample log for testing `log_analyzer.sh` is at
[`labs/log-analysis/sample.log`](../../labs/log-analysis/sample.log).

> ⚠️ Both scripts only read local information you point them at. Neither
> script contacts any other host. See Module 21's security notes for full
> context.
