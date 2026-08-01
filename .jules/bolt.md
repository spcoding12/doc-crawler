## 2024-08-01 - [Avoid Redundant Framework Detection]
**Learning:** Passing globally detected contexts (like framework name) down to page-level extractors prevents redundant DOM tree parsing (e.g., BeautifulSoup) on every page.
**Action:** When a crawler architecture evaluates pages using a detected global context, pass the context explicitly to page processing functions to skip redundant detections.
