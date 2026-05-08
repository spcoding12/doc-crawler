## 2025-02-27 - Prevent Redundant DOM Parsing via Context Propagation
**Learning:** In a multi-page crawler, failing to pass globally detected contexts (like the framework name) to page-level extractors results in redundant and expensive DOM tree parsing (e.g., `BeautifulSoup(html, 'lxml')`) on every single page during the detection phase.
**Action:** Pass known contexts (like `framework=adapter.name`) downwards to avoid duplicate work.
