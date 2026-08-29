"""
Problem: Bubble Sort
Platform: Code360
Link: https://www.naukri.com/code360/problems/bubble-sort_624380?kunjiRedirection=true
Date: 2026-08-29
Difficulty: Easy
Topics: Sorting, Arrays

Approach:
Standard bubble sort with early-exit optimization. Repeatedly compare
adjacent elements and swap if out of order, pushing the largest
unsorted element to the end each pass. A `swapped` flag breaks out
early once a full pass makes no swaps, meaning the array is already sorted.

Time Complexity:  O(n^2) worst/average case, O(n) best case (already sorted)
Space Complexity: O(1) — in-place, only a swapped flag used
"""


# ----------------------- Solution ---------------------------


from typing import List

def bubbleSort(arr: List[int], n: int):
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
