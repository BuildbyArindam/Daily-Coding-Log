"""
Problem: S P A C E J A M
Platform: FreeCodeCamp (Daily Coding Challenge, 08-14)
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/08-14
Date: 2026-08-30
Difficulty: Easy 
Topics: String Manipulation, Formatting/Whitespace Handling, Case Conversion

Approach:
Strip all existing spaces from the input string, uppercase every
character, then rejoin the characters with a double space between
each one to produce the "spaced out" formatting.

Time Complexity: O(n) — single pass to strip spaces, single pass to
                  uppercase/join, where n is the length of the string.
Space Complexity: O(n) — new string created for the cleaned/joined output.
"""


# -------------------------- Solution ------------------------------


def space_jam(s):
    s = s.replace(" ", "")
    return "  ".join(s.upper())
