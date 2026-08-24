"""
Problem: Pancake Sorting
Platform: Code360 (Naukri)
Link: https://www.naukri.com/code360/problems/pancake-sorting_1262344?kunjiRedirection=true
Date: 2026-08-24
Difficulty: Easy
Topics: Sorting, Greedy, Array Manipulation

Approach:
Selection-sort style pancake flipping. For each suffix size from n down to 2,
find the index of the max element within that unsorted prefix. Flip it to the
front (if not already there), then flip the whole current window to send it
to its final position at the end. Record each flip length (1-indexed) in `ans`.

Time Complexity:  O(n^2)  -- for each of n passes, O(n) scan + O(n) flip
Space Complexity: O(n)    -- for the `ans` list of flip operations (in-place otherwise)
"""


# ------------------------ Solution -----------------------------


from os import *
from sys import *
from collections import *
from math import *

def pancakeSort(arr, n):
    # Write your code here.
    ans = []
    for curr_size in range(n, 1, -1):
        max_idx = 0
        for i in range(1, curr_size):
            if arr[i] > arr[max_idx]:
                max_idx = i
        if max_idx == curr_size - 1:
            continue
        if max_idx != 0:
            arr[:max_idx + 1] = reversed(arr[:max_idx + 1])
            ans.append(max_idx + 1)
        arr[:curr_size] = reversed(arr[:curr_size])
        ans.append(curr_size)
    return ans
