## 2024-05-14 - Redundant Framework Detection Bottleneck
**Learning:** In a multi-page crawler architecture, redundant DOM parsing and querying during page-level framework detection (`detect_framework(html)`) introduces a major performance bottleneck, as the framework identity is typically homogenous across the entire site.
**Action:** Pass globally detected contexts (such as the framework name determined at the entry point) down to page-level extractors (`extract_content(..., framework=adapter.name)`) to bypass redundant per-page detection and expensive `BeautifulSoup` tree construction.
