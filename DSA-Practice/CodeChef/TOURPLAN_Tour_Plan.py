"""
Problem   : Tour Plan
Platform  : CodeChef
Link      : https://www.codechef.com/problems/TOURPLAN
Date      : 2026-08-23

Approach:
    A tour package covers the first 50 days for a fixed cost `x`.
    Any day beyond day 50 costs an extra `y` per day.
    - If total days z <= 50   -> cost is just the flat package price x
    - If total days z > 50    -> cost is x plus (z - 50) extra days at rate y

Time complexity  : O(1)  — single conditional check, no loops
Space complexity : O(1)  — only a few scalar variables
"""


# ------------------------- Solution -------------------------


x, y, z = map(int, input().split())
if z <= 50:
    total_cost = x
else:
    total_cost = x + (z - 50) * y
print(total_cost)
