# Lesson 21.2 — Text Processing Building Blocks

## Pipes (`|`) and redirection (`>`, `>>`, `2>`)

```bash
ps aux | grep ssh          # pipe: feed one command's output into another
echo "log line" > out.txt   # redirect stdout, OVERWRITING out.txt
echo "another" >> out.txt   # redirect stdout, APPENDING
command 2> errors.txt       # redirect only stderr
```

## `awk` — column-based text processing

```bash
ps aux | awk '{print $1, $2, $11}'   # print columns 1, 2, 11 (user, pid, command)
awk -F: '{print $1}' /etc/passwd      # -F sets the field separator to ':'
```

## `sed` — stream editing

```bash
sed 's/foo/bar/' file.txt        # replace first "foo" per line with "bar"
sed -i 's/foo/bar/g' file.txt    # -i edits the file in place, g = all occurrences
```

> ⚠️ `sed -i` modifies the file immediately with no confirmation — test on a copy first.

## Combining them (the actual point of this lesson)

```bash
grep "Failed password" /var/log/auth.log | awk '{print $(NF-3)}' | sort | uniq -c | sort -rn
```
This single line: filters failed logins, extracts the source IP column, counts occurrences per IP, and sorts by frequency — the same logic `log_analyzer.sh` implements as a reusable script.

## Further Reading

- `man awk`, `man sed`
- [GNU sed manual](https://www.gnu.org/software/sed/manual/sed.html)
