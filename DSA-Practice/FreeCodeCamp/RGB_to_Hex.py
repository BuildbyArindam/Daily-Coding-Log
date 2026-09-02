"""
Problem: RGB to Hex
Platform: FreeCodeCamp (Daily Coding Challenge)
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/09-02
Date Solved: 2026-09-02
Difficulty: Easy
Topics: String Manipulation, Parsing, Number Base Conversion (Hex)

Approach:
Strip the "rgb(" prefix and trailing ")" from the input string, split
the remaining string on commas to get the three color components,
convert each to an int, then format each as a 2-digit zero-padded
hex value and concatenate with a leading "#".

Time Complexity: O(1) — fixed-size input (always 3 components)
Space Complexity: O(1) — fixed-size output string
"""


# ----------------------- Solution ---------------------------


def rgb_to_hex(rgb):
    values = rgb[4:-1].split(",")
    r = int(values[0].strip())
    g = int(values[1].strip())
    b = int(values[2].strip())
    return f"#{r:02x}{g:02x}{b:02x}"
