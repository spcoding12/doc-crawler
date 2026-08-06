## 2023-10-27 - Optimize BeautifulSoup framework detection
**Learning:** Using `.select()` for attribute lookups in BeautifulSoup is significantly slower than `.find()` or `.find_all()`. Additionally, converting a tag to a string using `str(tag)` incurs a massive performance penalty compared to accessing `tag.text`.
**Action:** Use `.find()` or `.find_all()` with attribute dictionaries instead of `.select()` and avoid using `str(tag)` when inspecting content.
