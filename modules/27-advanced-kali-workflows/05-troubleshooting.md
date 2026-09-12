# Troubleshooting — Module 27

**Nmap `-oA` produces three files but I only see one** — the flag creates three files with the same base name and different extensions (`.nmap`, `.gnmap`, `.xml`); check with `ls output.*`.

**tmux session lost after terminal closed** — if you detached (`Ctrl+B d`) before closing, `tmux attach` recovers it; if you closed without detaching, the session is gone. Use `Ctrl+B d` before closing any terminal running a long scan.

**Workspace getting disorganised mid-engagement** — stop and reorganise before continuing; a messy evidence directory mid-engagement compounds into a messy report. Five minutes of organising now saves an hour of reconstruction later.
