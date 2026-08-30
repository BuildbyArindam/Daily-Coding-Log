"""
Problem: Golf Handicap Calculator
Platform: FreeCodeCamp (Daily Coding Challenge)
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/08-04
Date Solved: 2026-08-30
Difficulty: Easy
Topics: Arrays, Basic Math, Averages, Decimal Precision/Rounding

Approach:
Compute the differential (score - par) for each round, then average all
differentials using Decimal arithmetic (instead of float) to avoid binary
floating-point rounding errors. Round the final average to one decimal
place using ROUND_HALF_UP (standard "round half up" behavior, matching
how golf handicaps are conventionally reported).

Time Complexity:  O(n) — single pass to build differentials + O(n) sum
Space Complexity: O(n) — stores the differentials list
"""


# -------------------------- Solution ---------------------------------


from decimal import Decimal, ROUND_HALF_UP

def calculate_handicap(scores, pars):
    differentials = [score - par for score, par in zip(scores, pars)]
    average = Decimal(sum(differentials)) / Decimal(len(differentials))
    return float(average.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP))
