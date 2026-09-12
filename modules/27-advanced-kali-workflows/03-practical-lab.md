# Lab 27 — Building an Efficient Engagement Workspace

**Environment:** Your Kali VM.

## Steps

1. Create a clean engagement workspace:
   ```bash
   mkdir -p ~/engagement-lab/{scope,recon,evidence/{screenshots,captures},findings,report}
   echo "192.168.56.0/24" > ~/engagement-lab/scope/targets.txt
   ```

2. Run a full recon workflow saving all output:
   ```bash
   nmap -sV -T2 -oN ~/engagement-lab/recon/nmap-services.txt <metasploitable-ip>
   nmap -sV -oG ~/engagement-lab/recon/nmap-grep.txt <metasploitable-ip>
   ```

3. Hash all recon output immediately:
   ```bash
   sha256sum ~/engagement-lab/recon/* > ~/engagement-lab/evidence/hashes.txt
   ```

4. Create a finding file from your nmap results:
   ```bash
   cp modules/25-reporting-security-findings/08-challenge.md \
      ~/engagement-lab/findings/finding-001.md
   # Edit it with your actual nmap findings
   ```

5. Review: can you reconstruct everything you did from this directory alone? If not, what's missing?

## Expected Result

A workspace that is self-documenting — someone who wasn't there could follow what was done, when, and what was found, purely from the directory structure and its contents.
