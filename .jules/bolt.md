## 2024-05-14 - Optimize BeautifulSoup Text Extraction
**Learning:** Stringifying a BeautifulSoup tag with `str(tag)` incurs a severe serialization performance penalty (~8x slower) compared to extracting text natively with `tag.get('src', '')` and `tag.text`.
**Action:** Always use native bs4 methods for text extraction and attribute checking instead of full string serialization to avoid unnecessary overhead in DOM operations.
