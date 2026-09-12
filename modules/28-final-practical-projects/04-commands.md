# Capstone Commands Reference

All commands used in the capstone appear in earlier modules. This file is a quick-reference summary.

```bash
# Workspace
mkdir -p ~/capstone/{scope,recon,evidence,findings,report}

# Recon
nmap -sV -T2 -oA ~/capstone/recon/scan <target>

# Enumeration
enum4linux -a <target> > ~/capstone/recon/smb-enum.txt
nmap --script=ftp-anon -p 21 <target>

# Evidence integrity
sha256sum ~/capstone/recon/* >> ~/capstone/evidence/hashes.txt

# Report
pandoc ~/capstone/report/final-report.md -o ~/capstone/report/final-report.pdf
```
