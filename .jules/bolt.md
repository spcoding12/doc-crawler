## 2025-05-18 - Avoid str(tag) in BeautifulSoup
**Learning:** Using `str(tag)` for stringification of a BeautifulSoup tag incurs a severe serialization performance penalty, completely negating regex/string match speed advantages. It is over 2.5x slower than checking `.text` and attributes manually, and up to 100x slower for large tags.
**Action:** Replace `str(tag)` with `.text` and explicit attribute lookups (e.g., `tag.get('src', '')`) when checking tags like `<script>`.
## 2025-05-18 - Avoid CSS Selectors for Existence Checks
**Learning:** Using `soup.select()` or `soup.select_one()` with CSS selectors is significantly slower (approx 2x) than using `soup.find_all()` or `soup.find()` with direct attributes or lambda functions for existence checks or single tag lookups, due to the overhead of the cssselect library parsing the CSS string.
**Action:** Replace `soup.select()` and `soup.select_one()` with equivalent `soup.find()` or `soup.find_all()` calls, using lambda functions in `attrs` or class arrays when complex logic is required.
