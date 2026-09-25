## 2024-05-25 - BeautifulSoup script text extraction
**Learning:** Using `str(tag)` on a BeautifulSoup tag (like `<script>`) to perform substring matching is a significant performance anti-pattern. Stringifying the entire tag incurs a huge overhead.
**Action:** Use `script.get('src', '')` and `script.text` to inspect the contents of script tags. It's an order of magnitude faster and avoids string serialization.
