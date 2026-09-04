"""
Problem   : Reach Weight
Platform  : CodeChef
Link      : https://www.codechef.com/problems/REACHWT
Date      : 2026-09-04
Difficulty: Cakewalk
Topics    : Basic Math, Parity, Conditional Statements

Approach:
To reach a weight of N kg using 30kg and 20kg plates (minimum cost),
the greedy/parity trick works: use as many 30kg units as possible via
(N // 2) pairs, since 2 * 30 = 60 covers 2kg of "weight-equivalent"
cost efficiently, and add one 20kg plate if N is odd to cover the
remaining unit. (Equivalent to: cost = 30*(N//2) + 20*(N%2))

Time Complexity : O(1) per test case, O(T) overall
Space Complexity: O(1)
"""


# ---------------------- Solution --------------------------------


T = int(input())
for _ in range(T):
    N = int(input())
    cost = (N // 2) * 30
    if N % 2 == 1:
        cost += 20
    print(cost)
