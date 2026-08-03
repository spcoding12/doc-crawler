## 2024-05-30 - Optimize DOM Traversal
**Learning:** Replaced slow CSS selector parsing (soup.select) and tag stringification (str(tag)) with optimized single-pass native find methods and direct attribute/text lookups.
**Action:** Always prefer native DOM methods (find/find_all) with precise attributes and grouped lists over .select() overhead for multi-candidate tag inspection.
