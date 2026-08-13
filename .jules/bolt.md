## 2024-05-18 - Avoid str(tag) in BeautifulSoup
**Learning:** Stringifying a BeautifulSoup tag using `str(tag)` incurs a significant serialization penalty, slowing down DOM parsing significantly compared to using `tag.get()` and `tag.text` to inspect the contents and attributes of the tag.
**Action:** Replace instances of `str(tag)` with `.text` and `.get('src', '')` (or other attributes) when iterating over script tags or similar elements in BeautifulSoup.
