## 2024-09-12 - BeautifulSoup tag serialization performance penalty
**Learning:** Using `str(tag)` on a BeautifulSoup element incurs a massive performance penalty because it serializes the entire tag and its contents. For `<script>` tags, this can be extremely slow.
**Action:** When extracting text or searching for keywords within a tag, use `.text` (which safely handles children without full serialization) and `.get('src', '')` for attributes, instead of `str(tag)`.
