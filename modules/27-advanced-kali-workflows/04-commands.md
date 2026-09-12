# Lesson 27.2 — Efficiency Commands

## Nmap output formats

```bash
nmap -oN output.txt target      # normal (human-readable)
nmap -oG output.grep target       # greppable (script-friendly)
nmap -oX output.xml target         # XML (importable into tools)
nmap -oA output target              # all three at once
```

## Chaining enumeration

```bash
nmap -sn 192.168.56.0/24 -oG - | awk '/Up$/{print $2}' > live.txt
cat live.txt | xargs -I{} nmap -sV -T2 {}
```

## tmux — multi-window terminal (essential for long engagements)

```bash
tmux                              # start tmux
Ctrl+B then %                      # split pane vertically
Ctrl+B then "                       # split pane horizontally
Ctrl+B then arrow key                # switch between panes
Ctrl+B then d                         # detach (session survives SSH disconnect)
tmux attach                            # re-attach to a running session
```

## Kali tool discovery

```bash
apt-cache search "port scanner"    # find tools by description
kali-linux-top10                     # install Kali's top 10 tools metapackage
```
