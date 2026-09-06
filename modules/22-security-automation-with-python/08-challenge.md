# Challenge — Module 22

Build a "Security Report Generator" that combines this module's two scripts conceptually:

- Accepts a directory of log files and a directory of files-to-integrity-check
- Produces a single JSON report containing: (a) the log_parser-style summary for every log file, and (b) the SHA-256 hash of every file in the integrity-check directory
- Handles missing/unreadable files gracefully (report the error per-file, don't crash the whole run)
- Include a small set of test files and document, in a comment block at the top of the script, exactly what you tested and what the expected output was — following the same standard this course holds itself to.
