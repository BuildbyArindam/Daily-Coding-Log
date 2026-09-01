"""
Problem: Search Insert Position
Platform: Code360
Link: https://www.naukri.com/code360/problems/search-insert-position_839813?kunjiRedirection=true
Date: 2026-09-01
Difficulty: Easy
Topic: Binary Search, Arrays

Approach:
Standard binary search over the sorted array. If target `m` is found,
return its index. Otherwise, the search naturally converges so that
`left` ends up at the correct insertion index (the first position
where `m` could be inserted to keep the array sorted).

Time Complexity: O(log n)
Space Complexity: O(1)
"""


# ----------------------- Solution ------------------------------


def searchInsert(arr: [int], m: int) -> int:
    # Write your code here.
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == m:
            return mid
        elif arr[mid] < m:
            left = mid + 1
        else:
            right = mid - 1
    return left
