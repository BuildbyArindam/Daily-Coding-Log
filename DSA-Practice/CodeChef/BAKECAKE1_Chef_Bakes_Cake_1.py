"""
Problem   : Chef Bakes Cake 1
Platform  : CodeChef
Link      : https://www.codechef.com/problems/BAKECAKE1
Date      : 2026-08-24
Difficulty: Beginner / Easy
Topics    : Math, Implementation

Approach:
Chef spends 30 per cake baked (N cakes) and earns 50 per cake sold (M cakes).
Profit = Revenue - Cost = (M * 50) - (N * 30). Direct formula, no loops needed.

Time Complexity : O(1)
Space Complexity: O(1)
"""


# --------------------- Solution ------------------------


N, M = map(int, input().split())
total_cost = N * 30
total_revenue = M * 50
total_money_made = total_revenue - total_cost
print(total_money_made)
