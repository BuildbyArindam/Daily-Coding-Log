"""
Problem: Min Cost To Make Two Strings Identical
Platform: GeeksforGeeks
Link: https://www.geeksforgeeks.org/problems/minimum-cost-to-make-two-strings-identical1107/1
Difficulty: Medium
Topics: Dynamic Programming
Date Solved: 2026-09-19

Approach:
LCS-based edit distance variant. Instead of insert/delete costing 1 each,
deleting a char from s1 costs `costS1` and deleting a char from s2 costs
`costS2`. We compute the LCS-style DP where matching characters are free
(carried over from the diagonal), and mismatches take the min of "drop
char from s1" (dp[j] + costS1) or "drop char from s2" (dp[j-1] + costS2).
Answer = cost to delete all characters not part of the optimal LCS,
weighted by their respective per-character costs.

Optimized to a 1D rolling DP array (space O(min(n, m))) by always making
s2 (columns) the shorter string.

Time Complexity: O(n * m)
Space Complexity: O(min(n, m))
"""


# --------------------------------------------- Solution -----------------------------------------------


class Solution:
    def findMinCost(self, s1: str, s2: str, costS1: int, costS2: int) -> int:
        # code here
        if len(s1) < len(s2):
            pass
        else:
            s1, s2 = s2, s1
            costS1, costS2 = costS2, costS1
        m = len(s2)
        dp = [j * costS2 for j in range(m + 1)]
        for i in range(1, len(s1) + 1):
            prev = dp[0]
            dp[0] = i * costS1
            for j in range(1, m + 1):
                temp = dp[j]
                if s1[i - 1] == s2[j - 1]:
                    dp[j] = prev
                else:
                    dp[j] = min(
                        dp[j] + costS1,     
                        dp[j - 1] + costS2  
                    )
                prev = temp
        return dp[m]
