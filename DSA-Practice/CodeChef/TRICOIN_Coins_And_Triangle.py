"""
Problem   : Coins And Triangle
Platform  : CodeChef
Link      : https://www.codechef.com/problems/TRICOIN
Date      : 2026-09-01
Difficulty: Cakewalk
Topics    : Basic Math / Triangular Numbers / Quadratic Formula

Approach:
Coins form a triangle where row i needs i coins, so a triangle of height h
uses h(h+1)/2 coins. We need the largest h such that h(h+1)/2 <= N.
Rearranging h(h+1)/2 <= N into a quadratic in h and solving via the
quadratic formula gives h = floor((sqrt(8N + 1) - 1) / 2).
math.isqrt is used for an exact integer square root, avoiding floating-point
precision errors for large N.

Time complexity : O(1) per query (isqrt on ~N is effectively O(log N) bit ops)
Space complexity: O(1)
"""


# ----------------------- Solution -----------------------------


import math
T = int(input())
for _ in range(T):
    N = int(input())
    height = (math.isqrt(1 + 8 * N) - 1) // 2
    print(height)
