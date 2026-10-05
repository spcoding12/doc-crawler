## 2024-10-05 - Multi-page crawler architecture performance pattern
**Learning:** In a multi-page crawler architecture (like this codebase), passing globally detected contexts (such as the framework name) down to page-level extractors (e.g., `extract_content`) prevents redundant and expensive DOM tree parsing (e.g., `BeautifulSoup(html, 'lxml')`) on every page.
**Action:** Always pass the known framework to `extract_content` to bypass redundant `detect_framework` execution.
