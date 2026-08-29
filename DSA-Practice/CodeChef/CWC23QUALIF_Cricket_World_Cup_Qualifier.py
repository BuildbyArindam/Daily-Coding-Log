"""
Problem   : Cricket World Cup Qualifier
Platform  : CodeChef
Link      : https://www.codechef.com/problems/CWC23QUALIF
Date      : 2026-08-29
Difficulty: Cakewalk (simple threshold check, single condition)
Topics    : Basic Math / Conditional Statements / Implementation

Approach:
Read points X. A team qualifies if it has reached the cutoff of 12
points, so a single if/else comparison against 12 decides Yes/No.

Complexity:
Time  : O(1) — one comparison
Space : O(1) — one integer stored
"""


# ------------------------- Solution ------------------------------


X = int(input())
if X >= 12:
    print("Yes")
else:
    print("No")
