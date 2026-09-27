## 2024-05-18 - BeautifulSoup DOM Traversal Optimization
**Learning:** Using `.select()` inside loops for DOM traversal incurs a significant parsing and execution overhead, and stringifying large DOM trees `str(tag)` takes a heavy performance penalty.
**Action:** Use native BeautifulSoup methods like `.find()` or `.find_all()` with lists of classes (`class_=['a', 'b']`), check element `.text`, or extract specific attributes (`.get()`) instead of serializing the entire tree or using `.select()`.
