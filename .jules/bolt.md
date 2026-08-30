## 2024-05-18 - Passing context to avoid redundant parsing
**Learning:** In a multi-page crawler architecture, failing to pass globally detected context (like the framework name) down to page-level functions causes redundant and expensive DOM tree parsing on every page.
**Action:** Pass the globally detected context (`framework=adapter.name`) to page-level extractors (`extract_content`) to prevent redundant BeautifulSoup parsing overhead.
