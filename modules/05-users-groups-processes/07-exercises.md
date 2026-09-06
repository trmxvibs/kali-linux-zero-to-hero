# Exercises — Module 05

1. Explain, in your own words, why `/etc/passwd` is world-readable but `/etc/shadow` is not.
2. Run `awk -F: '$3 == 0 {print $1}' /etc/passwd` on your own system and confirm only `root` appears.
3. Create a user, add them to two groups using the correct (`-aG`) method, and verify both memberships with `id`. Clean up afterward.
4. Start three background `sleep` jobs, list them with `jobs`, and terminate exactly the second one by its job number (`kill %2`).
