## YYYY-MM-DD - [BeautifulSoup Serialization Bottleneck]
**Learning:** Stringifying a BeautifulSoup tag using `str(tag)` incurs a severe serialization performance penalty, especially on large HTML documents.
**Action:** Always use `.text` and explicit attribute lookups (e.g., `tag.get('src', '')`) instead of `str(tag)` when searching for substrings in a tag, as it is significantly faster.
