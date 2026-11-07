## 2023-11-20 - [Performance Anti-pattern: stringifying BeautifulSoup tags]
**Learning:** Checking contents of BeautifulSoup tags (like `<script>`) by stringifying them (`str(tag)`) has a severe performance penalty because it forces a full serialization of the DOM element.
**Action:** Use native BeautifulSoup properties and methods like `tag.text`, `tag.get('src', '')`, or `tag.get('id', '')` to check for specific strings instead of converting the tag to a string first. This yields an order-of-magnitude speedup (~9x).
