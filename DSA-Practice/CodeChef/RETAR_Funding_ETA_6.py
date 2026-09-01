"""
Problem   : Funding ETA 6
Platform  : CodeChef
Link      : https://www.codechef.com/problems/RETAR
Date      : 2026-09-01
Difficulty: Cakewalk (estimated)
Topics    : Basic Math, Conditional Statements, Implementation

Approach:
Read X, A, Y, B (two revenue streams' unit counts and rates) and D
(the funding target). Compute total revenue = X*A + Y*B and compare
it against D — print "YES" if the target is met or exceeded, else "NO".

Time Complexity : O(1)  — single arithmetic comparison, no iteration
Space Complexity: O(1)  — fixed number of scalar variables
"""


# -------------------------- Solution ----------------------------------


X, A, Y, B, D = map(int, input().split())
revenue = X * A + Y * B
if revenue >= D:
    print("YES")
else:
    print("NO")
