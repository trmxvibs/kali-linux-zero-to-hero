# Lesson 04.2 — Permission Commands

## `chmod` — change permissions

**Symbolic mode:**
```bash
chmod u+x script.sh          # add execute for owner (user)
chmod g-w file.txt            # remove write for group
chmod o=r file.txt             # set "other" to exactly read-only
chmod a+r file.txt              # add read for all (user, group, other)
```
**Numeric (octal) mode:**
```bash
chmod 754 script.sh            # owner=rwx(7), group=rx(5), other=r(4)
chmod 644 file.txt              # owner=rw(6), group=r(4), other=r(4) — common default for regular files
chmod 755 script.sh             # owner=rwx(7), group=rx(5), other=rx(5) — common for scripts/executables
```
**Tested and confirmed:** `chmod u=rwx,g=rx,o=r file` and `chmod 754 file` produce byte-identical results — verified with `stat -c "%a"` during this course's build.

## `chown` and `chgrp`

```bash
chown kali file.txt             # change owner
chown kali:kali file.txt         # change owner AND group
chgrp kali file.txt               # change group only
```
> ⚠️ Changing ownership generally requires root/`sudo` unless you're the current owner giving it to a group you belong to.

## `umask`

```bash
umask              # show current umask (commonly 0022)
umask 027           # set a stricter umask for this session
```
**Reading it:** the umask is *subtracted* from the maximum (666 for files, 777 for directories) at creation time. A umask of `022` on a new file (max 666) results in `644` — confirmed by direct testing during this course's build.

## SUID / SGID / Sticky Bit

```bash
chmod u+s program        # set SUID
chmod g+s directory        # set SGID on a directory
chmod +t directory          # set sticky bit
chmod u-s program            # remove SUID
```
**Finding all SUID files on a system** (from Module 01, revisited here with context):
```bash
find / -perm -4000 -type f 2>/dev/null
```

## Further Reading

- `man chmod`, `man chown`, `man umask`
