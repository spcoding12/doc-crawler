
## 2024-05-20 - BeautifulSoup Selector Performance Anti-Pattern
**Learning:** Found a critical bottleneck in `src/detector.py` where BeautifulSoup's `.select()` was used extensively to detect framework features. `soup.select('.class')` parses a CSS selector and returns all matching elements, whereas `soup.find(class_='class')` directly traverses the internal tree and returns immediately upon the first match. This O(N) CSS parsing operation combined with a loop made the `detect_*` functions 60-98% slower than direct node traversal.
**Action:** When working with BeautifulSoup for simple tag or class lookups, strictly use `.find()` and `.find_all()` with keyword arguments (like `class_` or `id`) or attribute dictionaries (`{'name': 'generator'}`) instead of using `.select()`.
