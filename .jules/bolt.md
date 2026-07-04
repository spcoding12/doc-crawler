## 2024-07-04 - Optimize BeautifulSoup tag serialization
**Learning:** Stringifying existing BeautifulSoup objects (e.g., `str(tag)`) inside loops or lambda functions incurs a severe serialization performance penalty, completely negating any regex or iteration speed advantages.
**Action:** Always use native bs4 methods and properties like `tag.get('src', '')` and `tag.text` instead of `str(tag)` when extracting or checking text and attributes from tags.
