## 2024-05-18 - Avoid str(tag) serialization in BeautifulSoup
**Learning:** Stringifying a parsed BeautifulSoup object using `str(tag)` or `str(soup)` invokes full DOM tree serialization. In `src/detector.py`, checking `script` tags using `'docusaurus' in str(tag)` causes severe performance degradation on pages with many script tags (e.g. SPAs), taking ~2x-10x longer than directly checking attributes or `.text`.
**Action:** When extracting data or doing simple text checks on tags, directly check `.get('src', '')` and `.text` instead of casting the entire tag to a string.
