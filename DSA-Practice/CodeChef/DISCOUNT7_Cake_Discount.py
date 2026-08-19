"""
Problem   : Cake Discount (DISCOUNT7)
Platform  : CodeChef (Starters 233, Div 2/3/4)
Link      : https://www.codechef.com/problems/DISCOUNT7
Date      : 2026-08-19
Difficulty: Cakewalk / 500 (Beginner)
Topics    : Basic Programming, Conditionals, Implementation

Approach:
  Each cake costs 100. If N >= 5, a 15% discount applies to the
  total (each cake effectively costs 85), otherwise no discount
  and the price stays at 100 per cake. Just a single threshold
  check followed by O(1) arithmetic.

Complexity:
  Time  : O(1)  — single comparison and multiplication
  Space : O(1)  — no extra data structures used
"""


# -------------------- Solution ------------------------


N = int(input())
if N >= 5:
    print(N * 85)
else:
    print(N * 100)
