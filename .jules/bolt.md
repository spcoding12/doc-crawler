## 2026-03-22 - [Module-Level Regex Compilation]
**Learning:** Pre-compiling multiple individual regexes at the module level is significantly more performant than dynamically compiling them within frequently called functions, especially in loops or high-throughput tasks like markdown cleaning.
**Action:** Always pre-compile regular expressions using `re.compile()` at the module level to avoid overhead from re-compilation and cache lookups.
