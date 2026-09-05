"""
Problem: Unique Characters
Platform: FreeCodeCamp - Daily Coding Challenge (09-09)
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/09-09
Date Solved: 2026-09-05
Difficulty: Easy
Topics: String Manipulation, Hashing, Sets

Approach:
Convert the string to a set to drop duplicate characters, then compare
its length to the original string's length. If lengths match, every
character was unique.

Time Complexity: O(n) — building the set requires a single pass over the string
Space Complexity: O(n) — the set stores up to n unique characters
"""


# ------------------------- Solution -----------------------------


def all_unique(s):
    return len(s) == len(set(s))
