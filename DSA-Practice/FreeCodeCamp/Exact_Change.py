"""
Problem: Exact Change
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/07-10
Date Solved: 2026-08-31
Difficulty: Easy-Medium
Topics: Dynamic Programming, Coin Change (Unbounded Knapsack), Combinatorics

Approach:
Bottom-up DP counting the number of ways to make `amount` cents using
unlimited coins of denominations {1, 5, 10, 25}. ways[c] holds the number
of combinations that sum to c. For each coin, update ways[] in increasing
order of amount so each coin can be reused any number of times (unbounded
knapsack pattern), avoiding permutation-based overcounting.

Time Complexity:  O(amount * len(coins)) -> O(4 * amount)
Space Complexity: O(amount)  — the `ways` array
"""


# ---------------------------- Solution -----------------------------


def exact_change(amount):
    ways = [0] * (amount + 1)
    ways[0] = 1
    for coin in [1, 5, 10, 25]:
        for cents in range(coin, amount + 1):
            ways[cents] += ways[cents - coin]
    return ways[amount]
