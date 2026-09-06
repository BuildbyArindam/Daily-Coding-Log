"""
Problem: Perfect Square
Platform: FreeCodeCamp - Daily Coding Challenge (09-24)
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/09-24
Date Solved: 2026-09-06
Difficulty : Easy
Topics : Math, Number Theory, Basic Programming

Approach:
    A number n is a perfect square if it's non-negative and the integer
    square root of n, when squared, equals n back exactly. We compute
    int(n ** 0.5) as a candidate root and verify by squaring it.

Time Complexity:  O(1) - single sqrt computation, no loops
Space Complexity: O(1) - constant extra space
"""


# ---------------------- Solution ----------------------------


def is_perfect_square(n):
    return n >= 0 and int(n ** 0.5) ** 2 == n
