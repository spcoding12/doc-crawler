## 2024-05-31 - BeautifulSoup Performance Anti-patterns
**Learning:** Using `soup.select()` with CSS selectors and `str(tag)` on elements with many children creates a severe performance bottleneck (17.6s vs 5.8s on large documents without target framework).
**Action:** Use `soup.find()`/`soup.find_all()` with direct attribute/class lookups and `tag.text` instead.
