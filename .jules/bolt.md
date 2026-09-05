## 2024-09-05 - BeautifulSoup parsing optimization
**Learning:** Using `.select()` in BeautifulSoup is significantly slower than using `.find()` or `.find_all()` with lists of classes (`class_=[...]`) and lambda attributes (`attrs={...}`), especially in heavy DOM structures. Also, `.text` is much faster than `str(tag)` for extracting text.
**Action:** When evaluating multiple candidate tags for presence, prefer `.find()` with combined class/attribute checks over looping through CSS selectors with `.select()`. Assign the result to a variable if both checking for existence and extracting data.
