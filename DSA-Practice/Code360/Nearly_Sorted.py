"""
Problem: Nearly Sorted
Platform: Code360
Link: https://www.naukri.com/code360/problems/nearly-sorted_982937?kunjiRedirection=true
Difficulty: Medium
Date Solved: 2026-08-31
Topics: Heap / Priority Queue, Sliding Window, Divide and Conquer, Sorting

Approach:
    Each element is at most k positions away from its sorted position, so a
    min-heap of size (k+1) always contains the correct next smallest element.
    Slide a window of size k+1 across the array: push the next element in,
    pop the minimum out, and place it at the current write index. Once the
    window reaches the end, drain the remaining heap into the array.

Time Complexity:  O(n log k)  — each of the n elements is pushed/popped once from a heap of size k+1
Space Complexity: O(k)        — heap holds at most k+1 elements (ignoring in-place output array)
"""


# -------------------------- Solution -------------------------------


from os import *
from sys import *
from collections import *
from math import *
from heapq import *

def nearlySorted(arr, k):
    min_heap = []
    for i in range(min(k + 1, len(arr))):
        heappush(min_heap, arr[i])
    index = 0
    for i in range(k + 1, len(arr)):
        arr[index] = heappop(min_heap)
        index += 1
        heappush(min_heap, arr[i])
    while min_heap:
        arr[index] = heappop(min_heap)
        index += 1
    return arr
