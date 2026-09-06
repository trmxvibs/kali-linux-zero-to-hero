# Lesson 10.1 — The Vocabulary and Mental Models of Security

## Learning Objectives

- Explain the CIA triad and use it to categorize any security concern
- Distinguish vulnerability, exploit, threat, and risk precisely
- Explain authentication vs. authorization
- Explain defense in depth and least privilege as design principles
- Understand attack surface as a concrete, reducible thing

## Prerequisites

Modules 01–09 (this module is the conceptual bridge before Modules 11–20's hands-on tools).

## Concept

### The CIA Triad

Almost every security concern is about protecting one (or more) of three properties:

- **Confidentiality** — only authorized parties can read the data (breached by: eavesdropping, unauthorized access, leaked credentials)
- **Integrity** — data hasn't been altered in unauthorized ways (breached by: tampering, corruption, unauthorized modification)
- **Availability** — the system/data is accessible when needed (breached by: denial of service, ransomware, hardware failure)

**Plain language check:** if someone reads your private messages without permission, that's a confidentiality breach. If they change the amount on your invoice without you knowing, that's integrity. If they take your website offline, that's availability. Nearly every security control (Modules 14–20) maps to protecting one or more of these.

### Vulnerability, Exploit, Threat, Risk — precisely

These four words are used loosely in casual conversation but mean specific, different things:

| Term | Meaning | Example |
|---|---|---|
| **Vulnerability** | A weakness that *could* be leveraged | An outdated web server with a known unpatched flaw |
| **Exploit** | A specific technique/code that leverages a vulnerability | A script that sends a crafted request triggering that flaw |
| **Threat** | A potential source of harm (an actor or event) | An attacker who might target that server |
| **Risk** | The likelihood × impact of a threat exploiting a vulnerability | "Low risk" if the server is internal-only and hard to reach; "high risk" if it's internet-facing with valuable data behind it |

A vulnerability existing doesn't automatically mean high risk — an unpatched flaw on an air-gapped machine with no threat actors able to reach it is a real vulnerability but low *risk*. This distinction is exactly why Module 15 (Vulnerability Assessment) and Module 25 (Reporting) insist on evidence-based severity, not "found a CVE, therefore critical."

### Authentication vs. Authorization

- **Authentication** — proving who you are (a password, a key, a fingerprint)
- **Authorization** — what you're allowed to do once authenticated

These fail independently: a system can authenticate you correctly but authorize you for too much (e.g., every logged-in user can access admin functions — an authorization flaw, not an authentication one). Module 14 and Module 16 both return to this distinction repeatedly.

### Defense in Depth

No single control should be the only thing standing between an attacker and their goal. A firewall, patched software, least-privilege accounts, monitoring, and backups are each individually imperfect — layered together, a failure in one doesn't mean total compromise. This is why Module 17 (Defensive Security) never presents any single technique as sufficient on its own.

### Least Privilege

Every user, process, and service should have the minimum access needed to do its job — nothing more. This principle underlies why Kali defaults to a non-root user (Module 02), why `sudo` exists instead of permanent root logins (Module 05), and why SUID misconfigurations are dangerous (Module 04/20).

### Attack Surface

The **attack surface** is the sum of everything an attacker could potentially interact with: open ports, exposed services, input fields on a website, installed software, even physical access points. Reducing attack surface — turning off unused services (Module 07), removing unnecessary software (Module 06), closing unneeded ports — is one of the most effective, boring, and underrated defensive practices there is.

## Why It Matters

Modules 11–20 will use every one of these terms constantly and precisely. Without this vocabulary, "vulnerability assessment" and "risk" sound interchangeable, and it becomes easy to either panic over low-risk findings or dismiss genuinely dangerous ones. This module exists specifically so that doesn't happen.

## Common Mistakes

- Treating "vulnerability found" as automatically meaning "critical risk" without considering exploitability, exposure, and impact.
- Confusing authentication failures with authorization failures when investigating an incident — they require completely different fixes.
- Believing a single strong control (e.g., "we have a firewall") means a system is secure — defense in depth exists because every single control can and does fail sometimes.

## Security Perspective

This entire lesson *is* the security perspective — it's the shared vocabulary that lets an attacker's finding and a defender's fix talk about the same thing precisely. Module 25 (Reporting) will hold you to using these terms correctly when describing real findings.

## Exercise

Before the lab, take a real, recent (widely reported, not obscure) security incident you're aware of and classify it: which CIA property was primarily violated? Was it fundamentally an authentication failure, an authorization failure, or both?

## Further Reading

- [NIST SP 800-12 — An Introduction to Information Security](https://csrc.nist.gov/pubs/sp/800/12/r1/final)
- [OWASP — Security Principles](https://owasp.org/www-project-developer-guide/release/foundations/security_principles/)
