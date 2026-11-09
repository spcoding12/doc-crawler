## 2025-02-25 - BeautifulSoup Serialization Bottleneck
**Learning:** Stringifying a BeautifulSoup tag object (e.g., `str(tag)`) for text searching inside loops (like searching for framework indicators in `<script>` tags) incurs a massive serialization penalty. In `detect_docusaurus`, replacing `str(tag)` with `.text.lower()` and `.get('src', '').lower()` reduced execution time from ~0.29s to ~0.03s on a large HTML document with 1000 scripts.
**Action:** Never use `str(tag)` on DOM elements just to check their contents or properties. Extract `.text` and explicit attributes (like `.get('src', '')`) instead, which bypasses the expensive serialization to string.

## 2025-02-25 - Docusaurus Script Checking Edge Case
**Learning:** When replacing `str(tag)` with `.text` and `.get('src')`, it's critical to capture *both* the script content (via `.text`) and the script source URL (via `.get('src')`) to correctly identify Docusaurus usage, as Docusaurus could be present in inline script contents or external script filenames. Docusaurus sites often mount their initial state using a script tag with `id="__docusaurus"`.
**Action:** When extracting data from `<script>` tags without `str()`, explicitly check `.text`, `.get('src', '')` and `.get('id', '')`.
