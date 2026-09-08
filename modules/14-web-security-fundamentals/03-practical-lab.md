# Lab 14 — Inspecting Requests and Breaking (Then Fixing) a Login Check

**Environment:** Any Linux terminal with `python3` and `curl` (no internet or VM required for this lab — everything runs locally).

## Part 1 — Inspecting Real HTTP Traffic

1. Serve a simple local page:
   ```bash
   mkdir -p ~/lab14/www && cd ~/lab14/www
   echo "<h1>Test Page</h1>" > index.html
   python3 -m http.server 8123
   ```
2. In a second terminal, inspect it:
   ```bash
   curl -I http://localhost:8123/
   curl -v http://localhost:8123/
   ```
3. Identify, from the output: the status code, the `Server` header (and what it reveals), and the `Content-Length`.

## Part 2 — Reproducing SQL Injection Yourself

Run the demonstration script included in this repository:
```bash
python3 labs/web-security/sqli_demo.py
```

Confirm you see:
- A normal login succeeding with correct credentials
- The injection (`admin' -- ` as the username) returning the **admin row despite a wrong password**, against the vulnerable version
- The identical injection attempt returning **no rows** against the safe, parameterized version

## Part 3 — Extend It Yourself, and a Real Gotcha About Operator Precedence

Open `labs/web-security/sqli_demo.py` and try this classic-looking payload as the username, with any password, against the vulnerable version:
```
' OR '1'='1
```
**Predict the result before running it** — then actually run it and compare. (This is deliberately a place where intuition can mislead you — see below.)

Now try this second, very similar-looking payload instead:
```
' OR '1'='1' -- 
```

## Expected Result — and the Gotcha

The first payload (`' OR '1'='1`, no comment) surprisingly returns **zero rows** — not "all rows" as intuition might suggest. This is because SQL's `AND` operator binds *tighter* than `OR`: the resulting query is effectively `username = '' OR ('1'='1' AND password = 'anything')`, and since no real password equals the literal string `anything`, that whole `AND` clause is false for every row.

The second payload (`' OR '1'='1' -- `) **does** return every row in the table, because the `--` comments out the password check entirely, leaving just `username = '' OR '1'='1'` — always true.

**This exact distinction was discovered by testing during this course's build** — an initial draft of this lab assumed the first payload alone would dump the whole table, which testing proved wrong. The lesson this leaves you with is a real one: SQL injection payloads are precise, and getting the syntax subtly wrong (missing a comment marker, misjudging operator precedence) can silently fail rather than obviously succeed — exactly why testing your actual assumptions, rather than trusting a remembered payload, matters.

## Next Step

[Module 15 — Vulnerability Assessment](../15-vulnerability-assessment/README.md)
