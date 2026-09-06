"""
Problem   : Photo Storage
Platform  : FreeCodeCamp (Daily Coding Challenge)
Link      : https://www.freecodecamp.org/learn/daily-coding-challenge/09-19
Date      : 2026-09-06
Difficulty: Easy
Topics: Basic Math, Unit Conversion, Implementation

Approach:
    Convert drive capacity from GB to MB (1 GB = 1000 MB), then divide
    by the size of a single photo. Floor the result since a partial
    photo can't be stored.

Time Complexity : O(1)  — single arithmetic expression
Space Complexity: O(1)  — no auxiliary storage
"""


# ------------------------ Solution -----------------------------


def number_of_photos(photo_size_mb, drive_size_gb):
    return int((drive_size_gb * 1000) / photo_size_mb)
