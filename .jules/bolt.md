
## 2024-05-18 - Optimize BeautifulSoup Framework Detection
**Learning:** Using `str(tag)` for text serialization on script tags is severely unoptimized. Additionally, evaluating independent CSS class selectors via `soup.select` or sequential `.find()` calls iterates the DOM multiple times.
**Action:** Always use `.text` for tag extraction if attributes aren't needed. Consolidate multiple independent class existence checks into a single pass operation using `soup.find(class_=['class1', 'class2'])`.
