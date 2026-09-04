"""
Problem   : Pronic Number
Platform  : FreeCodeCamp — Daily Coding Challenge (07-27)
Link      : https://www.freecodecamp.org/learn/daily-coding-challenge/07-27
Date      : 2026-09-04
Difficulty: Easy
Topics    : Math, Number Theory

Approach:
    A pronic number is a product of two consecutive integers, n = i*(i+1).
    Take the integer square root of n (isqrt), which gives the largest i
    such that i*i <= n. Then just check whether i*(i+1) reconstructs n.
    Negative numbers are never pronic, so they're rejected immediately.

Time Complexity : O(log n)  — isqrt uses a fast integer square-root algorithm
Space Complexity: O(1)
"""


# ------------------------ Solution ----------------------------------


from math import isqrt
def is_pronic(n):
    if n < 0:
        return False
    i = isqrt(n)
    return n == i * (i + 1)
