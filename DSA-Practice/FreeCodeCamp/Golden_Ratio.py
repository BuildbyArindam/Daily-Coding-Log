"""
Problem   : Golden Ratio
Platform  : FreeCodeCamp — Daily Coding Challenge (07-20)
Link      : https://www.freecodecamp.org/learn/daily-coding-challenge/07-20
Date      : 2026-09-02
Difficulty: Easy
Topics    : Math, Ratio Comparison, Floating-Point Tolerance

Approach:
    Compute the ratio of the larger to the smaller of the two inputs,
    then check whether it's within 0.01 of the golden ratio (1.618).
    A single division + absolute-difference comparison — no iteration
    or extra data structures needed.

Complexity:
    Time  : O(1)
    Space : O(1)
"""


# -------------------------- Solution -------------------------------


def is_golden_ratio(a, b):
    ratio = max(a, b) / min(a, b)
    return abs(ratio - 1.618) <= 0.01
