# Lab 03 — Shell Fluency Drill

**Environment:** Any Linux terminal, Kali VM recommended.

## Steps

1. Set and use a variable:
   ```bash
   export COURSE="Kali Zero to Hero"
   echo "Currently studying: $COURSE"
   ```
2. Demonstrate the single vs. double quote difference yourself:
   ```bash
   echo "Value: $COURSE"
   echo 'Value: $COURSE'
   ```
3. Create an alias and use it:
   ```bash
   alias ll='ls -la'
   ll
   ```
4. Use command substitution to embed the current date in a message:
   ```bash
   echo "Report generated on $(date)"
   ```
5. Use `history` to find and re-run your very first command from this session using `!N` (find `N` from the `history` output).
6. Look up `chmod` in the manual and identify, from the man page alone (not this course), what the `-R` flag does.

## Expected Result

Step 2 should show `Value: Kali Zero to Hero` for the double-quoted version and the literal text `Value: $COURSE` for the single-quoted version — if both print the same thing, re-read `01-concepts.md`'s quoting section.

## Next Step

[Module 04 — Filesystem & Permissions](../04-filesystem-and-permissions/README.md)
