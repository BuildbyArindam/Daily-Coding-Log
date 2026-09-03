"""
Problem: Max Adjacent Diffs Sum with 1 Replacements
Platform: GeeksforGeeks
Link: https://www.geeksforgeeks.org/problems/modify-array-to-maximize-sum-of-adjacent-differences1729/1
Date: 2026-09-03
Difficulty: Medium
Topics: Dynamic Programming, Arrays

Approach:
DP over two states per index — dp_original (current element kept as-is)
and dp_one (current element replaced by 1). At each step, transition
from both previous states, taking the best sum of absolute adjacent
differences. Final answer is the max of the two states at the last index.

Time Complexity:  O(n)
Space Complexity: O(1)
"""


# ------------------------------- Solution -----------------------------------


class Solution:
    def maxDiffSum(self, arr):
        # code here
        n = len(arr)
        if n <= 1:
            return 0
        dp_original = 0
        dp_one = 0
        for i in range(1, n):
            new_original = max(
                dp_original + abs(arr[i] - arr[i - 1]),
                dp_one + abs(arr[i] - 1)
            )
            new_one = max(
                dp_original + abs(1 - arr[i - 1]),
                dp_one
            )
            dp_original = new_original
            dp_one = new_one
        return max(dp_original, dp_one)
