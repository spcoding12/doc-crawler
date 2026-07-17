## 2024-05-18 - Avoid str(tag) in BeautifulSoup
**Learning:** Using `str(tag)` on BeautifulSoup tags, especially large tags like `<script>`, incurs a significant performance penalty (nearly 3x slower in our benchmarks) due to the overhead of serializing the DOM tree back into a string.
**Action:** Replace `str(tag)` with `tag.get('src', '').lower() + tag.text.lower()` or similar direct property accesses when checking for substrings in tags.
