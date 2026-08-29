"""
Problem   : Entertainments (ENTERTAIN)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/ENTERTAIN
Date      : 2026-08-29
Difficulty: Cakewalk
Topics    : Basic Math, Conditional Statements, Implementation

Approach:
Compute the total toy cost as N * 200, then cap it at 1000 using min(),
since the shop only ever charges up to Rs. 1000 regardless of quantity.

Time Complexity : O(1)
Space Complexity: O(1)
"""


# --------------------- Solution -----------------------------


N = int(input())
toy_cost = N * 200
print(min(1000, toy_cost))
