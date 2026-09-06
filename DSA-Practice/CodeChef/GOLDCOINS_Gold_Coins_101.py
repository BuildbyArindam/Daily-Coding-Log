"""
Problem   : Gold Coins 101 (GOLDCOINS)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/GOLDCOINS
Date      : 2026-09-06
Difficulty: Cakewalk
Topics    : Basic Math, Conditional Statements, Implementation

Approach:
    Read A, B, X, Y. Compare X and Y — whichever side "wins" the
    comparison determines which of A or B gets printed. Pure
    conditional logic, no loops or data structures needed.

Complexity:
    Time  : O(1)
    Space : O(1)
"""


# --------------------- Solution ---------------------------


A, B, X, Y = map(int, input().split())
if X > Y:
    print(A)
else:
    print(B)
