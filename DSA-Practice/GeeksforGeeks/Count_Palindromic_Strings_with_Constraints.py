"""
Problem: Count Palindromic Strings with Constraints
Platform: GeeksForGeeks
Link: https://www.geeksforgeeks.org/problems/number-of-palindromic-strings2706/1
Difficulty: Medium
Topics: Strings, Dynamic Programming, Mathematics, Combinatorics
Date Solved: 2026-09-01

Approach:
    For a string of length n built from k distinct characters, count strings
    that can be rearranged into a palindrome, using permutations instead of
    brute force. A palindrome of length n is fully determined by choosing an
    ordered set of m "outer pair" characters (m = 0..k) plus, if the leftover
    length is odd, one more character for the center.
        - perm = P(k, m) = k*(k-1)*...*(k-m+1), built incrementally.
        - If 2m <= n and m > 0: perm ways to arrange the pairs (even coverage).
        - If 2m+1 <= n: perm * (k - m) ways, choosing a distinct center char.
    Sum all valid contributions mod 1e9+7.

Time Complexity:  O(k)
Space Complexity: O(1)
"""


# ------------------------ Solution -----------------------------


class Solution:
    def palindromicStrings(self, n, k):
        # code here
        MOD = 10**9 + 7
        perm = 1
        ans = 0
        for m in range(0, k + 1):
            if m > 0:
                perm = (perm * (k - m + 1)) % MOD
            if 2 * m <= n:
                if m > 0:  
                    ans = (ans + perm) % MOD
            if 2 * m + 1 <= n:
                ways_odd = (perm * (k - m)) % MOD
                ans = (ans + ways_odd) % MOD
        return ans
