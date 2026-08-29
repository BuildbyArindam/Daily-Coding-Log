"""
Problem: Move All Negative Numbers To Beginning And Positive To End
Platform: Code360
Link: https://www.naukri.com/code360/problems/move-all-negative-numbers-to-beginning-and-positive-to-end_1112620
Difficulty: Easy
Date: 2026-08-29
Topics: Two Pointers, Array Partitioning

Approach:
Two-pointer partition (similar to Dutch National Flag).
- 'left' scans from the start looking for a positive/zero number that's out of place.
- 'right' scans from the end looking for a negative number that's out of place.
- Swap when both are found, otherwise advance the pointer that's already correct.
- Note: zero is treated as "positive" (goes to the end) per problem statement.

Time Complexity: O(n) — each pointer moves at most n times total.
Space Complexity: O(1) — in-place swaps, no extra array.
"""


# ------------------------ Solution ---------------------------


from os import *
from sys import *
from collections import *
from math import *

def separateNegativeAndPositive(nums):
    left = 0
    right = len(nums) - 1
    while left <= right:
        if nums[left] < 0:
            left += 1
        elif nums[right] >= 0:
            right -= 1
        else:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
    return nums
