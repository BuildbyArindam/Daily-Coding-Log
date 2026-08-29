"""
Problem   : Count Subsequences Divisible by N
Platform  : GeeksforGeeks
Link      : https://www.geeksforgeeks.org/problems/number-of-subsequences-in-a-string-divisible-by-n5947/1
Date      : 2026-08-29
Difficulty: Medium
Topic     : Dynamic Programming

Approach:
    Track counts of subsequences ending in each remainder class mod n
    using a running DP array `dp[r]` = number of subsequences formed so
    far whose numeric value mod n equals r. For each new digit, every
    existing subsequence with remainder r extends to remainder
    (r*10 + digit) % n, and the digit itself also starts a new
    length-1 subsequence with remainder (digit % n). Answer is dp[0]
    (excluding the empty subsequence, since dp starts at all zeros).

Time complexity : O(len(s) * n)
Space complexity: O(n)
"""


# ----------------------------- Solution ----------------------------------


class Solution:
    def countSubsequences(self, s, n):
        # code here
        MOD = 10**9 + 7
        dp = [0] * n
        for ch in s:
            digit = int(ch)
            ndp = dp[:]
            ndp[digit % n] = (ndp[digit % n] + 1) % MOD
            for r in range(n):
                if dp[r]:
                    new_r = (r * 10 + digit) % n
                    ndp[new_r] = (ndp[new_r] + dp[r]) % MOD
            dp = ndp
        return dp[0]
