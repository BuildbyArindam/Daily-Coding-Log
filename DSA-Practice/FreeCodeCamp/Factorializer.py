"""
Problem: Factorializer
Platform: FreeCodeCamp — Daily Coding Challenge (08-18)
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/08-18
Date Solved: 2026-08-30
Difficulty: Easy
Topics: Math, Loops, Iteration

Approach:
Iteratively multiply integers from 1 to n to compute n!.
Handles n=0 correctly since the loop simply doesn't execute (result stays 1).

Time Complexity: O(n) — single loop from 1 to n
Space Complexity: O(1) — only a running product is stored
"""


# ---------------------- Solution ----------------------------


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
