
## 2024-05-30 - [BeautifulSoup DOM Query Bottlenecks in Framework Detectors]
**Learning:** Using CSS selectors (`soup.select()`) in a loop over large HTML structures is significantly slower (by over 5x) than native targeted queries (`soup.find` or `soup.find_all` with `attrs` and lists for `class_`). Additionally, using `str(tag)` to check for patterns inside `<script>` elements serializes the entire DOM node back into a string, incurring a huge overhead.
**Action:** Always replace `.select()` with `.find()` or `.find_all()` using specific attribute/class filters when iterating over large DOMs. When checking script contents, use `.text` and explicitly check the `src` attribute (e.g. `tag.get('src')`) instead of stringifying the entire tag.
