## 2024-05-24 - Optimize BeautifulSoup HTML parsing in framework detection
**Learning:** Using CSS selectors (`.select()`) and serializing full HTML elements to strings (`str(tag)`) inside loops incurs a massive performance overhead during BeautifulSoup parsing, especially on large HTML documents.
**Action:** Consolidate class checks into single `.find()` passes using lists (`class_=['a', 'b']`), replace expensive string serialization with `.text` and direct attribute access (`.get('src')`), and sequence data extraction operations before early-return existential checks.
