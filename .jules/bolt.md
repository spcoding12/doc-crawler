## 2024-05-21 - BeautifulSoup DOM Traversal Optimization
**Learning:** In BeautifulSoup, using `soup.find(class_=['class1', 'class2'])` combined with direct attribute lookups (`attrs`) and `.text` extraction is significantly faster (~4x) than using `soup.select()` with CSS selectors, `str(tag)`, or multiple independent `soup.find()` calls.
**Action:** Default to using `.find_all` and `.find` with lists of classes or specific attributes instead of CSS selectors when scanning DOM trees for specific characteristics. Use `.text` instead of `str()` or `.string` for tag content matching.
