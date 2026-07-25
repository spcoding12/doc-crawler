## 2024-07-25 - Avoid CSS Selectors for specific DOM lookups
**Learning:** Using `soup.select()` in BeautifulSoup with CSS selectors is significantly slower than using `.find()` or `.find_all()` with specific attributes, especially for repeated existence checks like in framework detection. Furthermore, looping over multiple tags manually can be reduced by using `class_=['class1', 'class2']`.
**Action:** Replace `soup.select` loops with optimized `soup.find` or `soup.find_all` where applicable in `src/detector.py` to boost performance during framework detection.
