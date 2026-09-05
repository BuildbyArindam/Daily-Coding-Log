"""
Problem   : IPv4 Validator
Platform  : FreeCodeCamp — Daily Coding Challenge
Link      : https://www.freecodecamp.org/learn/daily-coding-challenge/09-05
Date      : 2026-09-05
Difficulty: Easy
Topics: String Manipulation, Parsing, Validation

Approach:
    Split the input string on ".". A valid IPv4 address must have exactly
    4 parts. Each part must be a non-negative integer with no leading
    zeros (unless the part is exactly "0"), and its value must be
    between 0 and 255 inclusive.

Time complexity : O(1) — at most 4 parts, each bounded to a few digits
Space complexity: O(1) — fixed-size list from split
"""


# ---------------------------------- Solution ----------------------------------------


def is_valid_ipv4(ipv4):
    parts = ipv4.split(".")
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit():
            return False
        if len(part) > 1 and part[0] == "0":
            return False
        if int(part) > 255:
            return False
    return True
