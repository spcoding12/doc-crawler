
## 2024-05-18 - [Performance] BeautifulSoup .find_all() vs .select()
**Learning:** In BeautifulSoup, using CSS selectors with `.select()` is significantly slower than using `.find_all()` or `.find()` with direct attribute/class matching. CSS selectors incur substantial parsing overhead.
**Action:** When extracting or verifying indicators (e.g., detecting framework structures), always prefer using `.find_all()` or `.find()` over `.select()` to avoid the performance penalty of CSS parsing.
