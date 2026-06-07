## 2025-06-07 - Optimize BeautifulSoup DOM Traversal
**Learning:** Using `soup.select()` for CSS selector arrays is significantly slower than using `soup.find(class_=['cls1', 'cls2'])` which acts as a single-pass OR check traversing the DOM tree exactly once. Additionally, `str(tag)` incurs massive serialization penalty compared to native `tag.text` and `tag.get('attr')`.
**Action:** Always prefer `.find()` with `class_=` array over `.select()` loops. Never use `str(tag)` for string matching inside loops.
