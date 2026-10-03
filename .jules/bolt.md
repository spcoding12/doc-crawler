
## 2024-05-14 - BeautifulSoup Performance Anti-pattern: Stringifying Tags
**Learning:** In `src/detector.py`, stringifying BeautifulSoup objects (e.g., `str(tag)`) within loops to execute `in` checks incurs a severe serialization performance penalty. Benchmarks show `str(tag)` takes ~2.8s for 100 iterations of 1000 tags, while using `.get('src', '')` and `.text` takes ~0.8s.
**Action:** Always avoid `str(tag)` when checking tag contents or attributes. Instead, use native bs4 methods and properties like `.get('attr', '')` and `.text` to perform these checks robustly without the overhead of serializing the DOM tree back to a string.
