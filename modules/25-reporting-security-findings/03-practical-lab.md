# Lab 25 — Writing a Complete Finding Report

**Environment:** Text editor — this is a writing lab.

## The Finding to Report

Use the vsftpd 2.3.4 / CVE-2011-2523 finding from Module 20 (or, if you haven't run Module 20 yet, use Module 15's vulnerability lookup result for vsftpd 2.3.4 as your basis).

## Steps

Write a complete finding document using the template from `01-concepts.md`:

```
Title:
Severity:
CWE:
Affected Component:
Prerequisites:
Reproduction Steps:
  1.
  2.
  3.
Evidence: (describe what you would capture — shell output, Metasploit session log)
Impact:
Remediation:
Limitations:
```

Then write a one-paragraph Executive Summary above the full finding.

## Self-Review Checklist

Before finalising:
- [ ] Can someone who wasn't in the room reproduce this from your steps alone?
- [ ] Is your severity rating justified by the impact you described — not higher, not lower?
- [ ] Is your remediation specific and actionable?
- [ ] Does your executive summary stand alone without needing the rest of the document?
- [ ] Did you state what you did NOT test (scope/limitations)?

## Expected Result

A complete, professional-quality finding document you could hand to a developer and expect them to act on without follow-up questions.

## Next Step

[Module 26 — Building Your Own Security Lab](../26-building-your-own-lab/README.md) (if not already completed) or [Module 27 — Advanced Kali Workflows](../27-advanced-kali-workflows/README.md).
