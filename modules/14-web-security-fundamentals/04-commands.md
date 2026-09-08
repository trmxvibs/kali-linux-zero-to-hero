# Lesson 14.2 — Inspecting and Testing Web Behavior

## `curl` for headers and requests

```bash
curl -I http://target/                          # headers only
curl -v http://target/                             # verbose: shows the full request AND response
curl -X POST -d "user=alice&pass=test" http://target/login   # send form data
curl -H "Cookie: session=abc123" http://target/               # send a specific header/cookie manually
```

**Tested and confirmed during this course's build**, against a local Python test server:
```
$ curl -I http://localhost:8123/
HTTP/1.0 200 OK
Server: SimpleHTTP/0.6 Python/3.12.3
Date: Mon, 07 Sep 2026 02:33:55 GMT
Content-type: text/html
Content-Length: 19
```
**Reading it:** the `Server:` header reveals the exact software and version serving the page — directly useful enumeration data (Module 12) once you're looking at a real target, and something Module 17's hardening advice sometimes recommends suppressing or genericizing.

## Browser Developer Tools

Not a terminal command, but essential: every modern browser's Developer Tools (F12) → Network tab shows every request/response your browser makes, including headers, cookies, and timing — often faster for interactive exploration than `curl`, which is better for scripted/repeatable testing.

## Demonstrating SQL Injection Safely (local, throwaway database)

The exact script used to verify Lesson 14.1's claims is reproduced here in full — run it yourself:

```python
import sqlite3

conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("CREATE TABLE users (id INTEGER, username TEXT, password TEXT)")
c.execute("INSERT INTO users VALUES (1, 'alice', 'alicepass123')")
c.execute("INSERT INTO users VALUES (2, 'admin', 'supersecretadminpass')")
conn.commit()

def vulnerable_login(username, password):
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    print(f"  Executing query: {query}")
    c.execute(query)
    return c.fetchall()

def safe_login(username, password):
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    c.execute(query, (username, password))
    return c.fetchall()

print("=== Normal login (vulnerable version) ===")
print(vulnerable_login("alice", "alicepass123"))

print("=== SQL injection attempt (vulnerable version) ===")
print(vulnerable_login("admin' -- ", "wrongpassword"))

print("=== Same injection attempt against SAFE version ===")
print(safe_login("admin' -- ", "wrongpassword"))
```

**Tested output, exactly as run during this course's build:**
```
=== Normal login (vulnerable version) ===
  Executing query: SELECT * FROM users WHERE username = 'alice' AND password = 'alicepass123'
  Result: [(1, 'alice', 'alicepass123')]

=== SQL injection attempt (vulnerable version) ===
  Executing query: SELECT * FROM users WHERE username = 'admin' -- ' AND password = 'wrongpassword'
  Result: [(2, 'admin', 'supersecretadminpass')]

=== Same injection attempt against SAFE version ===
  Result: []
```

## Further Reading

- [MDN — HTTP overview](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview)
- [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
