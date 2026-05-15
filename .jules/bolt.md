## 2024-05-15 - Pass global framework context to avoid redundant parsing
**Learning:** In a multi-page crawler architecture, if a framework (e.g. Docusaurus) is identified globally during site discovery, passing this context down to individual page extractors avoids redundant and expensive DOM parsing (e.g. `BeautifulSoup(html, 'lxml')` inside the `detect_framework` function) for every single page.
**Action:** Always identify contextual dependencies early and pass them down as arguments rather than re-computing them, especially in tight loops or large collections processing.
