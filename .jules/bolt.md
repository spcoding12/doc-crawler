
## 2024-04-10 - [Optimization: BeautifulSoup find_all vs select]
**Learning:** For testing specific classes or elements the `.find()`/`.find_all()` methods with multiple class lookups via array `class_=['class1', 'class2']` are significantly faster (~2.5x in our benchmark) than calling `.select()` multiple times with CSS selectors. This is due to Python's BeautifulSoup single-pass internal optimizations compared to the more expensive CSS selector compilation engine used by `.select()`.
**Action:** Always prefer `.find()`/`.find_all()` over `.select()` when simply traversing attributes, classes, or IDs, and utilize arrays within `class_` or `attrs` to perform single-pass evaluations instead of multiple successive `.select()` loops.
