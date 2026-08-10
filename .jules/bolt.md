## 2026-08-10 - Avoid redundant framework detection per page
**Learning:** In a multi-page crawler architecture, globally detected contexts (like framework name) should be passed to page-level extractors to prevent redundant and expensive DOM tree parsing (e.g., BeautifulSoup) on every page.
**Action:** Pass the globally detected framework name to `extract_content`.
