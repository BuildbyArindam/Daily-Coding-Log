"""
Problem   : Bucket Sort
Platform  : Code360
Link      : https://www.naukri.com/code360/problems/bucket-sort_4605868?kunjiRedirection=true
Date      : 2026-08-24
Difficulty: Medium
Topics    : Sorting, Counting Sort, Arrays

Approach:
Values are floats in [0, 1) with at most 2 decimal places, so each value maps
to a unique bucket index in [0, 100] via round(x * 100). Use a counting array
of size 101 to tally occurrences, then reconstruct the sorted array by
walking the counts in index order. This avoids O(n log n) comparison sort
since the value domain is small and fixed.

Time complexity : O(n + k), k = 101 (fixed) -> effectively O(n)
Space complexity: O(k) = O(1) extra (fixed-size count array), O(n) for output
"""


# ------------------------- Solution ---------------------------


from sys import *
from collections import *
from math import *

def sortArray(n: int, arr: []) -> []:
    count = [0] * 101
    for x in arr:
        count[int(round(x * 100))] += 1
    ans = []
    for i in range(101):
        while count[i] > 0:
            ans.append(i / 100)
            count[i] -= 1
    return ans
