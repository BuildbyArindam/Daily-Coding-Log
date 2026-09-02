"""
Problem   : Search an Element in an Array
Platform  : Code360
Link      : https://www.naukri.com/code360/problems/search-an-element-in-an-array_975480?kunjiRedirection=true
Difficulty: Easy
Topic     : Binary Search, Arrays
Date      : 2026-09-02

Approach:
    For each query value, run standard binary search over the sorted
    array `arr`. Maintain left/right pointers, compute mid, and narrow
    the range based on comparison with the target. Append 1 if found,
    0 otherwise, for each query.

Time Complexity : O(q * log n) — binary search per query
Space Complexity: O(q) — for the output list (O(1) extra beyond that)
"""


# ---------------------------- Solution --------------------------------


from os import *
from sys import *
from collections import *
from math import *

def searchInSortedArray(arr, n, queries, q):
    # Write your code here.
    ans = []
    for x in queries:
        left = 0
        right = n - 1
        found = False
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == x:
                found = True
                break
            elif arr[mid] < x:
                left = mid + 1
            else:
                right = mid - 1
        ans.append(1 if found else 0)
    return ans
