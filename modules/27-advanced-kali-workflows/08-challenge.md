# Challenge — Module 27

Automate your entire Module 11–15 workflow into a single script:
- Takes a target IP as an argument
- Creates a timestamped workspace directory
- Runs conservative nmap (initial, then service scan)
- Runs enum4linux if SMB is detected
- Hashes all output
- Prints a summary: discovered services, notable findings, evidence hashes

This is a real, useful tool — the kind security professionals actually build and reuse across engagements.
