"""
Problem: Credit Card Masker
Platform: FreeCodeCamp (Daily Coding Challenge #10-17)
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/10-17
Difficulty: Easy
Topics: Strings, Splitting & Joining, Data Masking
Date Solved: 2026-09-10

Approach:
Detect whether the card number uses '-' or ' ' as its separator, split
the string on that separator into 4 groups, then rebuild the string by
replacing the first three groups with '****' and keeping the last group
(last 4 digits) unchanged, rejoined with the same separator.

Time Complexity: O(n) — split and join each traverse the string once
Space Complexity: O(n) — storing the split parts and the rebuilt string

Note: Assumes the input always has exactly 4 groups separated by '-' or
' '. Doesn't validate malformed input (e.g., all-digit strings with no
separator).
"""


# ------------------------- Solution ---------------------------------


def mask(card):
    separator = '-' if '-' in card else ' '
    parts = card.split(separator)
    return separator.join(['****', '****', '****', parts[3]])
