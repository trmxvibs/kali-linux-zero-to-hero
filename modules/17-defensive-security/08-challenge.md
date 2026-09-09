# Challenge — Module 17

Building on Module 21 (Bash automation), write `service_audit.sh` (first sketched in Module 07's challenge):
- Accepts a list of expected-enabled services as arguments
- For each, reports whether it is enabled AND active (both states, not just one)
- Lists any *other* currently-running services not in your expected list, flagged as "UNEXPECTED — investigate"
- Saves the full output to a timestamped report file

Test it against your own Kali VM and document what, if anything, it flagged as unexpected.
