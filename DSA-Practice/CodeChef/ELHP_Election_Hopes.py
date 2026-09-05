"""
Problem: Election Hopes
Platform: CodeChef
Link: https://www.codechef.com/problems/ELHP
Date Solved: 2026-09-05
Difficulty: Cakewalk
Topics: Basic Math, Greedy, Conditional Statements

Approach:
    X's current votes must be at least double Y's remaining votes
    for X to be guaranteed a win regardless of how votes split.
    Directly compare X against 2*Y and print the result.

Time Complexity: O(1)
Space Complexity: O(1)
"""


# ----------------------- Solution -----------------------------


X, Y = map(int, input().split())
if X >= 2 * Y:
    print("Yes")
else:
    print("No")
