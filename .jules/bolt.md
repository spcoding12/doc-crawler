## 2024-05-18 - BeautifulSoup Optimization
**Learning:** Replacing .select() with .find_all() and checking tag.text instead of str(tag) provides significant performance gains.
**Action:** Always prefer native bs4 methods and specific attribute lookups over CSS selectors and full stringification in parsing tasks.
