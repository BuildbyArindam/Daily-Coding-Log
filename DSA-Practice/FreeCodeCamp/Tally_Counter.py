"""
Problem: Tally Counter
Platform: FreeCodeCamp (Daily Coding Challenge)
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/07-13
Date Solved: 2026-09-02
Difficulty: Easy
Topics: String Manipulation, Character Counting, Frequency Counting

Approach:
Count the tally marks by summing the occurrences of "|" (single mark)
and "/" (diagonal mark used to close a group of five) in the string.
Python's built-in str.count() handles both in linear time.

Time Complexity: O(n) — single pass over the string per count() call (two passes total)
Space Complexity: O(1) — no auxiliary data structures used
"""


# ---------------------- Solution ----------------------------


def get_tally_count(s):
    return s.count("|") + s.count("/")
