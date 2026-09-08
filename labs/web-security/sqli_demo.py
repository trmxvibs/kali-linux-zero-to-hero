#!/usr/bin/env python3
"""
sqli_demo.py

A safe, local, self-contained demonstration of SQL injection via string
concatenation, and the fix via parameterized queries.

Used in: Module 14 (Web Security Fundamentals)

This uses an in-memory SQLite database with fabricated demo data — no
real system, network, or external database is touched. Safe to run
anywhere, by anyone, for learning purposes.
"""

import sqlite3


def build_demo_db():
    conn = sqlite3.connect(":memory:")
    c = conn.cursor()
    c.execute("CREATE TABLE users (id INTEGER, username TEXT, password TEXT)")
    c.execute("INSERT INTO users VALUES (1, 'alice', 'alicepass123')")
    c.execute("INSERT INTO users VALUES (2, 'admin', 'supersecretadminpass')")
    conn.commit()
    return conn, c


def vulnerable_login(cursor, username, password):
    """VULNERABLE: builds SQL via string concatenation. Do not use this
    pattern in real code — it is shown here only to demonstrate the flaw."""
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    print(f"  Executing query: {query}")
    cursor.execute(query)
    return cursor.fetchall()


def safe_login(cursor, username, password):
    """SAFE: parameterized query. Username/password are always treated as
    data, never as part of the SQL syntax, regardless of their content."""
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    cursor.execute(query, (username, password))
    return cursor.fetchall()


def main():
    conn, c = build_demo_db()

    print("=== Normal login attempt (vulnerable version) ===")
    result = vulnerable_login(c, "alice", "alicepass123")
    print(f"  Result: {result}\n")

    print("=== SQL injection attempt (vulnerable version) ===")
    malicious_username = "admin' -- "
    result = vulnerable_login(c, malicious_username, "wrongpassword")
    print(f"  Result: {result}\n")

    print("=== Same injection attempt against SAFE version ===")
    result = safe_login(c, malicious_username, "wrongpassword")
    print(f"  Result: {result}")

    conn.close()


if __name__ == "__main__":
    main()
