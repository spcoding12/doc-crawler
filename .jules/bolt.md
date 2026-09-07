## 2024-05-24 - Avoid `str(tag)` when inspecting tag attributes or inner text
**Learning:** In `BeautifulSoup`, using `str(tag)` serializes the entire DOM subtree within the tag to a string. This can cause massive memory and CPU overhead if a `<script>` tag contains huge webpack bundles.
**Action:** When extracting or checking text/attributes, always use `tag.text` and `tag.get('src')` instead of `str(tag)`.
