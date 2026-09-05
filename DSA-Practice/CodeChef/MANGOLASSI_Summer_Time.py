"""
Problem: Summer Time
Platform: CodeChef
Link: https://www.codechef.com/problems/MANGOLASSI
Date Solved: 2026-09-05
Difficulty: Cakewalk
Topics: Basic Math, Conditional Statements, Implementation

Approach:
Read temperature X. If X exceeds 35°C, it's considered "Summer" (YES),
otherwise it's not (NO). Straightforward threshold comparison.

Time Complexity: O(1)
Space Complexity: O(1)
"""


# ----------------------- Solution -----------------------------


X = int(input())
if X > 35:
    print("YES")
else:
    print("NO")
