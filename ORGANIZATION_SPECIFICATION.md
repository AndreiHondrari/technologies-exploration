# Numeric Prefix Organization System Specification

## 1. Core Rules
* **Padding:** All numerical identifiers MUST be zero-padded to at least two digits (e.g., `01`, `02`) to guarantee correct sequential sorting.
* **Separators:** Use underscores (`_`) to separate numerical levels from each other and to separate words in the description.
* **Casing:** Descriptions MUST use standard `snake_case` (all lowercase) to avoid cross-platform conflicts.
* **Format Base:** `[L1]_[L2]_[...Ln]_[description]`

## 2. Hierarchy Structure
* **Arbitrary Depth:** Nesting can continue indefinitely by appending new two-digit numeric prefixes. There is no hard limit to the depth of the tree.
* **Level 1 (Main Topic):** `XX_description` (e.g., `01_main_thing`)
* **Level 2 (Subchapter):** `XX_YY_description` (e.g., `01_01_first_subchapter`)
* **Level N (Deep Node):** `XX_YY_..._ZZ_description` (e.g., `01_02_04_01_03_specific_concept`)

## 3. Special Conventions
* **The `00` Index (Metadata & Overview):** The `00` prefix at any level is strictly reserved for metadata, overviews, or configuration files pertaining to its parent category. 
    * *Level 1 Example:* `00_global_metadata`
    * *Level 2 Example:* `01_00_main_thing_overview`
    * *Level 3 Example:* `01_02_00_subchapter_context`