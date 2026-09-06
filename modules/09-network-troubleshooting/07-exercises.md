# Exercises — Module 09

1. Walk through the full 6-step checklist from `01-concepts.md` against a real website of your choice, recording the actual command and result for each step.
2. Using two terminals and `nc`, reproduce the "listener only accepts one connection" gotcha from the lab yourself, and explain in your own words why it happens.
3. Explain the practical difference between a `nc -zv` "connection refused" result and a result that just hangs with no response, and what each implies about what's between you and the target.
4. Pick a port you expect to be closed on your own machine and one you expect to be open, and confirm both with `nc -zv`.
