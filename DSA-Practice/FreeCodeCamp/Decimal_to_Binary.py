"""
Problem: Decimal to Binary
Platform: FreeCodeCamp - Daily Coding Challenge (10-02)
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/10-02
Date Solved: 2026-09-08
Difficulty: Easy
Topics: Number Base Conversion, String Manipulation, Loops

Approach:
Repeatedly divide the decimal number by 2, prepending each remainder
(0 or 1) to a result string, until the number reduces to 0. This builds
the binary representation from least significant bit to most significant
bit since each remainder is placed at the front.

Time Complexity: O(log n) - number of divisions equals the bit length of n
Space Complexity: O(log n) - for the output binary string
"""


# ---------------------- Solution ------------------------------


def to_binary(decimal):
    binary = ""
    while decimal > 0:
        remainder = decimal % 2
        binary = str(remainder) + binary
        decimal = decimal // 2
    return binary
