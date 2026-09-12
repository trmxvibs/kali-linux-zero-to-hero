# Lesson 25.2 — Report Generation Helpers

## Markdown-based report template (version-controlled, diffable)

A plain Markdown file is the most portable, version-controllable format for security findings. The template from `01-concepts.md` works directly as a `.md` file.

```bash
cp modules/25-reporting-security-findings/finding-template.md ~/findings/finding-001.md
```

## Screenshot capture on Kali

```bash
scrot -s ~/evidence/screenshot.png    # -s = interactive region selection
```

## Hashing evidence before including it

```bash
sha256sum evidence/* | tee evidence/hashes.txt    # hash everything and save the manifest
```

## Generating a PDF from Markdown (if needed for delivery)

```bash
# Requires pandoc: sudo apt install pandoc
pandoc finding.md -o finding.pdf
```

## Archiving a complete finding package

```bash
tar -czvf finding-001-package.tar.gz ~/findings/finding-001/ ~/evidence/
sha256sum finding-001-package.tar.gz   # hash the package itself for chain of custody
```
