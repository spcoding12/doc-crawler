## 2024-06-09 - [Optimize framework detection]
**Learning:** `.select()` has huge overhead in BeautifulSoup compared to `.find()`. Also, `str(tag)` invokes the full DOM serialization overhead whereas `tag.text` is extremely fast. Checking for multiple classes using `class_=['a', 'b']` is vastly superior.
**Action:** Replaced `.select()` based loops with `.find()` and class lists. Used `.text` instead of `str()`.
