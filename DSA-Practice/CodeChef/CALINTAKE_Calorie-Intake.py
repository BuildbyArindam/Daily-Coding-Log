"""
Problem: Calorie Intake
Platform: CodeChef
Link: https://www.codechef.com/problems/CALINTAKE
Date: 2026-09-05
Difficulty: Cakewalk
Topics: Basic Math, Conditional Statements, Implementation

Approach:
Given daily calorie limit X, and Y meals of Z calories each,
compute total calories eaten (Y*Z). If it exceeds the limit X,
print -1 (limit exceeded). Otherwise, print the remaining
calorie allowance (X - calories_eaten).

Time Complexity: O(1) — constant-time arithmetic and comparison
Space Complexity: O(1) — no extra data structures used
"""


# -------------------------- Solution -----------------------------------


X, Y, Z = map(int, input().split())
calories_eaten = Y * Z
if calories_eaten > X:
    print(-1)
else:
    print(X - calories_eaten)
