## 2024-05-24 - Optimizing BeautifulSoup DOM Selection
**Learning:** Evaluating CSS selectors via `soup.select()` within loops introduces heavy performance overhead. Native `.find()` and `.find_all()` with direct attribute/class lookups are significantly faster.
**Action:** Always prefer `.find()`/`.find_all()` over `.select()` for performance critical DOM extractions, and consolidate class checking into a single `.find(class_=[...])` call where possible.
