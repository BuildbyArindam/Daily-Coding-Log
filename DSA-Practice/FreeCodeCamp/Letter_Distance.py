"""
Problem: Letter Distance
Platform: FreeCodeCamp
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/07-26
Date Solved: 2026-09-04
Difficulty: Easy
Topics: String Manipulation, Character Encoding (ord), Modular Arithmetic

Approach:
For each aligned pair of characters from str1 and str2, compute the raw
ASCII/ordinal difference. Since we want "letter distance" on a circular
26-letter alphabet, take the shorter of the direct difference and the
wraparound difference (26 - diff). Sum these minimal distances across
all pairs.

Time Complexity: O(n), where n = min(len(str1), len(str2)) — single pass via zip
Space Complexity: O(1) — only a running total is kept
"""


# --------------------------- Solution -----------------------------------


def letter_distance(str1, str2):
    total = 0
    for a, b in zip(str1, str2):
        diff = abs(ord(a) - ord(b))
        distance = min(diff, 26 - diff)
        total += distance
    return total
