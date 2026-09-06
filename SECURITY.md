# Security Policy

This repository is educational documentation, scripts, and lab material —
not a production application — but two categories of "security issue" can
still apply:

## 1. A Documentation/Lab Safety Issue

If you find guidance in this course that is technically unsafe (e.g., a
command that could affect systems beyond the intended lab scope, or a lab
that isn't actually isolated the way it claims to be), please open an issue
using the label `safety` or `security`. This is the most important category
— report it even if you're unsure it's a real problem.

## 2. A Vulnerability in a Provided Script

If a script under `scripts/` has an actual security flaw (e.g., unsafe
handling of input that could lead to command injection), please open an
issue with the label `security`, or, for anything sensitive, use GitHub's
private vulnerability reporting feature on this repository if available.

## What NOT to Report Here

Vulnerabilities in third-party tools referenced by this course (Nmap,
Metasploit, DVWA, etc.) should be reported to those projects directly, not
here.

## Response

This is a community-maintained educational project without a dedicated
security team or SLA. Reports will be reviewed as maintainer time allows —
please be patient, and thank you for helping keep the course safe and
accurate.
