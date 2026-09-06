# Troubleshooting — Module 01

**"command not found"**
The program isn't installed, or isn't in your `PATH`. Check with `which <command>`; install with `sudo apt install <package>` (Module 06).

**"Permission denied" running a script**
The file isn't marked executable. Run `chmod +x script.sh` then `./script.sh` (Module 04 covers this fully).

**`cd` says "No such file or directory"**
You likely have a typo, or you're not where you think you are — run `pwd` and `ls` before retrying.

**`rm` doesn't ask "are you sure?"**
Correct — Linux doesn't have a confirmation prompt or trash bin by default. This is intentional. Consider `rm -i` while learning, which *does* prompt per file.

**Terminal looks "frozen" after running a command**
Some commands (like `top`, `less`, `tail -f`) take over the screen until you quit them — `q` usually exits, `Ctrl+C` interrupts.
