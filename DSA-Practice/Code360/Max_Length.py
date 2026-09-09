"""
Problem: Max Length
Platform: Code360 (Naukri)
Link: https://www.naukri.com/code360/problems/max-length_7642273?kunjiRedirection=true
Date Solved: 2026-09-09

Approach:
Count the number of distinct elements in the array by converting it to a set
and returning its length. A set automatically discards duplicates, so its
size equals the count of unique values.

Time Complexity: O(n)  -- one pass to build the set from n elements
Space Complexity: O(n) -- set can hold up to n unique elements in worst case

Difficulty: Easy
Topics: Arrays, Hashing / Sets
"""


# ------------------------ Solution ---------------------------------


from typing import *

def maxLength(a: List[int]) -> int:
    return len(set(a))
