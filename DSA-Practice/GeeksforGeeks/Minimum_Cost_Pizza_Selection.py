"""
Problem: Minimum Cost Pizza Selection
Platform: GeeksforGeeks
Link: https://www.geeksforgeeks.org/problems/pizza-mania0155/1
Date: 2026-09-26
Difficulty: Medium
Topics: Dynamic Programming

Approach:
Bottom-up DP over achievable "area" (up to x). dp[i] = minimum cost to reach
at least i area of pizza. Starting from dp[0] = 0, for every area i we try
adding a small/medium/large pizza and cap the resulting area at x (since
extra area beyond x is wasted but still valid), updating dp[new_area]
with the cheaper cost. Answer is dp[x].

Time Complexity: O(x) — outer loop over 0..x, inner loop over 3 fixed pizza types → O(3x) = O(x)
Space Complexity: O(x) — dp array of size x+1
"""


# ----------------------------------- Solution -------------------------------------------


class Solution:
    def minimumCost(self, x, s, m, l, cs, cm, cl):
        # code here
        INF = float('inf')
        dp = [INF] * (x + 1)
        dp[0] = 0
        pizzas = [(s, cs), (m, cm), (l, cl)]
        for i in range(x + 1):
            if dp[i] == INF:
                continue
            for area, cost in pizzas:
                new_area = min(x, i + area)
                dp[new_area] = min(dp[new_area], dp[i] + cost)
        return dp[x]
