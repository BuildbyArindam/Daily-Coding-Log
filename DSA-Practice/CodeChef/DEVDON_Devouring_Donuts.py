"""
Problem   : Devouring Donuts (DEVDON)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/DEVDON
Date      : 2026-09-02
Difficulty: Cakewalk
Topics    : Basic Math, Implementation

Approach:
    Chef eats X boxes, each containing Y donuts, so the total number of
    donuts devoured is simply the product X * Y. Read the two integers
    and print their product directly — no loops or edge-case handling
    needed.

Complexity:
    Time  : O(1)
    Space : O(1)
"""


# ------------------------ Solution ---------------------------


X, Y = map(int, input().split())
print(X * Y)
