"""
Problem   : Entry Check
Platform  : CodeChef
Link      : https://www.codechef.com/problems/P1169
Date      : 2026-08-24
Difficulty: Cakewalk
Topics    : Basic I/O, Conditional Statements, Implementation

Approach:
Read integer X. If X >= 10, entry is allowed ("YES"); otherwise
entry is denied ("NO"). Single condition check, no edge cases
beyond the threshold comparison.

Complexity:
Time  : O(1)
Space : O(1)
"""


# -------------------- Solution -----------------------


x = int(input())
if x >= 10:
    print("YES")
else:
    print("NO")
