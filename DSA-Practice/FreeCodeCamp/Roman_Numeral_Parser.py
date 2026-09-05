"""
Problem   : Roman Numeral Parser
Platform  : FreeCodeCamp (Daily Coding Challenge)
Link      : https://www.freecodecamp.org/learn/daily-coding-challenge/09-07
Date      : 2026-09-05
Difficulty: Easy-Medium
Topics: String Manipulation, Hashing/Dictionary Lookup, Number Base Conversion

Approach:
    Iterate left to right, mapping each symbol to its integer value.
    If the current symbol's value is less than the next symbol's value,
    it's a subtractive pair (e.g., IV, IX, XL) — subtract it. Otherwise,
    add it normally. This handles all standard Roman numeral cases in
    a single linear pass without needing to pre-process substrings.

Time Complexity  : O(n) — single pass over the numeral string
Space Complexity : O(1) — fixed-size lookup dict, no extra data structures
"""


# ----------------------- Solution --------------------------------


def parse_roman_numeral(numeral):
    values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    total = 0
    for i in range(len(numeral)):
        if i + 1 < len(numeral) and values[numeral[i]] < values[numeral[i + 1]]:
            total -= values[numeral[i]]
        else:
            total += values[numeral[i]]
    return total
