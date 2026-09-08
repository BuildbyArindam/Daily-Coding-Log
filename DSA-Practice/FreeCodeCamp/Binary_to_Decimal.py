"""
Problem: Binary to Decimal
Platform: FreeCodeCamp — Daily Coding Challenge (10-01)
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/10-01
Date Solved: 2026-09-08
Difficulty: Easy
Topics: Number Base Conversion, String Manipulation, Built-in Parsing

Approach:
Use Python's built-in int(str, base) constructor to directly parse a
binary string into its decimal integer equivalent, specifying base 2.

Time Complexity: O(n)  — n = length of the binary string (digit-by-digit parsing internally)
Space Complexity: O(1) — no auxiliary space beyond the input/output
"""


# ---------------------- Solution ----------------------------


def to_decimal(binary):
    return int(binary, 2)
