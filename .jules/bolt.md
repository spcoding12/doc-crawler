## 2024-03-20 - BeautifulSoup Tag Serialization Performance
**Learning:** Using `str(tag)` on BeautifulSoup tags within a loop to search for text incurs a significant serialization penalty (creating a full string representation of the DOM node and its children).
**Action:** Replace `str(tag)` with `tag.get('src', '')` and `tag.text` for targeted text extraction and attribute checking. This is especially impactful in loops over many elements, like script tags during framework detection.
