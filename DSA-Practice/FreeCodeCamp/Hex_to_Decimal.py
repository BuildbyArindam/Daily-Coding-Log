"""
Problem: Hex to Decimal
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/10-11
Date Solved: 2026-09-09
Difficulty: Easy
Topics: Number Systems / Base Conversion, String Manipulation, Math

Approach:
Iterate through each character of the hex string left to right.
Convert each character to its decimal value (digits via int(), letters
via ASCII offset from 'A'), then build the result using Horner's method:
decimal = decimal * 16 + value. This avoids needing pow() or reversing
the string.

Note: assumes uppercase hex digits (A-F). Add digit.upper() if lowercase
input needs to be supported.

Time Complexity: O(n) - single pass through the hex string
Space Complexity: O(1) - only a few scalar variables used
"""


# --------------------------- Solution ----------------------------------


def hex_to_decimal(hex):
    decimal = 0
    for digit in hex:
        if digit.isdigit():
            value = int(digit)
        else:
            value = ord(digit) - ord('A') + 10
        decimal = decimal * 16 + value
    return decimal
