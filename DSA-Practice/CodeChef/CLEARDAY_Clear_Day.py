"""
Problem   : Clear Day (CLEARDAY)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/CLEARDAY
Date      : 2026-09-02
Difficulty: Cakewalk (rating ~500)
Topics    : Basic Math, Conditional Statements, Implementation

Approach:
A week has 7 days. Given X rainy days and Y cloudy days, the
remaining days must be clear. Answer is simply 7 - X - Y.

Time Complexity : O(1)
Space Complexity: O(1)
"""


# ------------------------ Solution ----------------------------


X, Y = map(int, input().split())
clear_days = 7 - X - Y
print(clear_days)
