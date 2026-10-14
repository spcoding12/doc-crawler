## 2024-05-24 - Optimizing BeautifulSoup script tag evaluation
**Learning:** `str(tag)` incurs a significant serialization penalty when iterating over tags like `<script>`. Checking `tag.get('src', '')` and `tag.string or ''` or `tag.text` separately is ~10x faster than checking `str(tag)`.
**Action:** When searching for patterns in tags, always avoid stringifying the entire tag object; prefer checking specific properties (`.text`, `.string`, `.get()`) instead.
