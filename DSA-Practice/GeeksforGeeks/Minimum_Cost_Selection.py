"""
Problem   : Minimum Cost Selection
Platform  : GeeksforGeeks
Link      : https://www.geeksforgeeks.org/problems/buying-vegetables0016/1
Date      : 2026-08-28
Difficulty: Medium
Topic     : Dynamic Programming

Approach:
Row-wise DP where dp[j] tracks the minimum cost to reach the current
row while choosing column j, with the constraint that adjacent rows
can't pick the same column. For each row, new_dp[j] = mat[i][j] +
min of the other two columns' previous dp values. Answer is min(dp)
after processing all rows.

Time Complexity : O(n)  -- n = number of rows, 3 columns fixed
Space Complexity: O(1)  -- only two rows (dp, new_dp) of size 3 kept
"""


# ------------------------- Solution ------------------------------


class Solution:
    def minCost(self, mat):
        """code here"""
        dp = mat[0][:]
        for i in range(1, len(mat)):
            new_dp = [0, 0, 0]
            new_dp[0] = mat[i][0] + min(dp[1], dp[2])
            new_dp[1] = mat[i][1] + min(dp[0], dp[2])
            new_dp[2] = mat[i][2] + min(dp[0], dp[1])
            dp = new_dp
        return min(dp)
