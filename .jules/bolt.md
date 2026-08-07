## 2026-08-07 - Optimize BeautifulSoup queries in framework detector
**Learning:** Replacing `.select()` with `.find()`/`.find_all()`, combining `class_` queries, and using `.text` over `str(tag)` drastically improves parsing performance in `src/detector.py` for large DOMs. Also, version extraction must precede generic early returns.
**Action:** Always prefer native bs4 methods over CSS selectors when checking for classes, and avoid serialization penalties.
