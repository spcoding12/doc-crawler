## 2024-06-28 - Optimize BeautifulSoup Selectors
**Learning:** `soup.select()` parsing overhead in tight loops is significant. The previous pattern of looping over an array of selectors caused unnecessary overhead.
**Action:** Replace `soup.select()` with native `.find()` and `.find_all(class_=['a', 'b'])` which naturally handles list matching much faster without needing CSS string parsing.
