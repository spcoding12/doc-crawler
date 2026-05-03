## 2024-05-24 - HTML Parsing Redundancy in Crawler Loop
**Learning:** In a multi-page crawler architecture (like this codebase), detecting the framework on every page involves redundant and expensive DOM tree parsing (`BeautifulSoup(html, 'lxml')`).
**Action:** Pass globally detected contexts (such as the framework name) down to page-level extractors (e.g., `extract_content`) to prevent redundant parsing and improve overall scraping throughput.
