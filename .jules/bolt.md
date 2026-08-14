## 2025-02-19 - Optimize BeautifulSoup DOM Traversal
**Learning:** Checking classes sequentially via `soup.select()` combined with lambda validations and array iteration is a severe performance bottleneck. Avoid serializing full elements via `str(tag)` on `<script>` tags as it incurs a massive performance penalty.
**Action:** Replace sequential `.select()` queries with optimized single-pass OR validations via `soup.find(class_=['class1', 'class2'])`. When extracting script content, use `.text` combined with explicit `.get('src')` lookups to eliminate serialization overhead.
