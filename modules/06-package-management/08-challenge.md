# Challenge — Module 06

Write a short Bash script `package_audit.sh` (building on Module 21 concepts, previewed here) that:
- Takes a package name as an argument
- Reports whether it's installed, and if so, its installed version
- Reports whether a newer version is available (via `apt-cache policy`)
- Exits with a clear, distinct exit code for: package not found in repositories, package not installed, package installed and up to date, package installed but outdated

This is a preview of the automation skills formalized in Module 21 — it's fine if your first version is rough.
