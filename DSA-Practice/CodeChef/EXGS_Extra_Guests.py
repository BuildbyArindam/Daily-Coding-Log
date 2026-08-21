"""
Problem: Extra Guests (EXGS)
Platform: CodeChef (Starters 236)
Link: https://www.codechef.com/problems/EXGS
Date Solved: 2026-08-21

Approach:
    X guests were expected, Y guests actually arrived (X < Y).
    X plates were already ordered at Rs.100/plate.
    The extra (Y - X) plates ordered later cost Rs.150/plate.
    Total cost = X*100 + (Y-X)*150.
    Pure O(1) arithmetic, no loops or data structures needed.

Time Complexity:  O(1)
Space Complexity: O(1)
"""


# -------------------- Solution -------------------------


X, Y = map(int, input().split())
total_cost = X * 100 + (Y - X) * 150
print(total_cost)
