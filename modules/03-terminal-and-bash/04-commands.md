# Lesson 03.2 — Terminal Productivity Commands

## `history`

```bash
history          # list your command history
!42               # re-run history entry number 42
!!                 # re-run the previous command
!ls                # re-run the most recent command starting with "ls"
```
**Common mistake:** Blindly re-running `!!` after a destructive command failed for an unrelated reason — always glance at what `!!` will actually repeat if you're not 100% sure.

## `alias`

**What/why:** Creates a shortcut for a longer command.
```bash
alias ll='ls -la'
ll                  # now runs `ls -la`
```
Add aliases to `~/.bashrc` to make them permanent (Module 03.3 covers shell config files).

## `man` and `--help`

```bash
man grep            # full manual page
grep --help          # quick summary, most commands support this
man -k partition      # search all page descriptions for "partition"
```

## `echo` and variable expansion

```bash
echo "Current user: $USER"
echo "Home directory: $HOME"
echo "Today: $(date)"
```
`$(...)` is **command substitution** — runs the command inside and substitutes its output as text.

## `export` and `env`

```bash
export MY_TOOL_PATH="/opt/tools"
env | grep MY_TOOL_PATH     # confirm it's in the environment
```

## `type` and `which`

```bash
type cd            # shell builtin
type ls              # usually an alias or a file path
which ls             # the actual executable file, if it's not a builtin
```
**Reading the difference:** `type` tells you *how* the shell will interpret a name (builtin, alias, function, or file) — more complete than `which`, which only finds files.

## Further Reading

- `man bash`, section on "SHELL BUILTIN COMMANDS"
