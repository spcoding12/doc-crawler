## YYYY-MM-DD - Avoid str() serialization on BeautifulSoup tags
**Learning:** Using `str(tag)` to check for substrings within a BeautifulSoup element incurs a severe performance penalty because it serializes the entire DOM tree of that tag.
**Action:** Instead of `str(tag)`, explicitly check relevant attributes like `.get('src', '')` and `.get('id', '')` alongside `.text` for a significant speedup when matching content.
