"""
Problem: Sweets Shop
Platform: CodeChef
Link: https://www.codechef.com/problems/SWEETSHOP
Date: 2026-09-06
Difficulty: Cakewalk
Topics: Basic Math, Conditional Statements, Implementation

Approach:
Chef has X rupees and must buy N chocolates at Rs. 10 each first.
Whatever money remains is spent on jalebis at Rs. 20 each — find
how many jalebis Chef can buy (integer division, no partial jalebis).

Time Complexity: O(1)
Space Complexity: O(1)
"""


# ----------------------- Solution -------------------------------


X, N = map(int, input().split())
remaining_money = X - (N * 10)
jalebis = remaining_money // 20
print(jalebis)
