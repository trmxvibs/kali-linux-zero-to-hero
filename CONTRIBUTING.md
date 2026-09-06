# Contributing

Thank you for considering a contribution. This course is built to be
extended — most of its 30 modules are currently scaffolds waiting for full
content, following the exact format the completed modules already use.

## Ways to Contribute

- **Write a full module** from its current scaffold (see "Lesson Format" below)
- **Fix errors** in existing content (technical, factual, or typos)
- **Improve labs** — better reproducibility, clearer expected output
- **Add exercises/challenges** to existing modules
- **Report unsafe or unclear guidance** — especially anything that seems to
  conflict with `docs/getting-started/ethics-and-legal.md`
- **Translate** content (open an issue first to coordinate structure)
- **Test scripts and labs** on real hardware/VMs and report results

## The Lesson Format (Required)

Every lesson file should include, in order:

1. **Learning Objectives** — what the learner can do afterward
2. **Prerequisites** — what modules/knowledge are assumed
3. **Concept** — plain language first, then technical detail
4. **Why It Matters** — real-world/security relevance
5. **Commands** (if applicable) — for each command/tool: what it is, why it
   exists, what problem it solves, how it works conceptually, basic usage,
   a practical example, expected output, how to interpret that output,
   common mistakes, troubleshooting, defensive implications, and the
   legal/ethical boundary
6. **Safe Practical Lab** — a reproducible exercise
7. **Expected Result** — what the learner should see
8. **Common Mistakes** and **Troubleshooting**
9. **Security Perspective** — attacker view vs. defender view where relevant
10. **Exercise** and **Challenge** — practice without immediately giving the answer
11. **Further Reading** — authoritative sources (official docs, RFCs, OWASP, NIST)

Every module folder should contain (at minimum, as applicable):
```
README.md
01-concepts.md
02-installation.md      (skip if nothing to install)
03-practical-lab.md
04-commands.md
05-troubleshooting.md
06-security-notes.md
07-exercises.md
08-challenge.md
```

## Safety Requirements for New Content

- Every lab must target a system the learner owns, or a named, intentionally
  vulnerable training application (Metasploitable, DVWA, Juice Shop, WebGoat,
  or similar) inside an isolated network (Module 26)
- Every command with real-world risk must carry the `⚠️ LAB ONLY` warning
  format used throughout the repository
- Do not add content that could provide meaningful uplift toward attacking
  systems the reader doesn't own or lack authorization to test

## Testing Requirements

If you add or modify a script, lab, or set of commands:

- Actually run it before submitting — don't mark something as working from
  memory or assumption
- Note what you tested and on what (OS/Kali version, hypervisor) in your
  pull request description
- If a script is included, it must be syntax-checked (`bash -n script.sh` /
  `python3 -m py_compile script.py`) and exercised with at least one
  success case and one expected-failure case

## Pull Request Checklist

- [ ] Follows the Lesson Format above
- [ ] All commands/scripts were actually run and verified
- [ ] Every risky command has the `⚠️ LAB ONLY` warning
- [ ] No real, unauthorized targets referenced anywhere
- [ ] Links and file paths checked (run `python3 tests/validate_links.py`)
- [ ] Updated the module's status in the main `README.md` table if you completed a scaffold

## Code of Conduct

See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
