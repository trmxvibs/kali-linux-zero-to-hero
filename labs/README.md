# Shared Lab Data

This folder holds shared, reusable data/fixtures referenced by module labs
— as opposed to `modules/<name>/03-practical-lab.md`, which holds the
step-by-step lab instructions themselves.

| Folder | Used by |
|---|---|
| `log-analysis/sample.log` | Module 21 (`log_analyzer.sh`), Module 22 (`log_parser.py`) |

All sample data in this folder is **fabricated** — fictional hostnames and
RFC 5737 documentation IP ranges (`203.0.113.0/24`, `198.51.100.0/24`,
`192.0.2.0/24`), never real logs or real people's data. See
[docs/getting-started/ethics-and-legal.md](../docs/getting-started/ethics-and-legal.md).

VM-based labs (Metasploitable, DVWA, etc.) are documented in their owning
module (see Module 11, Module 26) rather than duplicated here, since they
require a hypervisor and can't be shipped as static files in this repository.
