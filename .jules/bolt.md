## 2025-05-18 - Avoid str(tag) in BeautifulSoup
**Learning:** Stringifying a BeautifulSoup tag using `str(tag)` is very expensive, especially if the tag contains a lot of text (like `<script>` tags). Using `tag.get('src', '')` and `tag.text` is about 4x faster.
**Action:** Replace `str(tag)` with attribute extraction (e.g. `tag.get('src', '')`) or `tag.text` for text nodes when searching for strings within a tag.
