## YYYY-MM-DD - Framework Detection Bottlenecks
**Learning:** Checking for substrings using `str(tag)` on BeautifulSoup tags incurs massive serialization overhead. Additionally, using multiple `.select()` calls with lambdas is significantly slower than consolidating checks with `.find(class_=[...])`. Using `.string` on scripts is brittle if child nodes exist; `.text` is safer and faster.
**Action:** Replace `str(tag)` with direct attribute/`.text` lookups and replace CSS `.select()` with consolidated `.find()` or `.find_all()` passing a list to the `class_` argument.
