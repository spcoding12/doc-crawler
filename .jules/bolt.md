## 2024-09-17 - BeautifulSoup Performance Optimization for Framework Detection
**Learning:** Using `soup.select(selector)` and `str(tag)` inside loops (especially for large DOM trees) is extremely slow compared to native `soup.find()` methods and `tag.text`. In `detector.py`, checking classes via `.select()` scales poorly with DOM size.
**Action:** Replace `soup.select()` with targeted `soup.find(class_=[...])` which does a single pass over the DOM and is much faster. Also use `script.text` instead of `str(script)`.
