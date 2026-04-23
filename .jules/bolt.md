
## 2024-04-23 - Avoid redundant framework detection during crawling
**Learning:** In a multi-page crawler architecture, calling a framework detection function (which parses the entire DOM tree) on every page during the extraction phase causes severe performance degradation due to redundant DOM parsing overhead (31% slower).
**Action:** Detect the framework once during the initialization phase and pass the detected framework context down to the extractor for all subsequent pages to bypass repeated DOM parsing.
