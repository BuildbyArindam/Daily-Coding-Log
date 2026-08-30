"""
Problem: Sum of Squares
Platform: FreeCodeCamp — Daily Coding Challenge
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/08-19
Date Solved: 2026-08-30
Difficulty: Easy
Topics: Math, Formula-based, Number Theory

Approach:
Uses the closed-form sum-of-squares formula 1² + 2² + ... + n² = n(n+1)(2n+1)/6
instead of iterating, giving a constant-time O(1) solution.

Time Complexity: O(1)
Space Complexity: O(1)
"""


# ------------------------ Solution ---------------------------


def sum_of_squares(n):
    return n * (n + 1) * (2 * n + 1) // 6
