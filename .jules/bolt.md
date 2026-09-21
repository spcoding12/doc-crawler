## 2025-02-20 - Multi-page Crawler Context Passing
**Learning:** Extracting framework-specific content on a multi-page crawler can incur redundant DOM parsing (e.g., `BeautifulSoup(html, 'lxml')`) if framework detection is re-run per page.
**Action:** Pass globally detected contexts (like framework name) down to page-level extractors to bypass repetitive detection and significantly improve overall extraction speed.
