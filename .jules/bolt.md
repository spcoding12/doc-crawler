## 2024-05-30 - Replace slow BeautifulSoup select with find
**Learning:** BeautifulSoup's `.select()` CSS selector calls are incredibly slow compared to native `.find()` and `.find_all()` methods. In `src/detector.py`, replacing these calls reduced framework detection time by ~50% (from 43s to 21s in a 1000-iteration benchmark).
**Action:** When working with BeautifulSoup, prioritize direct tag, class, or attribute lookups using `find` and `find_all` over CSS selectors (`select`), especially inside loops or high-frequency code paths.
