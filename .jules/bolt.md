## 2024-05-24 - Optimize script tag parsing in BeautifulSoup
**Learning:** Using `str(tag)` or `.string` on BeautifulSoup tags incurs a significant serialization overhead, especially for large tags like `<script>`.
**Action:** Always use `.text` and explicitly check attributes like `.get('src', '')` instead of serializing the entire tag to a string when searching for keywords.
