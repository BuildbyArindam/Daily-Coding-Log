"""
Problem: Fill The Tank
Platform: FreeCodeCamp — Daily Coding Challenge (09-18)
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/09-18
Date Solved: 2026-09-06
Difficulty: Easy
Topics: Basic Math / Arithmetic, Implementation, String Formatting

Approach:
    Compute the remaining capacity of the tank (tank_size - fuel_level),
    multiply by the price per gallon to get total refill cost, and format
    the result as a currency string rounded to 2 decimal places.

Time Complexity: O(1) — constant arithmetic operations, no loops/recursion.
Space Complexity: O(1) — only a fixed number of scalar variables used.
"""


# ------------------------ Solution -----------------------------


def cost_to_fill(tank_size, fuel_level, price_per_gallon):
    gallons_needed = tank_size - fuel_level
    cost = gallons_needed * price_per_gallon
    return f"${cost:.2f}"
