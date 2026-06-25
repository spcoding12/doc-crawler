## 2024-06-25 - Optimize BeautifulSoup logic
**Learning:** Re-evaluating multiple css queries via `.select()` and fully stringifying tags with `str(tag)` significantly degrades performance in large HTML files, whereas single-pass lookups with `.find(class_=[...])` and checking `.text` attributes provide extreme speedups.
**Action:** Use native attribute-based `BeautifulSoup` search functions like `find_all` and `find` combined with `.text` instead of CSS selector methods or stringification.
