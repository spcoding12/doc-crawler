## 2024-05-18 - BeautifulSoup DOM Traversal Optimization
**Learning:** Checking multiple classes at once in one pass via `soup.find(class_=['class1', 'class2'])` combined with direct attribute lookups instead of CSS selectors significantly avoids parsing overhead and allows short-circuiting DOM traversal. Using `soup.select` evaluates full CSS selectors against the entire DOM repeatedly.
**Action:** Always prefer native bs4 methods like `find` and `find_all` with attribute/class arrays over `select` in highly repetitive detection loops.
