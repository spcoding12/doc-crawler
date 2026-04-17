## 2024-04-17 - BeautifulSoup String vs Text Saftey
**Learning:** When optimizing BeautifulSoup queries, replacing `.string` with `.text` on `<script>` tags is strictly safer because `.string` returns `None` if the tag contains multiple child nodes (e.g. an HTML comment wrapping the JS), whereas `.text` cleanly extracts all text content regardless of child structure.
**Action:** Always prefer `.text` over `.string` when extracting text content from DOM nodes unless you explicitly want to fail on multi-node tags.
