## 2024-05-24 - Passing Global Context to Page Extractors
**Learning:** In a multi-page crawler, passing globally detected contexts (such as the framework name) down to page-level extractors prevents redundant and expensive DOM tree parsing (e.g., `BeautifulSoup(html, 'lxml')`) on every page.
**Action:** Always pass the already-determined framework name to `extract_content` to bypass the redundant `detect_framework` execution.
