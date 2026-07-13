## 2024-05-24 - Avoid str() serialization in BeautifulSoup
**Learning:** Using `str(tag)` in BeautifulSoup loops to search within a tag causes severe performance degradation due to full DOM serialization.
**Action:** Always use targeted `.get()` for attributes and `.text` for tag contents instead of `str()` when analyzing tags.
