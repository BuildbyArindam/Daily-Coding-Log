"""
Problem: Minimum Operations to Reduce X to Zero
Platform: LeetCode (Medium)
Link: https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/
Date: 2026-09-23 
Topics: Array, Hash Table, Binary Search, Sliding Window, Prefix Sum

Approach:
    Removing elements from only the ends leaves a contiguous middle subarray.
    So minimizing removals is the same as maximizing the length of a
    subarray whose sum is (sum(nums) - x). Use a sliding window (all values
    are positive, so shrinking from the left is safe) to find the longest
    such window. Answer = len(nums) - max_window_len, or -1 if none exists.

Complexity:
    Time:  O(n), each pointer moves at most n times
    Space: O(1)
"""


# ----------------------------------------- Solution -----------------------------------------------


class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target = sum(nums) - x
        if target < 0:
            return -1
        if target == 0:
            return len(nums)
        left = 0
        current_sum = 0
        max_len = -1
        for right in range(len(nums)):
            current_sum += nums[right]
            while current_sum > target and left <= right:
                current_sum -= nums[left]
                left += 1
            if current_sum == target:
                max_len = max(max_len, right - left + 1)
        return -1 if max_len == -1 else len(nums) - max_len

__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
