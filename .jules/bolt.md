## 2024-05-18 - Pass globally detected framework to extract_content
**Learning:** In the multi-page crawler architecture, passing globally detected contexts (such as the framework name) down to page-level extractors (e.g., `extract_content`) prevents redundant and expensive DOM tree parsing (e.g., `BeautifulSoup(html, 'lxml')`) on every page.
**Action:** When extracting content in `src/main.py`, pass the `framework.name` that was already detected in the initial site scan to the `extract_content` function to avoid redundant framework detection overhead for each page.
