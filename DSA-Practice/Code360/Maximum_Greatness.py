"""
Problem: Maximum Greatness
Platform: Code360
Link: https://www.naukri.com/code360/problems/maximum-greatness_4609691
Date Solved: 2026-08-29
Difficulty: Medium
Topics: Greedy, Two Pointers, Sorting

Approach:
Sort both arrays x and y. Use a greedy two-pointer scan over sorted x:
for each value in x, try to match it against the smallest unused y[j]
that it can "beat" (value > y[j]). Each successful match increases the
answer and advances j, since a larger x value should be reserved for
larger y values it can still beat. This greedy works because matching
the smallest feasible y first never hurts future matches (exchange
argument / standard greedy-matching proof).

Time Complexity: O(n log n)  -- dominated by sorting both arrays
Space Complexity: O(1)       -- excluding input storage, in-place sort
"""


# ------------------------ Solution ----------------------------


from os import *
from sys import *
from collections import *
from math import *
from typing import *
from builtins import open

def MaximumGreatness(n: int, x: List[int], y: List[int]):
    x.sort()
    y.sort()
    j = 0
    ans = 0
    for value in x:
        if j < n and value > y[j]:
            ans += 1
            j += 1
    return ans
