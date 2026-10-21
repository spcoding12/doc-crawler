
## 2024-10-24 - HTML parsing overhead in framework detection
**Learning:** In BeautifulSoup, using `soup.select()` with CSS selectors is significantly slower than native tree traversal methods like `soup.find()` and `soup.find_all(class_=['a', 'b'])`. Additionally, calling `str(tag)` on large tags (like `<script>` bundles) incurs a massive serialization penalty.
**Action:** Always prefer native DOM traversal methods (`find`/`find_all`) over CSS selectors for performance-critical HTML parsing. Avoid stringifying large DOM nodes; extract only the necessary attributes (`get('src')`) or inner text (`.text`) to check for signatures.
