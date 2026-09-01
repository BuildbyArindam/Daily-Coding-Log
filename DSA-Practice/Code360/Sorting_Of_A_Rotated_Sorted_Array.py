"""
Problem   : Sorting Of A Rotated Sorted Array
Platform  : Code360
Link      : https://www.naukri.com/code360/problems/sorting-of-a-rotated-sorted-array_1070231
Difficulty: Easy
Topics    : Arrays, Sorting, Rotation

Approach:
    A sorted array that's been rotated has exactly one "drop point" (pivot)
    where arr[i] > arr[i+1]. Scan for that pivot in a single pass, then
    rotate the array back into sorted order by slicing at pivot+1 and
    swapping the two halves. If no pivot is found, the array is already sorted.

Time Complexity : O(n)  — single pass to find pivot + O(n) slice/concat
Space Complexity: O(n)  — new list created by slicing/concatenation
                          (could be reduced to O(1) with in-place reversal
                          via the "reverse three times" rotation trick)
"""


# -------------------------- Solution ----------------------------


from os import *
from sys import *
from collections import *
from math import *

def sortRotatedArray(arr, n):
    pivot = -1
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            pivot = i
            break
    if pivot == -1:
        return
    arr[:] = arr[pivot + 1:] + arr[:pivot + 1]
