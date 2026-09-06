# Troubleshooting — Module 21

**Script runs but produces no output** — check you didn't redirect to a file by accident (`>` vs the command you meant); verify with `cat` on any output file.

**"unbound variable" error after adding `set -u`** — you used a variable before assigning it, or misspelled its name. Add `echo "DEBUG: $myvar"` temporarily to trace it.

**Script exits immediately after one failed command** — that's `set -e` working as intended. If a command is *expected* to sometimes fail (e.g., `grep` finding nothing), append `|| true` to that specific line.

**Numbers look wrong from `awk`** — double check field numbering; `awk` fields are 1-indexed and separated by whitespace by default (`-F` changes the separator).
