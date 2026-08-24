# Problem: Count Prefix-Balanced Binary Strings
# Link: https://www.geeksforgeeks.org/problems/geek-and-his-binary-strings1951/1
# Platform: GeeksforGeeks | Difficulty: Easy | Topic: Dynamic Programming
# Date: 2026-08-24
#
# Approach:
#   dp[i] = number of prefix-balanced binary strings of length 2*i (Catalan-style).
#   Split at the first point the string returns to balance: dp[i] = sum_{j=0}^{i-1} dp[j] * dp[i-1-j]
#   dp[0] = 1 (empty string), then build bottom-up.
#
# Time Complexity: O(n^2)
# Space Complexity: O(n)


# --------------------- Solution ---------------------------


class Solution:
    def prefixStrings(self, n: int) -> int:
        # code here
        MOD = 10**9 + 7
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, n + 1):
            for j in range(i):
                dp[i] = (dp[i] + dp[j] * dp[i - 1 - j]) % MOD
        return dp[n]
