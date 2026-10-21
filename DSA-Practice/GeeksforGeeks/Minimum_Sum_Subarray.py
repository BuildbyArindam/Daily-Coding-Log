"""
Problem   : Minimum Sum Subarray
Platform  : GeeksforGeeks
Link      : https://www.geeksforgeeks.org/problems/smallest-sum-contiguous-subarray/1
Difficulty: Medium
Topics    : Arrays, Dynamic Programming
Date      : 2026-10-21

Approach:
    Kadane's algorithm, inverted to find the minimum. At each index, either
    extend the current subarray or start fresh at arr[i], whichever gives the
    smaller sum. Track the smallest value seen across all positions.

Time Complexity : O(n), single pass
Space Complexity: O(1)
"""


# --------------------------------------------- Solution -------------------------------------------------------


class Solution:
    def minSubarraySum(self, arr: list[int]) -> int:
        # code here
        curr_sum = arr[0]
        min_sum = arr[0]
        for i in range(1, len(arr)):
            curr_sum = min(arr[i], curr_sum + arr[i])
            min_sum = min(min_sum, curr_sum)
        return min_sum
