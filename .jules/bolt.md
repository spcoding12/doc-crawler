## 2024-05-15 - Avoid redundant DOM parsing for global context
**Learning:** In a multi-page crawler, passing globally detected contexts (like the documentation framework name) down to page-level extractors prevents redundant and expensive DOM tree parsing (e.g., `BeautifulSoup(html, 'lxml')`) on every single page. The `detect_framework` function was taking significant time because it instantiates a full BeautifulSoup object to test selectors.
**Action:** Always check if a globally determined value can be passed down into loops or per-page handlers instead of recalculating it from scratch.
