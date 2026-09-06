"""
Problem: File Storage
Platform: FreeCodeCamp — Daily Coding Challenge
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/09-20
Date Solved: 2026-09-06
Difficulty: Easy
Topics: Basic Math, Unit Conversion, Implementation

Approach:
Convert the file size to bytes using a unit lookup table (B/KB/MB → bytes),
convert the drive size from GB to bytes, then floor-divide drive capacity by
file size to get the max number of files that fit.

Time Complexity: O(1) — constant-time dict lookup and arithmetic
Space Complexity: O(1) — fixed-size lookup table, no extra data structures
"""


# ----------------------- Solution ------------------------------


def number_of_files(file_size, file_unit, drive_size_gb):
    unit_to_bytes = {
        "B": 1,
        "KB": 1000,
        "MB": 1000000
    }
    file_size_bytes = file_size * unit_to_bytes[file_unit]
    drive_size_bytes = drive_size_gb * 1000000000
    return int(drive_size_bytes // file_size_bytes)
