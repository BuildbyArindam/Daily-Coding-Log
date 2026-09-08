"""
Problem   : Movie Snacks (MOVPR)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/MOVPR
Date      : 2026-09-08
Difficulty: Cakewalk / Easy
Topics    : Basic Math, Greedy, Conditional Statements, Implementation

Approach:
Three combo prices are given (X = 1 popcorn, Y = 1 drink, Z = combo of
popcorn+drink). Answer = minimum cost to get 2 popcorns and 3 drinks,
choosing among:
  - 2 separate popcorns + 3 separate drinks           -> 2X + 3Y
  - 1 combo (covers 1 popcorn+1 drink) + 1 popcorn + 2 drinks -> Z + X + 2Y
  - 2 combos (covers 2 popcorn+2 drink) + 1 drink      -> 2Z + Y
Take the min of the three.

Time complexity : O(1)
Space complexity: O(1)
"""


# ---------------------- Solution --------------------------


X, Y, Z = map(int, input().split())
ans = min(
    2 * X + 3 * Y, 
    Z + X + 2 * Y, 
    2 * Z + Y     
)
print(ans)
