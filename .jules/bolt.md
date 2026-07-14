## 2024-07-14 - Optimize BeautifulSoup Script Tag Parsing
**Learning:** Using `str(tag)` on BeautifulSoup tags triggers a full, expensive serialization of the entire DOM node and its children, making it ~10-100x slower for large tags (like scripts). `tag.string` fails if a tag has multiple children. `tag.text` safely extracts text content without full serialization overhead.
**Action:** Always prefer `tag.text` and explicit attribute checks (like `tag.get('src', '')`) instead of `str(tag)` when looking for substring matches inside HTML tags, especially for framework detection scripts.
