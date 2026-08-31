"""
Problem: IOI 2024
Platform: CodeChef
Link: https://www.codechef.com/problems/IOI2024
Date Solved: 2026-08-31
Difficulty: Cakewalk
Topics: Basic I/O, Conditional Statements, Implementation

Approach:
Given a date X (day of September), print "YES" if IOI is ongoing
(1 <= X <= 8), else print "NO". Simple range check, no algorithmic
complexity beyond a conditional.

Time Complexity: O(1) per test case
Space Complexity: O(1)
"""


# ------------------------- Solution ----------------------------


x = int(input())
if 1 <= x <= 8:
    print("YES")
else:
    print("NO")
