"""
Problem: String Count
Platform: FreeCodeCamp - Daily Coding Challenge
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/10-14
Date Solved: 2026-09-10
Difficulty: Easy
Topics: Strings, Substring Search, Sliding Window (fixed-size)

Approach:
Slide a window of length len(parameter) across text. At each valid
starting index, slice out a substring of that length and compare it
to parameter. Increment a counter on match. This checks every
possible alignment, including overlapping occurrences.

Time Complexity: O(n * m) where n = len(text), m = len(parameter)
  - (n - m + 1) window positions, each comparison costs O(m)
Space Complexity: O(1) extra space (excluding the slice itself,
  which is O(m) per iteration but not retained)
"""


# ----------------------------- Solution -----------------------------------


def count(text, parameter):
    total = 0
    for i in range(len(text) - len(parameter) + 1):
        if text[i:i + len(parameter)] == parameter:
            total += 1
    return total
