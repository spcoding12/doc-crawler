
## 2025-05-25 - Optimize BeautifulSoup element lookup performance
**Learning:** Using `soup.select()` and `str(tag)` incurs a significant performance penalty (100x slower) in repetitive element checks during framework detection. Using `.find()` and `.find_all()` with direct attribute/class lookups (e.g. `soup.find(class_=['class1', 'class2'])`) and using `.text` instead of `str()` or `.string` drastically improves traversal time.
**Action:** Always prefer `.find()` and `.find_all()` with class lists for OR logic instead of CSS selectors when checking for multiple specific classes.
