"""
Problem   : Rectangle and Square (RECSQ)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/RECSQ
Date      : 2026-08-21
Difficulty: Cakewalk (Beginner)
Topics    : Basic Math, Conditionals

Approach:
Given a rectangle A x B and a square of side C, compare their areas.
Print "Yes" if area(rectangle) == area(square), else "No".

Time Complexity : O(1)
Space Complexity: O(1)
"""


# ------------------------ Solution ---------------------------


A, B, C = map(int, input().split())

if A * B == C * C:
    print("Yes")
else:
    print("No")
