"""
Problem: camelCase
Platform: FreeCodeCamp - Daily Coding Challenge (08-25)
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/08-25
Date Solved: 2026-08-30
Difficulty: Easy
Topics: String Manipulation, Parsing, Naming Convention Conversion

Approach:
    Normalize all separators (hyphens and underscores) to spaces, split
    into words, lowercase the first word, and capitalize the first
    letter of every subsequent word before joining them back together.

Time Complexity: O(n) - single pass to replace/split + one pass to build result
Space Complexity: O(n) - storage for the words list and output string
"""


# ------------------------ Solution ---------------------------------


def to_camel_case(s):
    words = s.replace("-", " ").replace("_", " ").split()
    if not words:
        return ""
    return words[0].lower() + "".join(word.capitalize() for word in words[1:])
