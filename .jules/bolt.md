## 2024-04-27 - BeautifulSoup CSS Selector Overhead
**Learning:** Using `.select()` for CSS selectors like `.classname` or iterating over multiple `soup.select()` calls adds significant overhead due to selector AST parsing and multiple DOM traversals. Passing a list of classes to `soup.find(class_=['class1', 'class2'])` consolidates these into a single tree traversal.
**Action:** Replace `soup.select()` with `soup.find()` or `soup.find_all()` using direct attribute/class lookups when performance is critical.
