## 2024-04-07 - BeautifulSoup select() vs find() performance
**Learning:** Using `soup.select()` with CSS selectors inside loops is a major anti-pattern in this codebase's framework detectors. Benchmarks showed `soup.select()` is 2-3x slower than native `soup.find()` and `soup.find_all()`.
**Action:** Always prefer `soup.find()` and `soup.find_all()` over `soup.select()` for simple tag, class, or attribute queries. Consolidate multiple independent class checks into a single-pass operation by passing a list to the class parameter (e.g., `soup.find(class_=['class1', 'class2'])`).
