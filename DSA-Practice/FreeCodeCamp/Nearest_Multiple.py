"""
Problem: Nearest Multiple
Platform: FreeCodeCamp - Daily Coding Challenge (07-07)
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/07-07
Date Solved: 2026-08-31
Difficulty: Easy
Topics: Math, Modular Arithmetic, Basic Programming

Approach:
Compute num % multiple to get the remainder. If the remainder is at least
half of `multiple`, round up by adding the difference; otherwise round down
by subtracting the remainder.

Time Complexity: O(1) - single modulo and comparison
Space Complexity: O(1) - no extra data structures
"""


# -------------------------- Solution ---------------------------------


def round_to_nearest_multiple(num, multiple):
    remainder = num % multiple
    if remainder >= multiple / 2:
        return num + (multiple - remainder)
    else:
        return num - remainder
