"""
Problem   : Contrast Rating 2
Platform  : FreeCodeCamp (Daily Coding Challenge)
Link      : https://www.freecodecamp.org/learn/daily-coding-challenge/07-29
Date      : 2026-09-04
Difficulty: Easy-Medium (typical consensus for this problem)
Topics    : Conditional Logic, WCAG Accessibility Rules, Ratio Comparison

Approach:
Compute the WCAG contrast ratio from the two relative luminance values
using (L1 + 0.05) / (L2 + 0.05), then classify it against the AAA/AA
thresholds. Thresholds differ depending on whether the text is "large"
(4.5 / 3.0) or normal-sized (7.0 / 4.5), checked in descending order.

Time Complexity : O(1) — fixed number of comparisons
Space Complexity: O(1) — no extra data structures
"""


# ------------------------- Solution -----------------------------------


def get_contrast_rating(l1, l2, is_large_text):
    ratio = (l1 + 0.05) / (l2 + 0.05)
    if is_large_text:
        if ratio >= 4.5:
            return "AAA"
        elif ratio >= 3.0:
            return "AA"
        else:
            return "Fail"
    else:
        if ratio >= 7.0:
            return "AAA"
        elif ratio >= 4.5:
            return "AA"
        else:
            return "Fail"
