"""
Problem: Exoplanet Search
Platform: FreeCodeCamp (Daily Coding Challenge)
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/10-05
Date Solved: 2026-09-09
Difficulty: Easy–Medium 
Topics: Arrays/Strings, Math (mean/average), Encoding/Base conversion, Threshold detection

Approach:
    Convert each character in `readings` to a numeric intensity value
    (digits 0-9 map directly, letters A-Z map to 10-35, similar to hex
    digit expansion). Compute the average intensity across all readings,
    then flag a possible exoplanet if any single reading dips to 80% or
    below the average (simulating a brightness dip caused by a transit).

Time Complexity: O(n) - one pass to build `values`, O(n) for sum(),
                  O(n) for the `any()` scan -> overall linear in n.
Space Complexity: O(n) - the `values` list holds one entry per reading.
"""


# -------------------------- Solution ------------------------------------


def has_exoplanet(readings):
    values = [int(char) if char.isdigit() else ord(char) - ord('A') + 10 for char in readings]
    average = sum(values) / len(values)
    return any(value <= average * 0.8 for value in values)
