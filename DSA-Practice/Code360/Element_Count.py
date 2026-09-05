"""
Problem: Element Count
Platform: Code360
Link: https://www.naukri.com/code360/problems/element-count_7118507?kunjiRedirection=true
Date: 2026-09-05
Difficulty: Easy
Topics: Hashing, Sets, Frequency Counting

Approach:
    Put all array elements into a set for O(1) lookups. For each element x,
    check whether x + 1 also exists in the array (via the set). Count how
    many elements have their "successor" present.

Time Complexity: O(N)  - one pass to build the set, one pass to check membership
Space Complexity: O(N) - set stores up to N distinct elements
"""


# ------------------------ Solution -----------------------------


from typing import *
def elementCount(A: List[int]) -> int:
    present = set(A)
    count = 0
    for x in A:
        if x + 1 in present:
            count += 1
    return count
