"""
Problem   : Saving Taxes (TAXSAVING)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/TAXSAVING
Date      : 2026-09-06
Difficulty: Cakewalk
Topics    : Basic Math, Basic I/O, Implementation

Approach:
    For each test case, read two integers X (income) and Y (tax paid),
    and output the saved amount as X - Y. Pure arithmetic, no edge
    case handling required since constraints guarantee valid input.

Complexity:
    Time  : O(T) — O(1) per test case
    Space : O(1) — no auxiliary storage beyond input variables
"""


# ---------------------- Solution ----------------------------


T = int(input())
for _ in range(T):
    X, Y = map(int, input().split())
    print(X - Y)
