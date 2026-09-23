## 2024-05-20 - BeautifulSoup DOM Traversal Optimization
**Learning:** `soup.select()` parsing and executing `str(tag)` for stringification carry enormous serialization and DOM traversal overhead compared to targeted `soup.find_all()` or `soup.find()` calls. Consolidating multiple class checks into a single list (e.g., `class_=['class1', 'class2']`) drastically improves traversal performance.
**Action:** Replace CSS selector (`.select`) loops with direct `soup.find_all()` or `soup.find(class_=[...])`. Avoid `str(tag)` in favor of `.text` or `tag.get('src', '')`.
