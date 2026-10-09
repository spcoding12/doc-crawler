## 2024-03-24 - [Avoid Redundant Framework Detection]
**Learning:** In a multi-page crawler architecture, globally detected contexts (such as the framework name) should be passed down to page-level extractors to prevent redundant and expensive DOM tree parsing (`BeautifulSoup(html, 'lxml')`) and repeated framework detection for every page.
**Action:** Always identify globally determined state and pass it down to lower-level functions in loops rather than re-computing it.
