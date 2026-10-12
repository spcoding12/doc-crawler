## 2025-05-18 - BeautifulSoup str(tag) serialization overhead
**Learning:** Stringifying large `BeautifulSoup` elements (e.g., `str(tag)` on a `<script>` tag containing thousands of lines of JS) completely blocks execution and causes an extreme performance penalty (taking multiple seconds), neutralizing any other optimizations.
**Action:** Always use native bs4 methods and properties like `.text` or direct attribute lookups (`.get('src')`) instead of `str(tag)` when inspecting element content.
