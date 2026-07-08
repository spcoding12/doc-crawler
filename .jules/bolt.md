## 2024-05-24 - Bypass Redundant Parsing
**Learning:** In a multi-page crawler architecture, globally detected contexts (such as the framework name) must be passed down to page-level extractors to prevent redundant and expensive DOM tree parsing on every page.
**Action:** Always pass the detected framework context to page-level extraction functions.
