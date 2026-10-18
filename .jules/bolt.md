
## 2024-05-18 - [Optimize framework detection DOM traversal]
**Learning:** Using `soup.select()` invokes the heavier `cssselect` parser and involves multiple DOM sweeps, and using `str(tag)` incurs massive serialization overhead on large elements like `<script>`.
**Action:** Replace `soup.select()` with native, highly optimized `soup.find()` and `soup.find_all()` methods. Map CSS attribute and class queries to exact BS4 native equivalents (e.g. `soup.find(class_=['a', 'b'])`). For `<script>`, check `.text`, `.get('src')`, and `.get('id')` to avoid string allocation overhead.
