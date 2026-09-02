"""
Problem   : Search In Rotated Sorted Array
Platform  : Code360
Link      : https://www.naukri.com/code360/problems/search-in-rotated-sorted-array_630450
Date      : 2026-09-02
Difficulty: Medium
Topic     : Binary Search, Rotated Sorted Array

Approach:
Modified binary search. At each step, at least one half of the array
(left..mid or mid..right) is guaranteed to be normally sorted.
- Check which half is sorted using arr[left] <= arr[mid].
- If the sorted half contains the target, narrow into it; otherwise
  search the other (unsorted) half.
- Repeat until found or the search space is exhausted.

Time Complexity : O(log n)
Space Complexity: O(1)
"""


# ------------------------- Solution --------------------------------


def search(arr, target):
    # Write your code here.
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        if arr[left] <= arr[mid]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1
