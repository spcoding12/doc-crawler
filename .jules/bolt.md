## 2024-05-20 - BeautifulSoup CSS Selector Parsing Overhead
**Learning:** In heavily nested HTML DOMs with repetitive tags (like `meta[name='generator']` injected multiple times), using `BeautifulSoup.select()` with CSS selectors is significantly slower than using native DOM lookups via `.find()` or `.find_all()`. Pre-compiling the CSS selector doesn't completely avoid the CSS parsing overhead.
**Action:** Always prefer native DOM methods (`.find`, `.find_all`) with specific attributes over CSS selectors (`.select`) when performance is critical. Consolidate multiple independent class checks into a single pass using lists (`soup.find(class_=['cls1', 'cls2'])`).

## 2024-05-20 - HTML2Text Thread Safety
**Learning:** `html2text.HTML2Text` is stateful (inherits from standard `HTMLParser`). Do NOT attempt to optimize performance by making it a global/module-level instance. Reusing a single instance across function calls is thread-unsafe and causes critical concurrency bugs.
**Action:** Instantiate `html2text.HTML2Text` per function call. Do not use global instances for stateful parsers.
