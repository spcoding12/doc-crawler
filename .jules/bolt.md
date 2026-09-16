## 2024-03-24 - Optimize BeautifulSoup select overhead
**Learning:** `soup.select()` is relatively slow compared to `soup.find()` / `soup.find_all()` with attributes/classes due to CSS selector parsing and evaluation.
**Action:** Replace `soup.select()` with faster `soup.find_all(class_=[...])` or direct attribute lookups in performance-critical paths like framework detection.
