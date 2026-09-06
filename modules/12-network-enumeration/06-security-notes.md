# Security Notes — Module 12

- **Enumeration findings are exactly what Module 25's reports are built from** — "anonymous FTP allowed" or "SMB shares listable without credentials" are the kind of specific, evidence-backed statements a real report needs, versus vague claims like "the server might be insecure."
- **Anonymous/guest access misconfigurations are extremely common findings in real assessments** — Metasploitable exaggerates this deliberately for teaching purposes, but the underlying issue (a share or service left open to anyone by accident) is one of the most frequently found real-world issues.
- **Defensive counter-measures** (Module 17 revisits these): disabling anonymous FTP/SMB access, removing unnecessary shares, and banner obfuscation (though obfuscation alone is not a real security control — it only slows down casual enumeration, not a determined attacker who fingerprints services by behavior instead of banner text).

> ⚠️ Every command in this module targets your isolated Metasploitable VM exclusively — enumeration is meaningfully more invasive than Module 11's basic scanning, making scope discipline even more important here.
