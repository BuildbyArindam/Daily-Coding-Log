"""
Problem   : Bitcoin Market
Platform  : CodeChef
Link      : https://www.codechef.com/problems/P1209
Date      : 2026-08-23
Difficulty: Cakewalk
Topics    : Implementation, Conditional Statements

Approach:
Chef buys bitcoin only if the market risk level R is at most 4.
Read R and print "YES" if R <= 4, else print "NO".

Time Complexity : O(1)
Space Complexity: O(1)
"""


# -------------------- Solution ------------------------

r = int(input())
if r <= 4:
    print("YES")
else:
    print("NO")
