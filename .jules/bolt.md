## 2024-05-30 - Passing Framework Context Down to Extract Content
**Learning:** In a multi-page crawler architecture, globally detected contexts (such as the framework name) should be passed down to page-level extractors (e.g., `extract_content`) to prevent redundant and expensive DOM tree parsing (`BeautifulSoup(html, 'lxml')`) on every page.
**Action:** When extracting content across multiple pages within the same site where the framework is already known, pass the `framework` name into the `extract_content` function explicitly.
