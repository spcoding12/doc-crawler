## 2024-05-07 - Optimization opportunity: BeautifulSoup find/find_all with attributes instead of select
**Learning:** `BeautifulSoup.select()` uses CSS selectors which is slower than using `.find()` or `.find_all()` with attributes because CSS selector parsing has more overhead.
**Action:** Replace `.select()` with `.find()`/`.find_all()` where appropriate for better performance.
## 2024-05-07 - Pass globally detected context to page-level extractors
**Learning:** In a multi-page crawler architecture, redundant DOM parsing (e.g., `BeautifulSoup(html, "lxml")`) on every page to detect the framework causes significant performance overhead.
**Action:** Pass globally detected contexts (such as the framework name) down to page-level extractors to prevent redundant parsing.
