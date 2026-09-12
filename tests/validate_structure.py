#!/usr/bin/env python3
"""
validate_structure.py

Checks that every module directory under modules/ contains at least a
README.md, and reports which of the standard lesson files are present vs.
missing for each module. This is informational for scaffolded modules
(missing files are expected there) and should be all-green for any module
listed as "Complete" in the main README.

Usage:
    python3 tests/validate_structure.py
"""

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
MODULES_DIR = REPO_ROOT / "modules"

STANDARD_FILES = [
    "README.md",
    "01-concepts.md",
    "02-installation.md",
    "03-practical-lab.md",
    "04-commands.md",
    "05-troubleshooting.md",
    "06-security-notes.md",
    "07-exercises.md",
    "08-challenge.md",
]

# Files that are legitimately optional for some modules even when complete
OPTIONAL = {"02-installation.md", "08-challenge.md"}

# Modules considered "complete" and thus held to a stricter standard
COMPLETE_MODULES = {
    "00-orientation",
    "01-linux-fundamentals",
    "02-kali-fundamentals",
    "03-terminal-and-bash",
    "04-filesystem-and-permissions",
    "05-users-groups-processes",
    "06-package-management",
    "07-services-and-sysadmin",
    "08-networking-fundamentals",
    "09-network-troubleshooting",
    "10-security-fundamentals",
    "11-reconnaissance-concepts",
    "12-network-enumeration",
    "13-traffic-analysis",
    "14-web-security-fundamentals",
    "15-vulnerability-assessment",
    "16-authentication-and-passwords",
    "17-defensive-security",
    "18-digital-forensics-fundamentals",
    "19-wireless-security-concepts",
    "20-exploitation-concepts-safe-labs",
    "23-ctf-and-practice-methodology",
    "24-vulnerability-research-fundamentals",
    "25-reporting-security-findings",
    "27-advanced-kali-workflows",
    "28-final-practical-projects",
    "29-career-and-further-learning",
    "21-automation-with-bash",
    "22-security-automation-with-python",
    "26-building-your-own-lab",
}


def main() -> int:
    if not MODULES_DIR.is_dir():
        print(f"ERROR: modules directory not found at {MODULES_DIR}", file=sys.stderr)
        return 1

    module_dirs = sorted(p for p in MODULES_DIR.iterdir() if p.is_dir())
    if not module_dirs:
        print("ERROR: no module directories found", file=sys.stderr)
        return 1

    problems = 0
    for mdir in module_dirs:
        missing = [f for f in STANDARD_FILES if not (mdir / f).is_file()]
        readme_missing = "README.md" in missing

        if readme_missing:
            print(f"[FAIL] {mdir.name}: missing README.md")
            problems += 1
            continue

        if mdir.name in COMPLETE_MODULES:
            required_missing = [f for f in missing if f not in OPTIONAL]
            if required_missing:
                print(f"[FAIL] {mdir.name} (marked Complete): missing {required_missing}")
                problems += 1
            else:
                print(f"[OK]   {mdir.name}: all required lesson files present")
        else:
            if missing:
                print(f"[INFO] {mdir.name} (scaffold): placeholder files present, "
                      f"{len(STANDARD_FILES) - len(missing)}/{len(STANDARD_FILES)} standard files exist")
            else:
                print(f"[OK]   {mdir.name}: all standard files present")

    print()
    print(f"Modules checked: {len(module_dirs)}")
    print(f"Hard failures (missing README, or missing required file in a Complete module): {problems}")

    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
