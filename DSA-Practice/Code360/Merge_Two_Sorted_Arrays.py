"""
Problem: Merge Two Sorted Arrays
Platform: Code360
Link: https://www.naukri.com/code360/problems/merge-two-sorted-arrays_1214628
Date: 2026-08-24
Difficulty: Medium
Topics: Two Pointers, Arrays, In-place Merging

Approach:
Merge arr2 into arr1 (which has trailing empty space for n elements) by
filling from the back. Compare the last unmerged elements of both arrays
and place the larger one at the current end position (k), moving pointers
i, j, k backward. This avoids overwriting unmerged elements in arr1 since
we always write to a slot that's already been "consumed." Any leftover
elements in arr2 are copied directly (leftover arr1 elements are already
in place).

Time Complexity:  O(m + n)
Space Complexity: O(1) — in-place, no extra array used
"""


# --------------------- Solution ------------------------


from math import *
from collections import *
from sys import *
from os import *

def ninjaAndSortedArrays(arr1, arr2, m, n):
    i = m - 1
    j = n - 1
    k = m + n - 1
    while i >= 0 and j >= 0:
        if arr1[i] > arr2[j]:
            arr1[k] = arr1[i]
            i -= 1
        else:
            arr1[k] = arr2[j]
            j -= 1
        k -= 1
    while j >= 0:
        arr1[k] = arr2[j]
        j -= 1
        k -= 1
    return arr1
