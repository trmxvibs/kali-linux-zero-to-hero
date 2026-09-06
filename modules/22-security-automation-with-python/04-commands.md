# Lesson 22.2 — Running the Scripts

## `file_hash_generator.py`

```bash
python3 file_hash_generator.py myfile.txt
python3 file_hash_generator.py myfile.txt --algo md5
python3 file_hash_generator.py file1.txt file2.txt   # multiple files at once
```
**Expected output:**
```
SHA256  a948904f2f0f479b8f8197694b30184b0d2ed1c1cd2a1ec0fb85d299a192a447  myfile.txt
```
**Exit codes:** `0` success, `1` one or more files unreadable/missing, `2` bad arguments (e.g. invalid `--algo`).

## `log_parser.py`

```bash
python3 log_parser.py auth.log
python3 log_parser.py auth.log --json
```
**Expected output (table mode):**
```
IP Address          Failed    Accepted
----------------------------------------
203.0.113.5         3         0
```
**Exit codes:** `0` success (including "no matches found," which is a valid outcome, not an error), `1` file not found.

## Further Reading

- `python3 file_hash_generator.py --help`
- `python3 log_parser.py --help`
