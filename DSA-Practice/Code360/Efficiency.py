"""
Problem   : Efficiency
Platform  : Code360 (Naukri)
Link      : https://www.naukri.com/code360/problems/efficiency_7623464?kunjiRedirection=true
Difficulty: Hard
Date      : 2026-08-24
Topics    : Dynamic Programming, Greedy, Sorting, Knapsack-style Assignment

Approach:
Sort the outcome values ascending. We want to assign each value a
"rank weight" k (1..n) such that each rank is used at most once,
maximizing sum(value * assigned_rank). Since sorting fixes a natural
order, use a bounded knapsack-style DP where dp[k] = best achievable
total using exactly k rank-assignments so far, processing values in
sorted order and iterating k in reverse to avoid reusing the same
rank twice for one value (0/1 knapsack pattern).

Time Complexity : O(n^2)   -- n values x n possible ranks
Space Complexity: O(n)     -- dp array of size n+1
"""


# -------------------------- Solution ------------------------------


def maximumEfficiency(outcome: [int], n: int) -> int:
    outcome.sort()
    dp = [float('-inf')] * (n + 1)
    dp[0] = 0
    for value in outcome:
        for k in range(n, 0, -1):
            if dp[k - 1] != float('-inf'):
                dp[k] = max(dp[k], dp[k - 1] + k * value)
    return max(0, max(dp))
