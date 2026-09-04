"""
Problem: Contrast Rating 1
Platform: FreeCodeCamp (Daily Coding Challenge)
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/07-28
Date Solved: 2026-09-04
Difficulty: Easy
Topics: Conditional Logic, String-to-Float Parsing, WCAG Accessibility Rules

Approach:
Convert the ratio to float, then branch on is_large_text to apply the
correct WCAG contrast thresholds (large text: 3.0/4.5, normal text: 4.5/7.0),
returning "AAA", "AA", or "Fail" accordingly.

Time Complexity: O(1) — fixed number of comparisons
Space Complexity: O(1) — no extra data structures
"""


# ------------------------- Solution --------------------------------


def get_contrast_rating(ratio, is_large_text):
    ratio = float(ratio)
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
