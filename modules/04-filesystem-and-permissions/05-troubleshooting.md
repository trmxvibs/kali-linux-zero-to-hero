# Troubleshooting — Module 04

**"Permission denied" running my own script** — it's not executable yet; `chmod +x script.sh` then `./script.sh`.

**`chmod` says "Operation not permitted"** — you don't own the file and aren't root; you generally can't change permissions on files you don't own.

**SUID shows uppercase `S` instead of lowercase `s`** — this is correct behavior, not an error: uppercase means SUID is set but the underlying execute bit for that audience is NOT set (see Lesson 04.1) — add execute (`chmod u+x`) if that's not what you intended.

**New files aren't getting the permissions I expect** — check your `umask`; it silently reduces permissions at creation time regardless of what you might assume the default should be.
