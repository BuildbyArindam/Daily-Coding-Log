"""
Problem: Exun and the Pizzas (EXUNPIZZA)
Link: https://www.codechef.com/problems/EXUNPIZZA
Date: 2026-08-24
Difficulty: Cakewalk
Topics: Basic Math, Implementation

Approach:
Chef has N pizzas, K are pre-ordered (given away/reserved), each of the
remaining pizzas sells for R rupees. Revenue is simply the count of
remaining pizzas (N - K) multiplied by the price R.

Time Complexity: O(1) - constant-time arithmetic
Space Complexity: O(1) - no extra data structures
"""


# ------------------ Solution -------------------------


n, k, r = map(int, input().split())
remaining_pizzas = n - k
revenue = remaining_pizzas * r
print(revenue)
