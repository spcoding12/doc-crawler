## 2024-05-26 - Optimized DOM tree traversal in framework detector

**Learning:** When detecting documentation frameworks using BeautifulSoup, calling `.select()` and iterating through the results, or multiple `.select()` calls with lambda functions, adds significant parsing overhead by repeatedly evaluating CSS selectors against the DOM tree.

**Action:** Consolidate multiple independent class checks into a single-pass operation by passing a list to the class parameter (e.g., `soup.find(class_=['class1', 'class2', ...])`) or by looking up the `meta` tags directly. This acts as an optimized OR check that traverses the DOM tree exactly once, reducing overhead compared to checking selectors one by one. Use `.text` instead of `str(tag)` when extracting text from tags to avoid serialization overhead.
