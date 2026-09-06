# Troubleshooting — Module 06

**"Unable to locate package"** — run `sudo apt update` first; your local package index may be stale or missing the relevant repository.

**"Could not get lock /var/lib/dpkg/lock"** — another package operation (or a background updater) is already running; wait for it to finish, or confirm no other `apt`/`dpkg` process is stuck (`ps aux | grep apt`).

**`dpkg -S somefile` says "no path found matching pattern"** — the path may be a symlink; resolve it first: `dpkg -S "$(realpath somefile)"`.

**`apt full-upgrade` wants to remove packages I didn't expect** — read the proposed changes carefully before confirming; this usually means a dependency chain changed upstream. It's rarely wrong, but always worth reading rather than blindly confirming with `-y` on a production system.

**Third-party repository breaks `apt update`** — remove the offending `.list`/`.sources` file from `/etc/apt/sources.list.d/` and re-run `apt update`.
