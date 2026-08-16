
## 2025-08-16 - Optimize BeautifulSoup DOM querying
**Learning:** Using CSS selectors (`.select`) inside `for` loops against BeautifulSoup objects incurs major parsing overhead. Furthermore, executing multiple `.find` calls on separate classes causes redundant DOM tree traversals. Serializing tags using `str(tag)` just to regex or check inclusion is incredibly slow compared to using the native `.text` property.
**Action:** Combine independent class checks into a single pass using `soup.find(class_=['class1', 'class2'])`. Prioritize specific direct-match extractions (like meta tags) over generic slow matching. Replace `.select` with direct `.find` or `.find_all` where applicable. Replace `str(tag)` serialization with `.text`.
