"""
Problem: Run Chase (RUNCHASE)
Link: https://www.codechef.com/problems/RUNCHASE
Date: 2026-08-23
Difficulty: Easy
Topics: Math, Basic Programming

Approach:
To score strictly more than N runs in 20 overs, find the minimum
constant runs-per-over rate R such that 20*R > N, i.e. R > N/20.
The smallest integer satisfying this is floor(N/20) + 1.

Time Complexity: O(1)
Space Complexity: O(1)
"""


# -------------------- Solution -------------------------


n = int(input())
r = (n // 20) + 1
print(r)
