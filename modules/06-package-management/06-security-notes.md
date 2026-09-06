# Security Notes — Module 06

- **Package management is a primary patch-delivery mechanism.** Regularly running `apt update && apt full-upgrade` is one of the highest-value, lowest-effort defensive habits covered in this entire course (Module 17 revisits this at the system-hardening level).
- **Untrusted repositories are a real supply-chain risk.** Adding a third-party `apt` source means trusting that source's maintainers with root-equivalent code execution on your system via install scripts — verify any repository's legitimacy before adding it, and prefer official sources.
- **Knowing exactly what's installed and its version** (`dpkg -l`, `apt-cache policy`) is the necessary first step before you can reason about whether a system is running known-vulnerable software — this connects directly to Module 15 (Vulnerability Assessment).

> ⚠️ Every command in this module manages software on your own system — no other host is involved.
