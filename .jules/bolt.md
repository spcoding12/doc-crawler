
## YYYY-MM-DD - BeautifulSoup DOM Traversal Bottlenecks
**Learning:** Using `str(tag)` to evaluate entire DOM subtrees (especially for `<script>` tags that can contain large payloads) incurs severe stringification overhead in `BeautifulSoup`. Combined with repeated `.select()` calls over the same parsed HTML, this causes significant performance degradation.
**Action:** Replace `str(tag)` with `.text` and targeted attribute checks. Replace `.select()` sequences with single-pass `.find()` or `.find_all()` using `class_=['class1', 'class2']` lists to short-circuit framework checks.
