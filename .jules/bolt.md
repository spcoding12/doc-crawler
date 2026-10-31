## $(date +%Y-%m-%d) - BeautifulSoup Selector Overhead
**Learning:** Using `soup.select()` and lambda checks combined with `str(tag)` in large DOMs incurs a severe overhead in BeautifulSoup compared to direct native methods.
**Action:** Use `.find()` or `.find_all()` with direct attribute lookups, avoid stringifying full tags when extracting text, and consolidate multiple class checks via a list argument (e.g., `soup.find(class_=['class1', 'class2'])`).
