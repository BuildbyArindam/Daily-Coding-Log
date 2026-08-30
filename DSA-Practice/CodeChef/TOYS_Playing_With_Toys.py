"""
Problem   : Playing with Toys
Platform  : CodeChef
Link      : https://www.codechef.com/problems/TOYS
Date      : 2026-08-30
Difficulty: Cakewalk
Topics    : Basic Math, Conditional Statements, Implementation

Approach:
Given N toys and M toys that can be carried away, the toys left behind
is simply N - M, clamped at 0 (can't go negative if M > N).

Time Complexity : O(1)
Space Complexity: O(1)
"""


# ---------------------- Solution ---------------------------


N, M = map(int, input().split())
toys_left = max(0, N - M)
print(toys_left)
