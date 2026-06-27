## 2024-06-27 - Optimize BeautifulSoup DOM Traversal
**Learning:** Replaced `.select()` and list of indicators with direct `.find()`/`.find_all()` lookups and lists of classes (`class_=['a', 'b']`). Avoided `str(tag)` for script text checking, instead using `.text`. This significantly speeds up framework detection.
**Action:** Always prefer `.find()` with exact attributes over `.select()`, and use `.text` instead of stringifying an entire tag.
