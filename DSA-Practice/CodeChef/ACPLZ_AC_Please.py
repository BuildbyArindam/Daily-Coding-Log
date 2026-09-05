"""
Problem   : AC Please
Platform  : CodeChef
Link      : https://www.codechef.com/problems/ACPLZ
Date      : 2026-09-05
Difficulty: Cakewalk
Topics    : Basic I/O, Conditional Statements, Implementation

Approach:
    Read T (attempts made). If T exceeds 30, the verdict is impossible
    within the allowed limit -> print "NO". Otherwise -> print "YES".
    Single conditional check, no loops or data structures needed.

Complexity:
    Time  : O(1)
    Space : O(1)
"""


# ----------------------- Solution --------------------------


T = int(input())
if T > 30:
    print("YES")
else:
    print("NO")
