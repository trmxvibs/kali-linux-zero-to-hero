# Security Notes — Module 26

- This module's isolation architecture is the practical implementation of the "One Rule" from Module 00 — read together, they are the safety backbone of the entire course.
- Never connect Metasploitable (or any deliberately vulnerable training image) to a network with internet access or shared with real devices, even briefly. Its vulnerabilities are real and exploitable by anything that can reach it, not just by you.
- If you ever need internet access on your Kali VM for updates (Module 06), do that on a **separate**, temporary NAT adapter or session — not the same network segment as your vulnerable lab targets — and disconnect it before running lab exercises.
