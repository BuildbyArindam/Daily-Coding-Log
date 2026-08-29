"""
Problem   : Basketball Score (P1BAR)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/P1BAR
Date      : 2026-08-29
Difficulty: Cakewalk
Topics    : Basic Math, Implementation

Approach:
Total score in basketball = 3 points per 3-pointer (X) + 2 points per
2-pointer (Y). Read X and Y, compute 3*X + 2*Y directly — no loops or
conditionals needed since it's a single closed-form formula.

Time Complexity : O(1) — constant-time arithmetic on two inputs
Space Complexity: O(1) — only two integer variables stored
"""


# -------------------- Solution ------------------------


X, Y = map(int, input().split())
total_score = 3 * X + 2 * Y
print(total_score)
