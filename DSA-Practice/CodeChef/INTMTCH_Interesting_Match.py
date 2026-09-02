"""
Problem   : Interesting Match (INTMTCH)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/INTMTCH
Date      : 2026-09-02
Difficulty: Cakewalk
Topics    : Basic Math, Conditional Statements, Implementation

Approach:
A match is "interesting" iff the two scores X and Y differ by at most 2 goals.
Read the two integers, compute abs(X - Y), and compare against the threshold.

Complexity:
Time  : O(1) per test case
Space : O(1)
"""


# ------------------------- Solution --------------------------


X, Y = map(int, input().split())
if abs(X - Y) <= 2:
    print("Interesting")
else:
    print("Boring")
