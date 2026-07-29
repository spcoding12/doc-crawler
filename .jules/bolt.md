## 2024-05-24 - Avoid bs4 stringification in loops
**Learning:** Using `str(tag)` on BeautifulSoup tag objects incurs severe serialization performance penalties, up to 4x slower than targeted `.get()` or `.text` attribute extraction, completely negating any regex or string match speed advantages.
**Action:** When validating specific HTML elements for text/attributes, directly target the string representations (e.g. `tag.get('src', '')` or `tag.text`) instead of stringifying the entire node tree.

## 2024-05-24 - Pass upstream metadata to avoid redundant DOM re-parsing
**Learning:** The multi-page crawling loop in `src/main.py` redundantly re-ran full framework detection (and all string matches/DOM traversals) on every individual page instead of utilizing the globally detected `adapter` context discovered on the initial entry point.
**Action:** In crawler loops, inject known upstream invariants (like the framework name) into the parser (e.g., via `extract_content(..., framework=adapter.name)`) to immediately bypass costly fallback routines downstream.
