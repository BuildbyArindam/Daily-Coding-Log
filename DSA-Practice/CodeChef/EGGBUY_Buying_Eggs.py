# Problem: Buying Eggs
# Link: https://www.codechef.com/problems/EGGBUY
# Date: 2026-09-10
# Difficulty: Beginner / Easy
# Topics: Basic Math, Conditional Logic / Greedy Choice, Simulation
# Approach: Compare cost of buying a dozen eggs individually (X per egg) 
#           vs. buying a pre-packed dozen (Y) plus flat delivery fee (F); 
#           take the minimum.
# Time Complexity: O(1)
# Space Complexity: O(1)


# -------------------------- Solution -------------------------------------


X, Y, F = map(int, input().split())
cost1 = X * 12
cost2 = Y * 12 + F
print(min(cost1, cost2))
