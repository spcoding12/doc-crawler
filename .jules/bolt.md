
## 2024-07-10 - Optimize Framework Detection with class lists
**Learning:** Using `soup.select(selector)` and looping over multiple indicators forces BeautifulSoup to parse CSS selectors and traverse the DOM tree multiple times. In the worst case, this is extremely slow. Using `.find()` and passing a list of classes (`class_=['a', 'b']`) allows BeautifulSoup to act as an optimized OR check during a single traversal. Avoid `str(tag)` because it incurs a huge serialization performance penalty compared to `tag.text` which safely extracts child strings.
**Action:** Replace CSS selector lists and multiple iteration passes with single `.find()` operations using lists for `class_`. Replace `.string` and `str(tag)` with `.text` or `.get('src', '')` to avoid serialization overhead.
