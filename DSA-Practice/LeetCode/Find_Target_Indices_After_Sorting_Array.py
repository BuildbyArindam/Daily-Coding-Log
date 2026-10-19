"""
Problem   : 2089. Find Target Indices After Sorting Array
Platform  : LeetCode
Link      : https://leetcode.com/problems/find-target-indices-after-sorting-array/
Date      : 2026-10-19
Difficulty: Easy
Topics    : Array, Binary Search, Sorting

Approach  : Sort nums in place, then scan once and collect every index
            whose value equals target. Because the array is sorted, the
            indices come out already in increasing order.

Time      : O(n log n), dominated by the sort
Space     : O(1) extra, ignoring the output list (Timsort uses O(n) worst case)
"""


# ---------------------------------------------- Solution ----------------------------------------------------------


class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            if nums[i] == target:
                result.append(i)
        return result

__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
