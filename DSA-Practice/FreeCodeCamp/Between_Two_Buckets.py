"""
Problem: Between Two Buckets
Platform: FreeCodeCamp (Daily Coding Challenge)
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/08-09
Date Solved: 2026-08-30
Difficulty: Easy
Topics: Math / Weighted Average / Implementation

Approach:
Compute the resulting RGB color when two paint buckets are mixed,
weighting each bucket's color by its fullness relative to the
combined total. Each channel is a fullness-weighted average of the
two buckets' corresponding channel, rounded to the nearest integer.

Time Complexity: O(1) - fixed 3 iterations for RGB channels
Space Complexity: O(1) - fixed-size output list
"""


# -------------------------- Solution -------------------------------


def mix_paint(bucket1, bucket2):
    color1 = bucket1["color"]
    color2 = bucket2["color"]
    fullness1 = bucket1["fullness"]
    fullness2 = bucket2["fullness"]
    total = fullness1 + fullness2
    return [
        round((color1[i] * fullness1 + color2[i] * fullness2) / total)
        for i in range(3)
    ]
