"""
Problem: Array Duplicates
Platform: FreeCodeCamp — Daily Coding Challenge
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/08-30
Date Solved: 2026-08-30
Difficulty: Easy
Topics: Arrays, Hashing, Frequency Counting

Approach:
Iterate through the array; for each number, check if it appears more
than once (arr.count(num) > 1) and hasn't already been recorded.
Collect qualifying numbers, then sort before returning.

Time Complexity: O(n^2) — arr.count() inside the loop rescans the
                  array for every element.
Space Complexity: O(n) — for the duplicates list (worst case).

Note: Can be optimized to O(n) time / O(n) space using a
frequency dictionary (collections.Counter) instead of arr.count().
"""


# ----------------------- Solution ---------------------------


def find_duplicates(arr):
    duplicates = []
    for num in arr:
        if arr.count(num) > 1 and num not in duplicates:
            duplicates.append(num)
    duplicates.sort()
    return duplicates
