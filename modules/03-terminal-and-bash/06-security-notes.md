# Security Notes — Module 03

- Improper quoting in scripts that build commands from user input is a real, common source of command injection vulnerabilities — this is the shell-level root cause behind many "OS command injection" web vulnerabilities covered conceptually in Module 14.
- Command history (`~/.bash_history`) can itself be sensitive — commands sometimes contain things like URLs with embedded credentials or IP addresses of systems you tested. Treat your own shell history with the same care as a log file (Module 17).
- Aliases can be used defensively too: some administrators alias destructive commands (`alias rm='rm -i'`) to force a confirmation prompt as a safety net — a small, real hardening habit.
