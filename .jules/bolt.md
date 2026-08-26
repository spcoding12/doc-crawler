## 2024-05-24 - Optimizing Framework Detection in BeautifulSoup

**Learning:** When checking for class existence to detect a framework, `soup.select(selector)` and checking `True` is slow. Using `soup.find_all(class_=[...])` or `soup.find(class_=[...])` is significantly faster as it evaluates multiple class matches in a single pass of the DOM tree. Furthermore, stringifying large BeautifulSoup tags (`str(tag)`) to check for a substring (like 'docusaurus') incurs huge serialization overhead. Checking `tag.text.lower()` and specific attributes like `tag.get('src', '')` avoids this serialization penalty and reduces execution time.

**Action:** Refactor `src/detector.py` to use `soup.find` or `soup.find_all` with direct attribute lookups and lists of classes instead of `soup.select`. Replace `str(tag)` checks with `.text` and `.get(...)` attribute checks, being sure to test both text and source for tags like `<script>`.
