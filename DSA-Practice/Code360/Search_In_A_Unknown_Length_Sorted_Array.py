"""
Problem: Search In A Unknown Length Sorted Array
Link: https://www.naukri.com/code360/problems/search-in-a-unknown-length-sorted-array_7574128
Platform: Code360
Difficulty: Medium
Date: 2026-09-01
Topics: Binary Search, Exponential (Galloping) Search, Unbounded/Unknown-size Array Search

Approach:
Since the array's length is unknown, we can't binary search directly.
1. Exponential (galloping) search: start with hi = 1 and double it until
   reader.get(hi) >= X (or throws/out-of-bounds in some variants), which
   brackets X within [lo, hi] in O(log(pos)) steps.
2. Standard binary search within that [lo, hi] window to find X.

Time Complexity:  O(log P), where P is the index of X (or insertion point)
Space Complexity: O(1)
"""


# ----------------------------- Solution -------------------------------------


"""
    You should not implement this.
    class UnknownArray:
        def __init__(self, a : List[int]):

        def get(self, ind : int) -> int:
"""
from typing import *

def searchInASortedArray(reader, X : int) -> int:
    INF = 1 << 30
    if reader.get(0) == X:
        return 0
    lo = 0
    hi = 1
    while reader.get(hi) < X:
        lo = hi
        hi *= 2
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        value = reader.get(mid)
        if value == X:
            return mid
        elif value < X:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
