# Test Log

This documents exactly what was executed and verified while building this
release, and what was **not** tested and still requires a real Kali/VM
environment. Nothing below is claimed as tested unless it was actually run
and its output inspected during development.

**Test environment used:** a sandboxed Ubuntu 24.04 Linux container (not a
Kali VM). It has: standard GNU coreutils, `bash`, `python3` (3.x, standard
library only), `grep`/`awk`/`find`. It does **not** have: internet/network
egress, `iproute2` (`ip`, `ss`), `ping`, `dig`, `curl`-to-internet, or
Kali-specific tools (`nmap`, Metasploit, Wireshark, etc.) installed.

## TESTED

### Module 01 — Linux Fundamentals
- Every command shown in `04-commands.md` that doesn't require networking
  (`pwd`, `ls -la`, `mkdir`, `touch`, `cp`, `mv`, `rm`, `rmdir`, `cat`,
  `head`, `tail`, `grep`, `find`, `which`, `ps aux`) was executed directly
  and produced the documented output shape.
- The full `03-practical-lab.md` walkthrough was executed end to end; the
  final `find` output matched what the lesson documents (modulo the actual
  home directory path).

### Module 21 — Automation with Bash
- `scripts/bash/system_info_collector.sh`: syntax-checked (`bash -n`),
  executed with and without an output-file argument, output inspected.
- `scripts/bash/log_analyzer.sh`: syntax-checked, executed against
  `labs/log-analysis/sample.log` with and without a keyword argument;
  executed against a missing file and with no arguments to confirm correct
  error messages and exit code `1` in both cases.
- Confirmed `log_analyzer.sh` reports exactly 3 matches for
  `"Failed password"` from `203.0.113.5` against the fixed sample log —
  this exact figure is what the module's lesson and exercises reference.

### Module 22 — Security Automation with Python
- `scripts/python/file_hash_generator.py`: compiled
  (`python3 -m py_compile`), run against a real file with `sha256` (default)
  and `md5`, and **cross-checked against the system's own `sha256sum`
  output — digests matched exactly**. Also tested: a missing file (exit
  code `1`, clear error on stderr), an invalid `--algo` value (argparse
  exit code `2`), and hashing multiple files in one invocation.
- `scripts/python/log_parser.py`: compiled, run against
  `labs/log-analysis/sample.log` in both table and `--json` mode; output
  verified by hand against the sample log's contents (3 failed / 0 accepted
  for `203.0.113.5`, etc.). Also tested: a missing file (exit code `1`) and
  a file with no matching lines (correct "no matches" message, exit `0`).

### Repository-wide tooling
- `tests/validate_structure.py`: run against the full repository; initially
  caught 3 real gaps (Modules 00, 08, 26 missing files their own status
  claimed existed), which were fixed, then re-run to a clean pass across
  all 30 modules.
- `tests/validate_links.py`: run against the full repository (276 Markdown
  files, 463 relative links checked); initially caught 9 broken links
  (references to this test log before it existed, and module README tables
  listing optional files that were deliberately not created), which were
  fixed, then re-run to a clean pass (0 broken links).

### Module 02 — Kali Fundamentals
- `uname -a`, `cat /etc/os-release`, `whoami`, `id` executed and confirmed
  to produce the documented output shape (on the Ubuntu sandbox, standing
  in for Kali's near-identical Debian-based output — the commands
  themselves are identical on real Kali; only exact OS name/version text
  differs, which is called out in the lesson).

### Module 03 — Terminal & Bash
- `$PATH`, `export`/variable expansion, single vs. double quote behavior,
  `$(...)` command substitution, and `alias` were all executed directly.
- Specifically confirmed: `echo "$VAR"` expands, `echo '$VAR'` does not.
- Confirmed a real, worth-documenting nuance: `alias` does **not** expand
  inside a non-interactive `bash -c` invocation (Bash only expands aliases
  in interactive shells by default) but **does** work correctly in an
  actual interactive shell (`bash -i -c`) — both were tested to confirm
  this distinction before it was written into the lesson's troubleshooting
  section.

### Module 04 — Filesystem & Permissions
- The entire `03-practical-lab.md` was executed end to end, exactly as
  written, including cleanup. Every single command's output was captured
  and matched what the lesson documents:
  - `chmod 754` vs. `chmod u=rwx,g=rx,o=r` confirmed byte-identical via
    `stat -c "%a"`
  - Default `umask` (`0022`) confirmed to produce `644` files / `755`
    directories
  - SUID confirmed to display as uppercase `S` (`-rwSr--r--`) before the
    owner-execute bit is set, and lowercase `s` (`-rwsr--r--`) after —
    this exact behavior was verified, not assumed, and is called out
    explicitly in the lesson as a common point of confusion
  - Sticky bit confirmed to display as trailing `t` in `ls -ld` output

### Module 05 — Users, Groups & Processes
- The entire `03-practical-lab.md` was executed end to end: `useradd -m`,
  `passwd` (via `chpasswd` in the non-interactive sandbox), `groupadd`,
  and — critically — `usermod -aG` was tested twice in sequence to
  **confirm the append behavior actually preserves prior group
  memberships** (`labuser` correctly retained both `labgroup` and
  `labgroup2`), which is the exact behavior the lesson's warning about
  `-aG` vs. `-G` depends on.
- Background job creation (`sleep 120 &`), `ps aux` lookup, and `kill`
  were tested and confirmed to cleanly terminate the process.
- The UID-0 audit command (`awk -F: '$3 == 0 {print $1}' /etc/passwd`)
  was run and confirmed to show only `root` on a clean system.
- All test accounts/groups were deleted at the end of testing.

### Module 06 — Package Management
- `dpkg -l`, `dpkg -L <package>`, `apt list --installed`, and
  `apt-cache policy <package>` were all executed against real installed
  packages (`bash` used as the test package, since the sandbox has no
  internet to install new ones) and produced the documented output shapes.
- Confirmed a real, worth-documenting nuance: `dpkg -S /bin/bash` fails
  with "no path found" because `/bin/bash` is a symlink; `dpkg -S` needs
  the resolved path (`dpkg -S /usr/bin/bash`, or `dpkg -S "$(realpath ...)"`)
  — this was caught by testing and written into both the lesson and its
  troubleshooting section, not assumed in advance.

### Module 09 — Network Troubleshooting
- Every `nc` (netcat) example was actually executed: a local listener
  (`nc -l -p <port>`) started, confirmed reachable with `nc -zv` (exact
  "succeeded" output captured), and confirmed that a closed port produces
  an immediate "Connection refused" (exit code 1) rather than a hang.
- Discovered and documented a genuine gotcha through testing: `nc -l`
  accepts exactly one connection before exiting, so reusing a listener
  across a `-zv` check and then a data-transfer test fails — this was
  caught by an initial failed test run, root-caused, and turned into a
  deliberate teaching moment in the lab rather than silently fixed and
  hidden.
- `ip`, `ping`, and `dig` (steps 1–4 of the module's checklist) were
  **not** live-tested — see NOT TESTED section below, same limitation as
  Module 08.

### Module 10 — Security Fundamentals
- Every cryptography example was executed with real `openssl` commands:
  - SHA-256 hashing of two near-identical files, confirmed completely
    different digests
  - AES-256-CBC symmetric encryption/decryption round-trip with the
    correct password, confirmed exact plaintext recovery
  - The same decryption attempted with a wrong password, confirmed to
    fail with a non-zero exit code and a "bad decrypt" error — and
    confirmed (by direct inspection with `wc -c`, not by printing to the
    terminal) that a failed decrypt writes a small amount of raw binary
    output before erroring, which is why the lab explicitly instructs
    redirecting output to a file rather than printing directly — this
    instruction exists because printing the raw failed-decrypt output
    directly during testing corrupted the test terminal's rendering, a
    real problem this course's build encountered firsthand
  - RSA 2048-bit key generation, public-key encryption, and private-key
    decryption round-trip, confirmed exact message recovery

### Module 12 — Network Enumeration
- The core banner-grabbing mechanic was tested directly: a simulated
  service (`printf "FAKE-SERVICE-BANNER-1.0\r\n" | nc -l -p 9000`) and a
  plain `nc localhost 9000` client confirmed the exact connect-and-read
  behavior the lesson describes, before being applied conceptually to real
  services (FTP, SSH) in the lab.
- `smbclient`, `enum4linux`, `showmount`, and Nmap NSE scripts were **not**
  live-tested — see NOT TESTED section below; the build sandbox has no
  Metasploitable VM and no network access.

### Module 13 — Traffic Analysis
- Actively checked for any usable packet-capture capability in this
  sandbox before writing the module: confirmed `tcpdump` and `tshark` are
  both absent (`which` returns nothing), and confirmed Python's `scapy`
  and `dpkt` libraries are not installed either (`pip show` and direct
  import both fail). This negative result is itself a tested, verified
  fact, not an assumption — it's why the entire module is written from
  documentation rather than partially faked with a workaround.

### Module 14 — Web Security Fundamentals
- `python3 -m http.server` and `curl -I`/`curl -v` against it were both
  executed; the exact header output shown in the lesson (`Server:
  SimpleHTTP/0.6 Python/3.12.3`, etc.) was captured live, not invented.
- `labs/web-security/sqli_demo.py` was written, compiled, and run multiple
  times. Confirmed: a normal login succeeds; the injection payload
  `admin' -- ` bypasses the vulnerable string-concatenation version and
  returns the admin row despite a wrong password; the identical payload
  against the parameterized (safe) version returns zero rows.
- **A real mistake was caught by testing, not assumed correct:** an
  initial draft of the lab claimed the payload `' OR '1'='1` (without a
  trailing comment) would return every row in the table. Running it
  actually returned **zero rows**, because SQL's `AND` operator binds
  tighter than `OR`, making the real resulting condition
  `username='' OR ('1'='1' AND password='anything')` — false for every
  row since no real password equals the literal string `anything`. A
  second payload, `' OR '1'='1' -- ` (which comments out the password
  check entirely), was then tested and confirmed to correctly return
  every row. The lab was rewritten to walk through this exact discovery
  rather than silently fixing the mistake and hiding that it happened.

### Module 15 — Vulnerability Assessment
- `labs/vulnerability-assessment/vuln_lookup.py` and its `known_vulns.json`
  dataset were written, compiled, and run: a valid lookup, `--list` mode,
  an unknown-service lookup (confirmed to return a clear "not found"
  message and exit code 1, not a false "safe" implication), and no-argument
  invocation (confirmed to print help and exit code 2) were all tested.
- The vsftpd 2.3.4 / CVE-2011-2523 worked example was fact-checked via web
  search against multiple independent sources (GitHub PoC repositories,
  a Twingate CVE report, a Medium write-up) before being written into the
  lesson, confirming: the CVE ID, the CWE-78 classification, the port 6200
  backdoor mechanism, and the general nature of the vulnerability.

### Module 16 — Authentication & Password Security
- `labs/password-security/hashing_demo.py` was written, compiled, and run.
  Confirmed: identical passwords produce identical SHA-256 hashes without
  a salt; the same password with two different random salts produces two
  different hashes; a 5-word dictionary attack against a known weak
  password succeeds in a fraction of a millisecond.
- The lesson's "predict what happens with a random 20-character password"
  exercise was tested directly before being written up: a
  `secrets.token_hex(10)`-generated password was confirmed **not** found
  by the same 5-word wordlist, and this result was used to add an explicit
  clarification that dictionary attacks only succeed against passwords
  actually present in the list — not a general statement about SHA-256
  being "broken."
- The Module 16 challenge's claimed numbers (20 distinct hashes without
  salt vs. 1,000 distinct hashes with salt, for 1,000 simulated users
  drawn from 20 common passwords) were verified by directly running the
  described logic before being included as a challenge.
- `bcrypt` and `argon2` Python libraries were checked and confirmed absent
  from this sandbox — flagged explicitly in the lesson rather than
  presented with fabricated example output.

## NOT TESTED — REQUIRES A REAL ENVIRONMENT

- **Any command requiring `ip`, `ss`, `ping`, `dig`, or internet-facing
  `curl`/`wget`** (all of Module 08's `04-commands.md`, Module 09's steps
  1-4, and the networking
  parts of Module 26) — these require a real network stack and internet
  access this sandbox does not have. The commands are standard, well-
  documented Linux networking utilities and their syntax was checked
  against their official man pages/documentation, but their live output
  was not captured in this environment.
- **`systemctl`, `journalctl`, and `crontab` (Module 07)** — this sandbox's
  container does not run `systemd` as PID 1; every `systemctl`/`journalctl`
  command tested returned `"System has not been booted with systemd as
  init system (PID 1). Can't operate."` Module 07's commands are written
  against official `systemd` and `cron` documentation and are standard,
  well-established syntax, but were **not live-executed** during this
  build. This is flagged explicitly at the top of Module 07's
  `04-commands.md`. Verify against a real Kali VM before treating this
  module as fully tested.
- **`john` (John the Ripper), `hashcat`, `bcrypt`, and `argon2` (Module 16)**
  — none are installed in this sandbox (confirmed directly: `pip show
  bcrypt` and a direct `import bcrypt`/`import dpkt`-style check both
  failed). Module 16's core teaching claims (fast-hash brute-forcing,
  salting) were fully demonstrated instead using Python's built-in
  `hashlib`, which required no external tools and was fully tested.
- **`tcpdump`, Wireshark, and `tshark` (Module 13)** — none of these are
  installed in this sandbox (confirmed directly, not assumed — see the
  TESTED section above), and there is no network traffic to capture even
  if they were. Module 13's commands are standard, well-documented
  `tcpdump`/Wireshark syntax, but were **not live-executed**. Verify
  against a real Kali VM.
- **Nmap and any Kali-specific tool** (Module 11's `04-commands.md` and
  Module 12's `smbclient`/`enum4linux`/`showmount`/NSE scripts,
  including the exact scan output shown) — none of these tools are
  installed in this sandbox and there is no Metasploitable VM available to
  scan or enumerate. The example
  output shown in Modules 11–12 is realistic, commonly-documented example
  output (consistent with widely published Metasploitable 2 results) but was
  **not captured from a live scan/enumeration during this build**.
- **The full two-VM lab setup in Module 26** (`02-installation.md`,
  `03-practical-lab.md`) — this requires a hypervisor (VirtualBox/VMware),
  a Kali ISO, and a Metasploitable image, none of which exist in this
  sandboxed environment. The steps follow each tool's official
  documentation but have not been reproduced click-by-click here.
- **Kali Linux installation itself** (referenced by Module 02, currently a
  scaffold) — not tested in this release.
- Any scaffolded module's placeholder content — by definition, scaffolds
  contain no tested claims, only a structural placeholder notice.

## How to Extend This Log

Any contribution that adds or modifies a script, lab, or command sequence
must add a corresponding entry here (or a note in the pull request) stating
exactly what was run and on what environment — see `CONTRIBUTING.md`.
