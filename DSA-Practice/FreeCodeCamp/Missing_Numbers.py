"""
Problem: Missing Numbers
Platform: FreeCodeCamp (Daily Coding Challenge)
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/09-13
Date Solved: 2026-09-05
Difficulty: Easy
Topics: Arrays, Hashing, Sets

Approach:
Convert the array to a set for O(1) lookups, then scan the range
[1, max(arr)] and collect every number not present in the set.

Time Complexity: O(n) — n = max(arr), one pass to build the set + one pass over the range
Space Complexity: O(n) — set of arr elements + missing list
"""


# ---------------------- Solution ----------------------------


def find_missing_numbers(arr):
    n = max(arr)
    numbers = set(arr)
    missing = []
    for i in range(1, n + 1):
        if i not in numbers:
            missing.append(i)
    return missing
