## 2024-07-19 - Avoid str() for BeautifulSoup tags
**Learning:** Stringifying BeautifulSoup tags with `str(tag)` incurs a massive performance penalty (~50x slower) compared to extracting specific attributes (`tag.get('src')`) and text content (`tag.text`).
**Action:** Use native BeautifulSoup properties like `.get()` for attributes and `.text` for content instead of serializing the entire tag to a string when checking for substrings.
