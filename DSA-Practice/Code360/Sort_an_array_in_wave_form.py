"""
Problem: Sort an Array in Wave Form
Platform: Code360 (Naukri)
Link: https://www.naukri.com/code360/guided-paths/data-structures-algorithms/content/118822/offering/1382139
Date Solved: 2026-09-18
Difficulty: Easy
Topics: Arrays, Sorting, Greedy, Two Pointers

Approach:
    Iterate over the array in steps of 2 (even indices). For each even index i,
    find the maximum among arr[i-1], arr[i], arr[i+1] and swap it into position i.
    This guarantees arr[i] >= arr[i-1] and arr[i] >= arr[i+1], producing the
    up-down (wave) pattern in a single pass without extra space.

Time Complexity: O(n)  - single pass over the array
Space Complexity: O(1) - in-place swaps, no extra data structures
"""


# ---------------------------------- Solution --------------------------------------------------


def waveFormArray(arr, n):
    for i in range(0, n, 2):
        max_index = i
        if i - 1 >= 0 and arr[i - 1] > arr[max_index]:
            max_index = i - 1
        if i + 1 < n and arr[i + 1] > arr[max_index]:
            max_index = i + 1
        arr[i], arr[max_index] = arr[max_index], arr[i]
    return arr
