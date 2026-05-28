## 2026-05-28 - [BeautifulSoup select vs find_all optimization]
**Learning:** Using multiple CSS selector checks with `.select()` is ~5x slower than using single-pass `.find()` operations with lists of classes, and specific attribute checks (like meta generators).
**Action:** Replace `.select()` with `.find()`/`.find_all()` for simple ID, class, and attribute lookups to optimize DOM traversals in python web crawlers.
