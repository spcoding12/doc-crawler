## 2024-05-23 - Optimize BeautifulSoup DOM Traversal
**Learning:** Using `.select()` for attribute and class checks, and using `str(tag)` instead of `.text` causes significant parsing overhead and bottlenecks in HTML structure scanning. Combining checks via `.find(class_=[...])` and checking specific attributes runs much faster.
**Action:** Avoid `.select()` when simple `.find()` or `.find_all()` is sufficient. Use `.find(class_=[...])` for combined class checks. Never use `str(tag)` for checking contents of script tags; use `.text` and explicitly check `.get('src')`.
