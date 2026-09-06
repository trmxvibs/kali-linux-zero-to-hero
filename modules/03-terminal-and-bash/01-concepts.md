# Lesson 03.1 — The Shell, Beyond Single Commands

## Learning Objectives

- Understand the shell's read-evaluate loop, history, and tab completion
- Understand environment variables and `PATH`
- Understand quoting and why it matters
- Understand `man` pages as the authoritative reference

## Prerequisites

Module 01 (basic commands), Module 02.

## Concept

**Plain language:** Module 01 taught individual commands. This module is about the shell *itself* as an environment — how it remembers what you typed, how it finds the programs you name, and how it decides where one argument ends and another begins.

**Technical — the shell's job, step by step, every time you press Enter:**

1. Read the line you typed
2. Split it into words, respecting quotes
3. Expand any variables (`$HOME`), globs (`*.txt`), and command substitutions (`` `date` `` or `$(date)`)
4. Look up the first word in `PATH` (or recognize it as a shell builtin/function)
5. Run it, connecting input/output as directed by any pipes/redirection
6. Wait for it to finish (unless run in the background with `&`), then show you a fresh prompt

### `PATH` and `which`

```bash
echo $PATH
```
This prints a colon-separated list of directories the shell searches, in order, when you type a bare command name. `which nmap` (Module 01) tells you *which one* of those directories actually contained it.

### Environment variables

```bash
export MY_VAR="hello"
echo $MY_VAR
```
`export` makes a variable available to programs the shell launches, not just the shell itself. `$HOME`, `$USER`, and `$PATH` are environment variables set for you at login.

### Quoting — why it matters

```bash
echo Hello World          # two words, both printed with one space between
echo "Hello   World"       # quotes preserve the exact spacing inside
name="Sam"
echo Hello $name            # expands to: Hello Sam
echo 'Hello $name'          # single quotes prevent expansion: literally "Hello $name"
```
Single quotes (`'...'`) suppress all expansion. Double quotes (`"..."`) allow variable/command expansion but still protect spaces and most special characters. This distinction becomes a genuine source of bugs (and, in security-relevant code, injection vulnerabilities) if ignored — Module 21 revisits this in scripts.

### History and tab completion

- Press **Up/Down arrows** to cycle through previous commands
- Press **Tab** to autocomplete a command or filename — press twice to see all options if ambiguous
- `history` prints your command history; `!42` re-runs history entry 42; `!!` re-runs the last command

### `man` pages

```bash
man ls
```
Every standard command has a manual page — press `q` to quit. This is the authoritative reference this entire course points you back to. `man -k keyword` searches all page descriptions for a keyword.

## Why It Matters

Every script in Module 21 and every complex command chain in Modules 11–20 depends on you being fluent with quoting, variables, and `PATH` — a misquoted variable in a security tool's arguments is a common, entirely avoidable source of bugs.

## Common Mistakes

- Forgetting to `export` a variable, then being confused why a subprocess doesn't see it.
- Using single quotes when you meant double quotes (or vice versa), silently breaking variable expansion.
- Typing a script name without `./` (e.g., `myscript.sh` instead of `./myscript.sh`) and getting "command not found" — your current directory (`.`) is deliberately **not** in `PATH` by default, for security reasons (a stray file named `ls` in your current directory shouldn't silently override the real `ls`).

## Security Perspective

The fact that `.` isn't in `PATH` by default is itself a security control — historically, tricking a privileged user into running a malicious file with a common name (`ls`, `cd`) from a shared or writable directory was a real attack technique. Understanding *why* `./script.sh` is required, rather than treating it as an annoying quirk, is a small but real piece of security literacy.

## Exercise

Before the lab, predict what `echo "$HOME"` vs `echo '$HOME'` will each print, and explain why they differ.

## Further Reading

- [Bash manual — Quoting](https://www.gnu.org/software/bash/manual/bash.html#Quoting)
- `man bash` (the full Bash manual page, very long but authoritative)
