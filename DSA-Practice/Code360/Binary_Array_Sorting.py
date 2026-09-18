"""
Problem: Binary Array Sorting
Platform: Code360
Link: https://www.naukri.com/code360/guided-paths/data-structures-algorithms/content/118822/offering/1382143
Date: 2026-09-18
Difficulty: Easy
Topics: Two Pointers, Array Partitioning, In-place Sorting

Approach:
Two-pointer partitioning (similar to a simplified Dutch National Flag).
`left` scans from the start skipping over 0s, `right` scans from the end
skipping over 1s. When left points to a 1 and right points to a 0 (i.e.,
they're "stuck"), swap them and move both pointers inward. This sorts
the array in-place in a single pass without extra space.

Time Complexity: O(n) — each pointer traverses the array at most once
Space Complexity: O(1) — sorted in-place, no extra data structures
"""


# -------------------------------- Solution ---------------------------------------------


def sortBinaryArray(arr, n):
    # Write your code here
    left = 0
    right = n - 1
    while left < right:
        while left < right and arr[left] == 0:
            left += 1
        while left < right and arr[right] == 1:
            right -= 1
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    return arr
