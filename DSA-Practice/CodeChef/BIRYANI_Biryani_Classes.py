"""
Problem: Biryani Classes
Platform: CodeChef
Link: https://www.codechef.com/problems/BIRYANI
Date Solved: 2026-09-06
Difficulty: Cakewalk
Topics: Basic Math, Implementation

Approach:
For each test case, read two integers X and Y and print their product X*Y.
No edge cases beyond standard integer input; straightforward simulation of the
required computation with no additional logic needed.

Time Complexity: O(1) per test case, O(T) overall
Space Complexity: O(1) extra space (excluding input storage)
"""


# ------------------------ Solution -------------------------------


T = int(input())
for _ in range(T):
    X, Y = map(int, input().split())
    print(X * Y)
