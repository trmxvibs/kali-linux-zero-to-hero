# Security Notes — Module 13

- **Traffic analysis is one of the clearest places where authorization matters at a deeply personal level.** Capturing on a network segment you don't administer can expose other real people's private data — passwords, messages, browsing activity — not just "a target system's" data. This is qualitatively different from scanning a single machine you own, and the bar for authorization should be treated as correspondingly higher.
- **Plaintext protocols are a real, demonstrable finding.** If a lab (or, in authorized work, a real assessment) shows credentials or sensitive data crossing the wire unencrypted, that's direct, capturable evidence for Module 25's reporting — far more convincing than a theoretical claim.
- **Defensively, traffic analysis is core incident-response work.** Unexpected destinations, unusual protocols on standard ports, or large unexplained data transfers are exactly what defenders look for when investigating a suspected compromise (Module 17).

> ⚠️ **LAB ONLY** — capture exclusively on interfaces/networks you own or have explicit authorization to monitor.
