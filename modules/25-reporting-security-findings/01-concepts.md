# Lesson 25.1 — Writing Findings That Actually Get Fixed

## Learning Objectives

- Understand what a professional security finding contains
- Understand evidence-based severity rating (not gut-feel)
- Write a finding that a developer can act on immediately
- Understand the difference between a finding and a recommendation

## Prerequisites

Module 10 (CVE/CWE/risk vocabulary), Module 15 (vulnerability assessment), Module 20 (exploitation for evidence).

## Concept

**Plain language:** Finding a vulnerability and reporting it are two completely different skills. A finding that says "the login page is vulnerable to SQL injection" with no evidence, no reproduction steps, and no fix recommendation will sit in a ticket queue forever. A finding that includes a specific payload, the exact request/response captured, the precise impact, and a concrete remediation will get fixed.

**Technical — anatomy of a complete finding:**

```
Title          — specific, not vague ("SQL Injection in /login username parameter"
                  not "SQL Injection Found")
Severity       — CVSS-based or a justified Low/Medium/High/Critical
CWE            — the weakness category (e.g. CWE-89 for SQL Injection)
Affected       — exact component, URL, version
Prerequisites  — what's needed to reproduce (credentials? network access? specific config?)
Reproduction   — numbered, exact steps anyone can follow
Evidence       — screenshot, request/response, tool output
Impact         — what can actually be done if exploited (not what theoretically could happen)
Remediation    — specific, actionable fix (not "sanitize input" — "use parameterized queries")
Limitations    — what you did NOT test; what might affect reproducibility
```

### Severity — evidence-based, not gut-feel

Severity is a *claim* and claims need evidence. The same vulnerability type can be Critical in one context and Low in another:

- SQL injection on an internet-facing login page handling financial data → Critical
- SQL injection on a read-only internal reporting tool accessible only to 3 authenticated admins → Medium at most

CVSS (Common Vulnerability Scoring System) gives you a structured way to justify a score — it's not the only way, but using it shows your rating isn't arbitrary.

### Impact vs. Severity — two different questions

- **Severity** = how bad could this be, and how easy is it to reach?
- **Impact** = what concretely happened (or would happen) as a result?

Never overclaim impact. "Full system compromise is possible" needs evidence that full system compromise is actually achievable from this finding — not that it's theoretically conceivable.

### The Executive Summary — for the people who won't read further

One paragraph. No jargon. Answers: what was found, what can an attacker do with it, and what should be done. This is often the only part a decision-maker reads, so it must be accurate and complete on its own.

## Common Mistakes

- Reporting "it might be vulnerable" without confirming it actually is — unconfirmed findings waste responders' time and destroy credibility
- "Remediation: fix the vulnerability" — not actionable; specify exactly what change is needed
- Omitting the reproduction steps — if a developer can't reproduce it, they can't fix it
- Reporting every scanner finding without validation — scanners have false positives; confirm before reporting

## Security Perspective

A good report protects users. A vague, unactionable report is effectively the same as no report — the vulnerability stays open. The skill of writing clearly is as professionally important as the skill of finding issues.

## Further Reading

- [CVSS v3.1 specification](https://www.first.org/cvss/specification-document)
- [OWASP Testing Guide — Reporting](https://owasp.org/www-project-web-security-testing-guide/)
