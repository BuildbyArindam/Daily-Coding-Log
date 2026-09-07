"""
Problem   : Minimum Elements Outside Subsequences
Platform  : GeeksforGeeks
Link      : https://www.geeksforgeeks.org/problems/minimum-number-of-elements-which-are-not-part-of-increasing-or-decreasing-subsequence2617/1
Difficulty: Hard
Topics    : Dynamic Programming, Arrays
Date      : 2026-09-07

Approach:
dp[i][j] = length of the longest chain built so far that currently ends
with arr[i-1] as the tail of an "increasing" run and arr[j-1] as the tail
of a "decreasing" run (0 means that dimension is unused/empty).
For each new element x = arr[k-1], try extending every existing (i, j)
state: if x can extend the increasing tail (i == 0 or x > arr[i-1]),
update dp[k][j]; if x can extend the decreasing tail (j == 0 or x 
arr[j-1]), update dp[i][k]. The answer is n minus the maximum value found
across the whole dp table (the largest number of elements that can be
covered by one increasing + one decreasing subsequence).

Time complexity : O(n^3)  — one O(n^2) inner scan for each of n elements
Space complexity: O(n^2)  — dp table of size (n+1) x (n+1)
"""


# --------------------------- Solution --------------------------------


class Solution:
    def minCount(self, arr):
        """ code here """
        n = len(arr)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for k in range(1, n + 1):
            x = arr[k - 1]
            for i in range(k):
                for j in range(k):
                    cur = dp[i][j]
                    if i == 0 or x > arr[i - 1]:
                        dp[k][j] = max(dp[k][j], cur + 1)
                    if j == 0 or x < arr[j - 1]:
                        dp[i][k] = max(dp[i][k], cur + 1)
        max_used = 0
        for i in range(n + 1):
            for j in range(n + 1):
                max_used = max(max_used, dp[i][j])
        return n - max_used
