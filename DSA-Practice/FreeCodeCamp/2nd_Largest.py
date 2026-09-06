"""
Problem: 2nd Largest
Platform: FreeCodeCamp - Daily Coding Challenge (09-25)
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/09-25
Date Solved: 2026-09-06
Difficulty: Easy
Topics: Arrays, Sorting, Sets (Hashing)

Approach:
    Convert the array to a set to drop duplicates, then sort the
    unique values in descending order and return the element at
    index 1 (the second-largest distinct value).

Time Complexity: O(n log n) - dominated by the sort
Space Complexity: O(n) - for the set/list of unique values
"""


# ---------------------- Solution ----------------------------


def second_largest(arr):
    unique_numbers = list(set(arr))
    unique_numbers.sort(reverse=True)
    return unique_numbers[1]
