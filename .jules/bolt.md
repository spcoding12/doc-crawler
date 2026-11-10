## YYYY-MM-DD - [Avoid CSS selector overhead in BeautifulSoup]
**Learning:** Using `.select()` or `.select_one()` with CSS selectors in BeautifulSoup incurs significant parsing overhead compared to native tree traversal methods. Also, `str(tag)` has massive serialization overhead.
**Action:** Always use native bs4 methods like `.find()` or `.find_all()` with direct attribute lookups or list of classes to maximize DOM traversal performance. Also avoid `.string` and use `.text` for robustness against None values.
