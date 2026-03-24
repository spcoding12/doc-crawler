
## 2024-05-15 - [Regex Pre-compilation Optimization]
**Learning:** Pre-compiling multiple individual regexes using `re.compile()` at the module level is more performant than dynamically joining multiple patterns or recreating patterns inside frequently called functions (like HTML/Markdown parsers or cleaners). Wait, bench show 2.58x speedup on loop logic.
**Action:** Always extract static regular expression patterns used in loops or frequent function calls to the module level and pre-compile them using `re.compile()`.
