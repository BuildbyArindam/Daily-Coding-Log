"""
Problem   : Vacation Excitement (VACAEX)
Platform  : CodeChef (Starter 229, Division 2/3/4)
Link      : https://www.codechef.com/problems/VACAEX
Date      : 2026-08-21
Difficulty: Cakewalk
Topics    : Basic Math, Ad-Hoc, Implementation

Approach:
Excitement increases by 1 each day starting from 1. Given the
excitement value X on some reference day and querying day Y,
the answer is simply X + Y - 1 (arithmetic progression, common
difference 1). Pure O(1) formula, no loops needed.

Time Complexity : O(1) per test case
Space Complexity: O(1)
"""


# ------------------------- Soluton ----------------------------


X, Y = map(int, input().split())
print(Y + X - 1)
