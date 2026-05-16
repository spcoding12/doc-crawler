## 2024-05-16 - Pass Global Framework Context to Page Extractors
**Learning:** In multi-page crawling architectures, failing to pass globally detected context (like the framework name) down to page-level extraction functions causes significant performance bottlenecks by forcing redundant and expensive DOM tree parsing (e.g., `BeautifulSoup(html, 'lxml')`) and detection logic on every single page.
**Action:** Always ensure that globally identified or computed properties are passed as arguments to down-stream processing functions to prevent redundant work.
