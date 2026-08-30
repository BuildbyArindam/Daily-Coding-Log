"""
Problem   : Max Sixers (MAX6)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/MAX6
Date      : 2026-08-30
Difficulty: Cakewalk
Topics    : Basic Math, Integer Division, Implementation

Approach:
Each six requires exactly 6 runs. The maximum number of sixes
possible from X runs is simply integer division of X by 6
(remainder runs can't form another six).

Time Complexity : O(1)
Space Complexity: O(1)
"""


# ---------------------- Solution -----------------------------


X = int(input())
print(X // 6)
