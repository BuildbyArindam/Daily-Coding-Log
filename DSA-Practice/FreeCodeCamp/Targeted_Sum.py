"""
Problem: Targeted Sum
Platform: FreeCodeCamp - Daily Coding Challenge (08-17)
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/08-17
Date Solved: 2026-08-30
Difficulty: Easy
Related topics: Arrays, Hashing, Brute Force, Two Pointers (if array is sorted)

Approach:
Brute-force pair search. For each index i, scan every later index j
and check if arr[i] + arr[j] equals target. Return the first matching
index pair found.

Time Complexity: O(n^2)  — nested loop over all index pairs
Space Complexity: O(1)   — no auxiliary data structures used

Note: Can be optimized to O(n) time / O(n) space using a hash map
that stores value -> index as you iterate once through the array.
"""


# ------------------------- Solution --------------------------------


def find_target(arr, target):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return [i, j]
    return "Target not found"
