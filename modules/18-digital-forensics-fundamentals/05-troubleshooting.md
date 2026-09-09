# Troubleshooting — Module 18

**`strings` produces one giant unreadable line** — null bytes inside the file may not be separating strings properly; try `strings -n 5 file` (set a minimum string length) or `xxd file | head` to inspect the raw hex content and understand what's actually there.

**`file` reports "data" or "application/octet-stream"** — the file doesn't match any magic number in the `file` database; it might be encrypted, compressed (and thus opaque), or genuinely unknown — all are themselves forensically interesting findings.

**Timestamps on the sample evidence differ from the lesson** — correct; timestamps are set at the time you created the files on your own system, not when this dataset was authored. The lesson's timestamps are from the build sandbox — yours will show your creation time.

**`sha256sum` hashes don't match between Step 1 and Step 6** — something modified a file during your analysis; check which file changed and what process was running (`ps aux` from Module 05) — though in this lab that's almost certainly a filesystem metadata write rather than a security event.
