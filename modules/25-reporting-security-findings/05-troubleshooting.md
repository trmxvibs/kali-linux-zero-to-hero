# Troubleshooting — Module 25

**Severity feels arbitrary** — use CVSS v3.1's online calculator (first.org/cvss/calculator) with your specific finding; fill in each metric honestly and let the score inform your rating rather than starting from a gut feeling.

**Can't reproduce a finding you found earlier** — this happens. If you can't reproduce it, you can't confirm it. Report it as "observed once, could not reproduce consistently" with your evidence from the original observation, rather than as a confirmed finding.

**Finding is real but impact seems low** — report it anyway with an honest low severity; a chain of low-severity findings sometimes enables a high-impact attack path, and documented findings serve future audits even if not immediately actionable.

**Not sure what remediation to recommend** — research the CWE entry for this vulnerability type; CWE entries include a "Potential Mitigations" section that provides direct, credible remediation guidance.
