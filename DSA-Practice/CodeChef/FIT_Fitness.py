"""
Problem   : Fitness (FIT)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/FIT
Date      : 2026-09-06
Difficulty: Cakewalk
Topics    : Basic Math, Implementation

Approach:
Chef walks X km to office and X km back home, 5 days a week.
Weekly distance = X * 2 (round trip) * 5 (working days).
Simply read T test cases and print X * 10 for each.

Complexity:
Time  : O(1) per test case, O(T) overall
Space : O(1)
"""


# ---------------------- Solution ------------------------------


T = int(input())
for _ in range(T):
    X = int(input())
    print(X * 2 * 5)
