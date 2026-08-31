"""
Problem: Kaprekar's Routine
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/07-04
Date Solved: 2026-08-31
Difficulty: Easy-Medium
Topics: Math, String Manipulation, Simulation, Number Theory (Kaprekar's Constant)

Approach:
Repeatedly rearrange the digits of a 4-digit number to form the largest and
smallest permutations, subtract (smallest from largest), and count the number
of iterations until the result reaches the Kaprekar constant 6174. All 4-digit
numbers with at least two distinct digits are known to converge to 6174 within
at most 7 iterations.

Time Complexity: O(1) — at most ~7 iterations, each doing O(1) work on a
                  fixed-length (4-digit) string.
Space Complexity: O(1) — fixed-size digit buffers only.
"""


# -------------------------- Solution ------------------------------


def kaprekar(n):
    count = 0
    while n != 6174:
        digits = f"{n:04d}"
        largest = int("".join(sorted(digits, reverse=True)))
        smallest = int("".join(sorted(digits)))
        n = largest - smallest
        count += 1
    return count
