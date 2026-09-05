"""
Problem   : Phone Number Formatter
Platform  : FreeCodeCamp — Daily Coding Challenge (09-30)
Link      : https://www.freecodecamp.org/learn/daily-coding-challenge/09-30
Date      : 2026-09-05
Difficulty: Easy
Topics    : String Manipulation, Slicing, Formatting

Approach:
    Treat the input as a fixed 11-digit string: 1 country-code digit
    followed by a 10-digit US-style number. Slice it into
    country code (index 0), area code (1:4), exchange (4:7), and
    line number (7:), then assemble with an f-string into
    "+C (AAA) EEE-LLLL" format.

Complexity:
    Time  : O(n) — n = len(number), single pass via slicing/f-string
    Space : O(n) — new formatted string of comparable length
"""


# ---------------------- Solution --------------------------------------


def format_number(number):
    return f"+{number[0]} ({number[1:4]}) {number[4:7]}-{number[7:]}"
