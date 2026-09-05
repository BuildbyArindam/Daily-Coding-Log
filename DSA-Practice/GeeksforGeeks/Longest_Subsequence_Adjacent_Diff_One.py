"""
Problem: Longest Subsequence with Adjacent Diff as 1
Platform: GeeksforGeeks
Link: https://www.geeksforgeeks.org/problems/longest-sub-sequence-such-that-difference-between-adjacents-is-one2558/1
Difficulty: Easy
Topic: Arrays
Date: 2026-09-05

Approach:
Dynamic programming with a hashmap keyed by element value.
dp[x] = length of the longest valid subsequence ending in value x.
For each element, look at dp[x-1] and dp[x+1] (the longest chains that
could extend into x), take the better one, add 1, and update dp[x].
Track the running max as the answer.

Time Complexity: O(n)
Space Complexity: O(n)  -- for the dp hashmap
"""


# --------------------------- Solution --------------------------------

class Solution:
    def longestSubseq(self, arr):
        dp = {}
        ans = 0
        for x in arr:
            prev = max(dp.get(x - 1, 0), dp.get(x + 1, 0))
            dp[x] = max(dp.get(x, 0), prev + 1)
            ans = max(ans, dp[x])
        return ans
