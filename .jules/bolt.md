## 2024-06-03 - [BeautifulSoup Performance: find vs select]
**Learning:** In BeautifulSoup, using `.select()` with CSS selectors is significantly slower than using `.find()` or `.find_all()` with direct class or attribute lookups. Furthermore, passing a list of classes to `.find(class_=[...])` acts as a highly optimized OR check, traversing the DOM tree exactly once instead of multiple times for each selector.
**Action:** Always prefer `.find()` and `.find_all()` over `.select()` when optimizing BeautifulSoup parsing logic.
