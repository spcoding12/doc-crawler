
## $(date +%Y-%m-%d) - [BeautifulSoup Performance]
**Learning:** Using BeautifulSoup's CSS selector `.select()` incurs a massive performance overhead in tight loops because it relies on the `soupsieve` package to compile and match complex selectors.
**Action:** Always replace `.select()` with native `.find()` and `.find_all()` using direct attribute lookups (`class_=[...]`, `attrs={...}`) for performance-critical DOM traversals.
