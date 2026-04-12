
## 2026-04-12 - [BeautifulSoup Performance: find vs select]
**Learning:** Consolidating multiple CSS selector checks (`soup.select()`) into single-pass direct DOM traversals using `soup.find(class_=['class1', 'class2'])` provides a massive performance boost (~7x speedup in framework detection). `select` parses CSS strings and traverses the DOM repeatedly, while `find` with a list parameter acts as a highly optimized OR check that evaluates multiple classes in a single pass over the DOM tree.
**Action:** Always prefer `find` or `find_all` with list parameters over `select` for simple class or tag existence checks, especially in loops or critical paths.
