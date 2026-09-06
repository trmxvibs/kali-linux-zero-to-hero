# Lab 01 — Navigating and Manipulating the Filesystem

**Environment needed:** Any Linux terminal (Kali VM, or any Linux/WSL terminal — this lab has no security tooling in it, so any Linux shell works).

## Goal

Build muscle memory for navigation and file manipulation before anything security-related is introduced.

## Steps

1. Open a terminal. Confirm where you are:
   ```bash
   pwd
   ```
2. Create a practice workspace and move into it:
   ```bash
   mkdir -p ~/lab01/reports
   cd ~/lab01
   ```
3. Create three text files and put different content in each:
   ```bash
   echo "Alpha report" > reports/alpha.txt
   echo "Beta report"  > reports/beta.txt
   echo "Gamma report" > reports/gamma.txt
   ```
4. List them in long format and identify the permissions column and file sizes:
   ```bash
   ls -l reports/
   ```
5. Use `grep` to find which file mentions "Beta":
   ```bash
   grep -l "Beta" reports/*.txt
   ```
6. Copy `alpha.txt` to `alpha_backup.txt`, then move it into a new `archive/` folder:
   ```bash
   cp reports/alpha.txt reports/alpha_backup.txt
   mkdir reports/archive
   mv reports/alpha_backup.txt reports/archive/
   ```
7. Confirm the final layout:
   ```bash
   find ~/lab01 -type f
   ```

## Expected Result

The `find` command should print exactly:
```
/home/<you>/lab01/reports/alpha.txt
/home/<you>/lab01/reports/beta.txt
/home/<you>/lab01/reports/gamma.txt
/home/<you>/lab01/reports/archive/alpha_backup.txt
```
(order may vary)

## Understanding the Output

- `find -type f` restricts results to regular files (not directories).
- The path shown is relative to how you invoked `find` — using `~/lab01` gives you full paths back.

## Common Mistakes

- Running `mv` and expecting a copy to remain behind — `mv` removes the original.
- Using `cd reports` then trying `mv alpha.txt archive/reports/` — a duplicated path segment. Always check `pwd` when a path error appears.

## Cleanup

```bash
rm -r ~/lab01
```

Next: [04-commands.md](04-commands.md) if you haven't read it yet, then [Module 02 — Kali Fundamentals](../02-kali-fundamentals/README.md).
