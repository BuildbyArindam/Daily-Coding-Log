"""
Problem   : Glass Prices (GLPR)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/GLPR
Date      : 2026-08-31
Difficulty: Cakewalk
Topics    : Basic Math / Conditional Statements / Implementation

Approach:
Compare cost of X glass units (2 * X per the problem's price ratio) against
plastic cost Y. If Y <= 2*X, plastic is cheaper or equal -> print "METAL"
per problem's chosen output convention; else "PLASTIC".

Time Complexity : O(1)
Space Complexity: O(1)
"""


# --------------------------- Solution -------------------------------


X, Y = map(int, input().split())
if Y <= 2 * X:
    print("METAL")
else:
    print("PLASTIC")
