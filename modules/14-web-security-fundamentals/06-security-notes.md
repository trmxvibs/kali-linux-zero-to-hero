# Security Notes — Module 14

- **SQL injection remains one of the most consistently found real-world vulnerabilities**, despite the fix (parameterized queries) being well-known and simple — this gap between "known fix exists" and "still found constantly" is worth internalizing as you move toward Module 15's assessment work.
- **This module's local demonstration used a deliberately unrealistic in-memory database with fabricated data** — never test SQL injection or any other web vulnerability against a real, unauthorized target; the identical technique against a real system without authorization is unauthorized access, not a lesson exercise.
- **Cookie/session theft** (Lesson 14.1) is why HTTPS matters even for sites that "don't have anything sensitive" — a stolen session cookie for *any* site can let an attacker impersonate a logged-in user, regardless of what the site's content actually is.
- **Defensive takeaway:** parameterized queries, input validation, and least-privilege database accounts (a web app's database user shouldn't have permission to do more than the app actually needs) are all real, standard mitigations Module 17 revisits.

> ⚠️ Every example and lab in this module runs against local, throwaway resources you control — no real website or database is targeted at any point.
