# Lesson 21.1 — Why Automate, and With What

## Learning Objectives

- Understand variables, conditionals, loops, and functions in Bash
- Understand exit codes and why every well-behaved script uses them
- Understand pipes and redirection as composition tools
- Know when a task should become a script vs. staying a one-off command

## Prerequisites

Modules 01–03 (terminal fluency), Module 10 (security fundamentals).

## Concept

**Plain language:** If you find yourself running the same 4–5 commands in the same order more than twice, that's a script waiting to be written. Bash scripting isn't a separate skill from the terminal — it's just terminal commands, saved to a file, with a little extra logic (conditions, loops) glued on.

**Technical:** A Bash script is a plain text file, interpreted line by line. Core building blocks:

```bash
#!/usr/bin/env bash     # shebang: tells the OS which interpreter to use
set -euo pipefail        # exit on error, undefined variable, or failed pipe stage

NAME="world"              # variable assignment — no spaces around =
echo "Hello, $NAME"       # variable expansion

if [ -f "/etc/hosts" ]; then   # conditional: file exists?
    echo "hosts file present"
fi

for f in *.txt; do        # loop over files
    echo "Found: $f"
done

greet() {                  # function
    echo "Hi, $1"          # $1 = first argument to the function
}
greet "Kali"
```

**Exit codes:** every command returns a number when it finishes — `0` means success, anything else means failure. `$?` holds the last exit code. This is how scripts (and other scripts calling them) know whether something worked, and it's why every script in this course's `scripts/` folder returns meaningful, documented exit codes.

**`set -euo pipefail`** is a defensive habit worth adopting immediately:
- `-e` — stop on the first command that fails, instead of plowing ahead
- `-u` — error on an undefined variable, instead of silently treating it as empty
- `-o pipefail` — a pipeline fails if *any* stage fails, not just the last one

## Why It Matters

In security work, scripts are how one-off manual checks become repeatable, shareable, and auditable. A script you can hand to a teammate (or your future self) with clear usage and exit codes is infinitely more valuable than a shell history full of half-remembered one-liners.

## Common Mistakes

- Forgetting to `chmod +x` a script, then being confused why `./script.sh` says "permission denied."
- Not quoting variables (`rm $file` instead of `rm "$file"`) — breaks badly on filenames with spaces, and is a genuine source of real bugs and security issues.
- Writing scripts with no error handling, so a missing file causes confusing downstream failures instead of a clear message.

## Security Perspective

Automation cuts both ways: attackers automate scanning and exploitation at scale; defenders automate detection, log analysis, and hardening checks at the same scale. The scripts built in this module (`system_info_collector.sh`, `log_analyzer.sh`) are explicitly defensive/informational tools — see `scripts/bash/` in the repository root.

## Exercise

Before opening the lab, write (on paper) the pseudocode for a script that checks if a given TCP port is open on `localhost` and prints a clear yes/no message.

## Further Reading

- [Bash manual](https://www.gnu.org/software/bash/manual/bash.html)
- [ShellCheck](https://www.shellcheck.net/) — a static analyzer for shell scripts, used to sanity-check every script in this repository
