## 2026-11-03 - BeautifulSoup Optimization
**Learning:** Serializing BS4 tags with `str(tag)` or using `.select()` incurs severe performance penalties compared to native `.find()` or `.find_all()` traversing the DOM tree. Consolidating checks with list parameters (e.g. `class_=['c1', 'c2']`) significantly speeds up detection.
**Action:** Avoid `str(tag)` for regex or basic text matching. Prefer passing a list to the `class_` argument instead of sequential checking. Replace `.select()` with `.find()` attribute checks.
