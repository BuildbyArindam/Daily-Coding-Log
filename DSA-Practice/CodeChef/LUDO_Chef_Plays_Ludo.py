"""
Problem   : Chef Plays Ludo
Platform  : CodeChef
Link      : https://www.codechef.com/problems/LUDO
Date      : 2026-09-06
Difficulty: Cakewalk
Topics    : Basic Math, Conditional Statements, Implementation

Approach:
    For each test case, read the die roll X. Chef can enter a new
    token into play only when he rolls a 6. Compare X to 6 and
    print "YES"/"NO" accordingly.

Time Complexity : O(T) — one constant-time check per test case
Space Complexity: O(1) — no extra data structures used
"""


# ---------------------- Solution ----------------------


T = int(input())
for _ in range(T):
    X = int(input())
    if X == 6:
        print("YES")
    else:
        print("NO")
