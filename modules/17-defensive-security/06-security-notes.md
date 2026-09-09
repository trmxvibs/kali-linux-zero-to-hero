# Security Notes — Module 17

- This module's commands (`ss`, `ps`, `find`, `journalctl`) are also the first things most incident-response processes reach for — **the same tools serve both routine maintenance and active investigation**, which is exactly why fluency with them from Modules 01–09 onward is foundational.
- **Log tampering is real.** A sophisticated attacker with root access may attempt to modify or delete log files to hide their activity — this is why externally-shipped logs (sending logs to a separate, dedicated log server) are a standard defensive practice in production environments.
- **Hardening is continuous, not one-time.** A system audited and secured today may have a newly-disclosed vulnerability tomorrow (Module 15), a new user added next week, or a misconfigured service deployed next month. The habits in this module (periodic auditing, log review, keeping software updated) are the answer to that ongoing nature of security work.
