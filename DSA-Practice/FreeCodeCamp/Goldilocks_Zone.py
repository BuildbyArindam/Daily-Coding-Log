"""
Problem: Goldilocks Zone
Platform: FreeCodeCamp — Daily Coding Challenge
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/10-08
Date Solved: 2026-09-09
Difficulty: Easy
Topics: Math, Formula Implementation

Approach:
    Compute the star's luminosity from its mass using L = M^3.5,
    then derive the inner and outer edges of the habitable
    ("Goldilocks") zone using L^0.5 scaled by the known
    empirical bounds (0.95 and 1.37 AU per unit sqrt-luminosity).

Time Complexity: O(1) — fixed number of arithmetic operations
Space Complexity: O(1) — constant extra space
"""


# ---------------------------- Solution -----------------------------------


def goldilocks_zone(mass):
    luminosity = mass ** 3.5
    start = 0.95 * (luminosity ** 0.5)
    end = 1.37 * (luminosity ** 0.5)
    return [round(start, 2), round(end, 2)]
