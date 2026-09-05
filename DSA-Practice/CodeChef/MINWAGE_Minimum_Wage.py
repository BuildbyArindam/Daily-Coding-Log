"""
Problem   : Minimum Wage
Link      : https://www.codechef.com/problems/MINWAGE
Platform  : CodeChef
Date      : 2026-09-05
Difficulty: Cakewalk
Topics    : Basic Math, Conditional Statements, Implementation

Approach:
Read a single integer X. If X exceeds the threshold (11),
print "YES", otherwise print "NO". Direct O(1) comparison,
no loops or data structures needed.

Time Complexity : O(1)
Space Complexity: O(1)
"""


# ----------------------- Solution ----------------------------


X = int(input())
if X > 11:
    print("YES")
else:
    print("NO")
