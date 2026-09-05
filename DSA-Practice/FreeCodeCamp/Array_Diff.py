"""
Problem: Array Diff
Platform: FreeCodeCamp — Daily Coding Challenge
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/09-10
Date Solved: 2026-09-05
Difficulty: Easy 
Topic: Arrays, Sets, Symmetric Difference, Hashing

Approach:
    Convert both arrays to sets and take the symmetric difference (^),
    which yields elements present in exactly one of the two arrays but
    not both. Sort the result for a deterministic, readable output.

Time Complexity:  O(n + m) — building both sets is linear in input size;
                   the symmetric difference and sort add O(k log k) for
                   the result set of size k.
Space Complexity: O(n + m) — for the two sets plus the output list.
"""


# -------------------- Solution ------------------------------


def array_diff(arr1, arr2):
    return sorted(list(set(arr1) ^ set(arr2)))
