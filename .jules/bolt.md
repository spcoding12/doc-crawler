## 2024-07-18 - Pass global context to page-level extraction
**Learning:** In a multi-page crawler architecture, redundant DOM tree parsing (like `BeautifulSoup(html, 'lxml')`) can occur on every page if the globally detected context (such as the framework name) is not passed down to page-level extractors.
**Action:** Always pass globally detected framework names to page-level extraction functions (e.g., `extract_content(..., framework=adapter.name)`) to bypass redundant parsing overhead and improve overall extraction speed.
