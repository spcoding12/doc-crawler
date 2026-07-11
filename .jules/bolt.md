## 2024-05-24 - Prevent redundant framework detection parsing
**Learning:** In a multi-page crawler architecture, if a global context (like the framework) is already detected once, it should be passed down to page-level extractors. Failing to do so causes `extract_content` to redundantly reconstruct the DOM tree (e.g., `BeautifulSoup(html, 'lxml')`) on every single page just to re-identify the framework.
**Action:** Always pass globally detected framework contexts (`adapter.name`) to page-level extractors (`extract_content(..., framework=adapter.name)`) to bypass redundant parsing overhead.
