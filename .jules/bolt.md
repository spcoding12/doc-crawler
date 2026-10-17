## 2024-05-14 - Redundant DOM parsing in multi-page crawlers
**Learning:** In a multi-page crawler architecture, failing to pass globally detected context (like the framework name) down to page-level extractors causes redundant and expensive DOM tree parsing (`BeautifulSoup(html, 'lxml')`) on every single page.
**Action:** Always pass known global state/context downwards to bypass redundant detection logic in loops.
