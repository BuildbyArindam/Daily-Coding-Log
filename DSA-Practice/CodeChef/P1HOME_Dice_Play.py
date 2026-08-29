"""
Problem   : Dice Play
Platform  : CodeChef
Link      : https://www.codechef.com/problems/P1HOME
Date      : 2026-08-29
Difficulty: Cakewalk (basic conditional check, similar to your other CodeChef cakewalk solves)
Topics    : Basic Math / Conditional Statements / Implementation

Approach:
    Read two integers A and B. The dice "match" (or the play succeeds)
    exactly when both values are equal, so a single equality check
    decides the answer — no loops or extra data structures needed.

Time Complexity : O(1)
Space Complexity: O(1)
"""


# ----------------------- Solution --------------------------------


A, B = map(int, input().split())
if A == B:
    print("YES")
else:
    print("NO")
