"""
Problem   : Minimum Squares with Full Cuts
Platform  : GeeksforGeeks
Link      : https://www.geeksforgeeks.org/problems/squares-in-reactangle3340/1
Difficulty: Medium
Topics    : Mathematics, Greedy, GCD / Euclidean algorithm
Date      : 2026-10-12

Approach:
    Repeatedly cut the largest possible square from the n x m rectangle.
    With n >= m, we get n // m squares of side m, leaving an m x (n % m)
    rectangle. Repeat until one side reaches 0. This is the Euclidean GCD
    algorithm, with the quotients at each step summed up.

Time Complexity : O(log(min(n, m)))
Space Complexity: O(1)
"""


# -------------------------------------------- Solution ----------------------------------------------------


class Solution:
    def minSquares(self, n, m):
        # code here
        count = 0
        while n > 0 and m > 0:
            if n < m:
                n, m = m, n
            count += n // m
            n = n % m
        return count
