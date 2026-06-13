## 2024-06-13 - Performance pattern for HTML parsing
**Learning:** In a multi-page crawler architecture, `extract_content` currently re-runs `detect_framework(html)` for EVERY page unless the framework is explicitly passed. This adds significant redundant BS4 parsing overhead (~1.4s per 100 pages, just for detection).
**Action:** Since we detect the framework globally at the start of the crawl (in `src/main.py`), we should pass `framework.name` (or `adapter.name`) down to `extract_content` in the page loop to skip the redundant framework detection per-page.
