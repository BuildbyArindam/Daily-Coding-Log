"""
Problem   : Ways to Reach Origin
Platform  : GeeksforGeeks
Link      : https://www.geeksforgeeks.org/problems/paths-to-reach-origin3850/1
Difficulty: Medium
Topics    : Arrays, Dynamic Programming, Matrix
Date      : 2026-09-30

Approach:
    Bottom-up 2D DP. dp[i][j] is the number of ways to reach (0, 0) from (i, j)
    when each move goes one step left or one step down. Base case dp[0][0] = 1.
    Each cell is the sum of the cell above it and the cell to its left, taken
    modulo 10^9 + 7. The answer is dp[x][y].

Complexity:
    Time : O(x * y)
    Space: O(x * y)  (can be reduced to O(y) with a rolling 1D array)
"""


# ------------------------------------- Solution ---------------------------------------


class Solution:
    def ways(self, x: int, y: int) -> int:
        # code here
        MOD = 10**9 + 7
        dp = [[0] * (y + 1) for _ in range(x + 1)]
        dp[0][0] = 1
        for i in range(x + 1):
            for j in range(y + 1):
                if i == 0 and j == 0:
                    continue
                left = dp[i - 1][j] if i > 0 else 0
                down = dp[i][j - 1] if j > 0 else 0
                dp[i][j] = (left + down) % MOD
        return dp[x][y]
