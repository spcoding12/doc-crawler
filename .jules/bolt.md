## 2024-04-21 - [Optimized DOM parsing in src/detector.py]
**Learning:** `BeautifulSoup.select()` using CSS selectors with multiple repetitive checks is very slow in this specific codebase context, as it initiates separate parsing traversals.
**Action:** Replace `.select()` with `.find()` and `.find_all()`. Use consolidated checks like `.find(class_=['class1', 'class2', ...])` to perform an OR check in a single DOM pass. Also replaced `script.string` with `script.text` for safety against mixed children text return values.
