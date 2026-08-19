"""
Problem: Assignment Due
Link: https://www.codechef.com/problems/P1_175/
Platform: CodeChef (Starters 175)
Date Solved: 2026-08-19
Difficulty: Cakewalk (~800 rating)
Topic: Basic Conditionals / I-O

Approach:
Given X (days needed) and Y (days available), the task can be
finished on time iff X <= Y. Direct comparison, no edge cases
beyond standard integer input.

Time Complexity: O(1)
Space Complexity: O(1)
"""


# -------------------- Solution -------------------------


X, Y = map(int, input().split())
if X <= Y:
    print("YES")
else:
    print("NO")
