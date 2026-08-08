## 2024-05-18 - [Optimize BeautifulSoup queries in framework detector]
**Learning:** Using `soup.find(class_=[...])` to check multiple class names in a single pass is drastically faster than executing multiple `.select()` statements and looping. Additionally, replacing `str(tag)` or `.string` with `.text` on `<script>` tags yields significant performance improvements while avoiding full serialization overhead.
**Action:** Always prefer `find(class_=[...])` over `.select()` arrays when checking for multiple alternative classes. Use `.text` for fast, robust tag text extraction.
