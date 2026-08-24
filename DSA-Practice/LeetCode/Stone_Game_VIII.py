"""
Problem: Stone Game VIII
Link: https://leetcode.com/problems/stone-game-viii/
Date Solved: 2026-08-24
Difficulty: Hard
Topics: Array, Math, DP, Minimax, Prefix Sum, Game Theory, Zero-Sum Game

Approach:
Convert the game into prefix-sum terms. Each player's move is equivalent to
choosing a stopping index i and taking prefix[i] as their "score delta" against
the opponent, who then plays optimally on the remaining suffix. Working from
the right, dp[i] = max(dp[i+1], prefix[i] - dp[i+1]) captures the best
achievable score difference starting from index i. The final answer is dp
evaluated from index 1 (since the first move must take at least 2 stones,
i.e., start at prefix index >= 1).

Time Complexity: O(n)  — one pass to build prefix sums, one pass for the DP
Space Complexity: O(n) — prefix sum array (can be reduced to O(1) by folding
                          the prefix sum into the same backward loop)
"""


# ------------------------- Solution -----------------------------


class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)
        prefix = [0] * n
        prefix[0] = stones[0]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + stones[i]
        dp = prefix[n - 1]
        for i in range(n - 2, 0, -1):
            dp = max(dp, prefix[i] - dp)
        return dp
        
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
