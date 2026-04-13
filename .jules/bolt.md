
## 2024-04-13 - [Pre-compiling multiple regex patterns]
**Learning:** Compiling lists of multiple regular expressions at the module level (e.g., `[re.compile(p) for p in [...]]`) is measurably faster than dynamically defining and compiling them inside a frequently called function, as it avoids repetitive list instantiation and iteration overhead. Pre-compiling multiple individual regexes is also more performant than joining multiple patterns into a single large regex using the `|` (OR) operator.
**Action:** Always pre-compile regex patterns at the module level if they are used repeatedly, especially in loops or frequently executed functions.
