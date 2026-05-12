## 2025-05-24 - Bypass redundant DOM parsing by passing known framework context
**Learning:** In a multi-page crawler architecture, pass globally detected contexts (such as the framework name) down to page-level extractors (e.g., extract_content) to prevent redundant and expensive DOM tree parsing (e.g., BeautifulSoup(html, 'lxml')) on every page.
**Action:** Always check if a context is already known at the global/scheduler level and can be passed down to avoid re-computing it.
