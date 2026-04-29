## 2024-04-29 - Optimize BeautifulSoup traversal in detector
**Learning:** CSS selectors (.select) introduce significant overhead compared to native .find() and .find_all(), and multiple redundant .find() calls increase DOM traversal time.
**Action:** Use .find() with direct attribute lookups and pass lists to the class parameter to consolidate checks into a single-pass OR operation, drastically reducing parse time.
