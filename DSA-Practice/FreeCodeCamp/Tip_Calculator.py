"""
Problem: Tip Calculator
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/10-20
Date: 2026-09-10
Difficulty: Easy
Topics: String parsing, type casting, arithmetic, string formatting

Approach:
Strip the "$" and "%" symbols from the input strings, cast to float,
then compute 15%, 20%, and a custom-percent tip off the base meal price.
Return all three as formatted currency strings.

Time Complexity: O(1) — fixed number of arithmetic operations
Space Complexity: O(1) — fixed-size output list
"""


# ------------------------------ Solution ----------------------------------


def calculate_tips(meal_price, custom_tip):
    price = float(meal_price.replace("$", ""))
    custom_percent = float(custom_tip.replace("%", ""))
    tip_15 = price * 0.15
    tip_20 = price * 0.20
    tip_custom = price * (custom_percent / 100)
    return [
        f"${tip_15:.2f}",
        f"${tip_20:.2f}",
        f"${tip_custom:.2f}"
    ]
