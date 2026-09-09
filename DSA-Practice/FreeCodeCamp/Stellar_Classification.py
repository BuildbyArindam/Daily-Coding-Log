"""
Problem: Space Week Day 1: Stellar Classification
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/10-04
Date Solved: 2026-09-09
Platform: FreeCodeCamp
Difficulty: Easy
Topics: Conditionals, Lookup/Threshold Logic

Approach:
Classify a star by surface temperature using the Morgan-Keenan (MK)
spectral classification system. Check the temperature against each
class's lower threshold in descending order (O > B > A > F > G > K > M)
and return the first class it satisfies.

Time Complexity: O(1) — fixed number of comparisons regardless of input
Space Complexity: O(1) — no extra data structures used
"""


# -------------------------- Solution ---------------------------------


def classification(temp):
    if temp >= 30000:
        return "O"
    elif temp >= 10000:
        return "B"
    elif temp >= 7500:
        return "A"
    elif temp >= 6000:
        return "F"
    elif temp >= 5200:
        return "G"
    elif temp >= 3700:
        return "K"
    else:
        return "M"
