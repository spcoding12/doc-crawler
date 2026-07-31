## 2024-05-24 - Avoid stringifying BeautifulSoup tags
**Learning:** Stringifying an entire tag inside a search/filter function using `str(tag)` on a BeautifulSoup tag (like `<script>`) causes severe serialization performance issues due to traversing the entire tag's DOM structure.
**Action:** When filtering tags based on contents or attributes, always use `.get()` to access attributes like `src`, and `.text` to get the inner text. Avoid `str(tag)`.
