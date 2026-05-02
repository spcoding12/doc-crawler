## 2024-05-24 - Initial Profile
## 2024-05-24 - Avoid Redundant DOM Parsing
**Learning:** In a multi-page crawler, not passing a globally detected context (like the framework name) down to page-level extractors can cause redundant and expensive DOM tree parsing (`BeautifulSoup(html, 'lxml')`) on every single page.
**Action:** Always pass the detected context to downstream functions to bypass duplicate detection steps.
