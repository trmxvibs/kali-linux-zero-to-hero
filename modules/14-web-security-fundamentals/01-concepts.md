# Lesson 14.1 — How Web Requests Actually Work

## Learning Objectives

- Understand the anatomy of an HTTP request and response
- Understand cookies and sessions as the mechanism behind "staying logged in"
- Understand why user input is the root of most web vulnerabilities
- Understand SQL injection as a concrete, worked example of that root cause

## Prerequisites

Module 08 (Networking), Module 10 (Security Fundamentals — especially authentication vs. authorization).

## Concept

**Plain language:** A website is, underneath the visual design, just two computers exchanging structured text messages: your browser sends a *request*, the server sends back a *response*. Almost every web vulnerability comes down to the server trusting something in that request more than it should.

**Technical — anatomy of a request/response**, confirmed with a real local example during this course's build:

```
$ curl -I http://localhost:8123/
HTTP/1.0 200 OK
Server: SimpleHTTP/0.6 Python/3.12.3
Date: Mon, 07 Sep 2026 02:33:55 GMT
Content-type: text/html
Content-Length: 19
```

- The **status line** (`HTTP/1.0 200 OK`) tells you the protocol version and result — `200` means success; `404` means not found; `500` means server error; `403` means forbidden.
- **Headers** (`Server:`, `Content-Type:`, etc.) are metadata about the request/response — Module 14's lab has you inspect these directly.
- The **body** (not shown by `-I`, which only fetches headers) is the actual content — HTML, JSON, an image, whatever the response contains.

### Cookies and Sessions

HTTP itself is **stateless** — each request is independent, with no memory of previous ones. "Staying logged in" is an illusion built on top: after login, the server gives your browser a **cookie** (a small piece of data), which your browser automatically resends with every subsequent request. The server looks up that cookie's value against its own records (a **session**) to know who you are. If that cookie is stolen (via network capture — Module 13 — or a vulnerability like XSS), the thief can impersonate you without ever knowing your password.

### Why User Input Is the Root Cause

Every piece of data a user provides — a form field, a URL parameter, a cookie value, even an HTTP header — is a place the server has to make a decision: trust this completely, validate it, or reject it. Nearly every category in the OWASP Top 10 is some version of "the server trusted user input more than it should have."

### SQL Injection — the concrete example

**The vulnerability:** building a database query by directly concatenating user input into a string.

```python
query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
```

If `username` is set to `admin' -- `, the query becomes:
```sql
SELECT * FROM users WHERE username = 'admin' -- ' AND password = 'wrongpassword'
```
The `--` starts a SQL comment, silently deleting the password check entirely. **This exact scenario was built and tested during this course's construction**: with a plain-text password check bypassed this way, the query returned the `admin` row despite an intentionally wrong password — logging in as admin with no valid credentials at all.

**The fix — parameterized queries:**
```python
query = "SELECT * FROM users WHERE username = ? AND password = ?"
cursor.execute(query, (username, password))
```
Here, the database driver treats `username` and `password` strictly as *data*, never as part of the SQL syntax — no matter what characters they contain. **Tested and confirmed**: the identical injection attempt against this version returned zero rows, exactly as intended.

## Why It Matters

SQL injection has been on the OWASP Top 10 for over two decades and remains a real, frequently-found vulnerability precisely because string concatenation *looks* like it works fine until someone deliberately breaks it. Module 14's lab has you reproduce both the exploit and the fix yourself, so the difference is concrete, not theoretical.

## Common Mistakes

- Trying to fix SQL injection by "sanitizing" input (stripping quotes, escaping characters) instead of using parameterized queries — sanitization is fragile and repeatedly bypassed in the real world; parameterization solves the problem structurally.
- Assuming SQL injection only applies to login forms — any place user input reaches a database query (search boxes, URL parameters, even HTTP headers if logged to a database) is a potential injection point.
- Confusing cookies (client-side storage) with sessions (server-side state) — the cookie is just a reference; the actual session data lives on the server.

## Security Perspective

This lesson is Module 10's authentication/authorization vocabulary made concrete: SQL injection that bypasses a login check is an **authentication** failure — the attacker never proved who they are, yet gained access anyway. Module 15 will cover how to identify this class of vulnerability during an assessment; Module 20 covers safe, lab-only exploitation.

> ⚠️ Every demonstration in this module runs against a local, throwaway database or web server you control — never test SQL injection or any web vulnerability against a site you don't own or lack explicit authorization to test.

## Exercise

Before the lab, predict: would changing `username` to `' OR '1'='1` produce a similar bypass in the vulnerable version above? Work through the resulting SQL string by hand before testing it.

## Further Reading

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [OWASP — SQL Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)
