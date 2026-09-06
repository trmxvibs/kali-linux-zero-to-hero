# Exercises — Module 04

1. Convert `rwxrwxr-x` to octal notation by hand, then verify with `chmod` and `stat -c "%a"`.
2. Explain, in one sentence each, the difference between SUID and SGID.
3. Find at least 2 real SUID binaries on your own Linux system with `find / -perm -4000 -type f 2>/dev/null`, and look up (via `man` or online) what one of them is for and why it legitimately needs SUID.
4. Set a umask of `077` for your current session, create a new file, and confirm it's readable/writable only by you.
