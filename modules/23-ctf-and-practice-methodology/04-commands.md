# Lesson 23.2 — Useful CTF Commands

These are general-purpose tools that appear in many CTF categories — all drawn from earlier modules.

## Forensics/General

```bash
file challenge_file            # what type of file is this actually?
strings challenge_file            # any readable text hidden inside?
xxd challenge_file | head          # raw hex dump
sha256sum challenge_file             # hash for comparison
```

## Crypto/Encoding

```bash
echo "aGVsbG8=" | base64 -d        # base64 decode
echo "68656c6c6f" | xxd -r -p         # hex decode
python3 -c "print(bytes.fromhex('68656c6c6f').decode())"   # hex decode via Python
```

## Web

```bash
curl -I http://challenge-url/          # check headers
curl -v http://challenge-url/            # see full request/response
curl -s http://challenge-url/ | grep -i "flag\|ctf"  # search response for flag pattern
```

## Network/Packets

```bash
tshark -r capture.pcap -Y "http"     # filter HTTP from a pcap
tshark -r capture.pcap -T fields -e http.file_data  # extract file data
```

## Quick Python helpers

```python
# Rotate cipher (Caesar)
import string
def rot(text, n):
    return text.translate(str.maketrans(
        string.ascii_lowercase + string.ascii_uppercase,
        string.ascii_lowercase[n:] + string.ascii_lowercase[:n] +
        string.ascii_uppercase[n:] + string.ascii_uppercase[:n]))

# XOR brute-force single byte
with open("file.bin","rb") as f: data = f.read()
for key in range(256):
    result = bytes(b ^ key for b in data)
    if b"flag" in result.lower(): print(key, result[:50])
```
