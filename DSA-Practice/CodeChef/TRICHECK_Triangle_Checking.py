"""
Problem: Triangle Checking
Link: https://www.codechef.com/problems/TRICHECK
Date: 2026-08-22
Difficulty: Easy (~800)
Topics: Math, Geometry, Implementation

Approach:
Given three side lengths A, B, C, a valid triangle exists iff the sum of
any two sides is strictly greater than the third (triangle inequality).
Check all three conditions simultaneously.

Time Complexity: O(1) — constant number of comparisons
Space Complexity: O(1) — no extra data structures used
"""


# ----------------------------- Solution -------------------------------


A, B, C = map(int, input().split())
if A + B > C and B + C > A and A + C > B:
    print("Yes")
else:
    print("No")
