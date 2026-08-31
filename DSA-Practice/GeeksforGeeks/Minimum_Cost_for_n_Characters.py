"""
Problem: Minimum Cost for n Characters
Link: https://www.geeksforgeeks.org/problems/minimum-time1238/1
Platform: GeeksforGeeks
Date Solved: 2026-08-31
Difficulty: Medium
Topic: Dynamic Programming

Approach:
Bottom-up DP where dp[x] = minimum cost to build a string of length x,
starting from length 0, using three operations:
  - Insert one character (cost i)
  - Delete one character (cost d)
  - Copy-paste current string, doubling its length (cost c)

For each length x from 1 to n:
  - Base case: reach x by inserting from x-1        -> dp[x-1] + i
  - If x is even: reach x by copying x//2            -> dp[x//2] + c
  - If x is odd: reach x either by
      - copying (x//2) then inserting 1               -> dp[x//2] + c + i
      - copying (x//2 + 1) then deleting 1             -> dp[x//2+1] + c + d
Take the minimum among all valid options at each step.

Time Complexity: O(n)  -- single pass, O(1) work per step
Space Complexity: O(n) -- dp array of size n+1
"""


# ---------------------------- Solution ------------------------------------


class Solution:
    def minCost(self, n: int, i: int, d: int, c: int) -> int:
        # code here
        dp = [0] * (n + 1)
        for x in range(1, n + 1):
            dp[x] = dp[x - 1] + i
            half = x // 2
            if x % 2 == 0:
                dp[x] = min(dp[x], dp[half] + c)
            else:
                dp[x] = min(dp[x], dp[half] + c + i)
                dp[x] = min(dp[x], dp[half + 1] + c + d)
        return dp[n]
