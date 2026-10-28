## 2024-10-28 - Optimizing BeautifulSoup Traversals
**Learning:** Replacing iterative .select() with a consolidated .find(class_=[...]) operation bypasses CSS parsing overhead and executes significantly faster in DOM traversals.
**Action:** Always favor native direct attribute lookups like .find over .select when parsing HTML.
