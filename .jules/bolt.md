## 2024-05-18 - Avoid str(tag) in BeautifulSoup
**Learning:** Using `str(tag)` on BeautifulSoup tags forces a full serialization of the DOM node and its children into an HTML string. This is severely slow (up to 10x slower) compared to extracting the `.text` content or accessing attributes directly (e.g. `tag.get('src')`).
**Action:** When checking script contents or attributes, use `tag.text` for inner text and `tag.get('src')` for attributes instead of `str(tag)`.
