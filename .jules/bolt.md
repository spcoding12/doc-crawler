## 2025-02-28 - [Avoid str(tag) serialization in BeautifulSoup]
**Learning:** Stringifying BeautifulSoup objects (e.g. `str(tag)`) to execute text or attribute checks incurs a severe serialization performance penalty, especially for large `<script>` tags, completely negating regex or text search speed advantages.
**Action:** Always use native bs4 properties like `.text` and `.get()` for attribute lookups instead of serializing the tag to a string.
