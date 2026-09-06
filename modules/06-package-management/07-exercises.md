# Exercises — Module 06

1. Run `dpkg -l | wc -l` and `apt list --installed | wc -l` and compare the counts — they should be close but not necessarily identical; investigate why if they differ significantly (hint: header/footer lines).
2. Pick any command you use regularly and find which package installed it, using `dpkg -S`.
3. Check `apt list --upgradable` on your system and explain, from the output alone, how you'd know if a security-relevant package had an update available.
4. Explain the practical difference between `apt remove` and `apt purge`, and describe one real scenario where the difference matters.
