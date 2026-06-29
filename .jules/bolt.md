
## 2024-06-29 - Cache Framework Detection During Page Extraction
**Learning:** In a multi-page crawler architecture, the `detect_framework` function re-parses the DOM tree and evaluates multiple frameworks for *every single page* crawled, even though the framework was already determined globally for the site at the start of the process.
**Action:** Always pass the globally detected context (like `framework=adapter.name`) down to page-level extraction functions (`extract_content`) to bypass redundant framework detection logic and save expensive `BeautifulSoup(html, 'lxml')` operations per page.
