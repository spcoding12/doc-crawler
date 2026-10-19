## 2025-05-24 - Avoid stringifying BeautifulSoup tags
**Learning:** Stringifying existing BeautifulSoup objects (e.g., `str(tag)`) to perform substring checks incurs a severe serialization performance penalty.
**Action:** When extracting text from tags (such as `<script>`), use `.text` and explicitly check relevant attributes like `.get('id', '')` or `.get('src', '')` instead of using `str(tag)`.
