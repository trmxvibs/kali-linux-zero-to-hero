# Troubleshooting — Module 03

**Alias disappears after closing the terminal** — aliases set directly on the command line are session-only; add them to `~/.bashrc` to persist (covered in this module's exercises).

**`$VAR` prints nothing** — the variable wasn't set in this shell, or you used single quotes somewhere upstream that prevented expansion; confirm with `echo "$VAR"` in a fresh check.

**"bash: !42: event not found"** — the history entry number you referenced doesn't exist (histories are numbered continuously and can differ between sessions); run `history` again to get a current number.

**Command substitution `$(...)` shows literal text instead of running** — you're likely inside single quotes; switch to double quotes or no quotes.

**Alias works when typed directly but not inside a script file** — by design, Bash only expands aliases in *interactive* shells; a script run with `bash script.sh` won't expand an alias defined earlier in the same script unless you add `shopt -s expand_aliases` first. This is exactly why Module 21 uses functions, not aliases, for anything going into a script file — aliases are a command-line convenience, not a scripting tool.
