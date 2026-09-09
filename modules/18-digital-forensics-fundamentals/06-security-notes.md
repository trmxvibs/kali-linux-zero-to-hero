# Security Notes — Module 18

- **File-extension spoofing is a real attack vector.** Malware named `invoice.pdf` that is actually an ELF binary or a JavaScript file is a documented, real-world technique to trick users into executing something they think they're just opening for viewing. `file`'s content-based analysis is the correct countermeasure.
- **Timestamps are not reliable proof.** Any user who owns a file (or has root) can modify timestamps freely. In forensics, timestamps provide a starting hypothesis, not a conclusion — corroboration from logs, network captures, or other independent sources is required before treating a timestamp as evidence of *when* something happened.
- **This module's sample data uses RFC 5737 documentation IP ranges** (`198.51.100.0/24`) and fabricated paths — nothing in it represents real systems, real events, or real malware. Actual malware samples require very different handling and are out of scope for this course.

> ⚠️ The commands in this module are read-only analysis operations on your own files — no other host is involved.
