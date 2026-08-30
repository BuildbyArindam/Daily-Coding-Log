"""
Problem: Mile Pace
Platform: FreeCodeCamp - Daily Coding Challenge (08-21)
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/08-21
Date: 2026-08-30
Difficulty: Easy
Topics: Math, String Manipulation, Parsing

Approach:
Parse the "MM:SS" duration string into total seconds, divide by the
number of miles to get seconds-per-mile, round to the nearest second,
then convert that back into a "MM:SS" formatted pace string.

Time Complexity: O(1) — fixed number of arithmetic/string operations
Space Complexity: O(1) — no extra data structures, output size is constant
"""


# -------------------------- Solution --------------------------------


def mile_pace(miles, duration):
    minutes, seconds = map(int, duration.split(":"))
    total_seconds = minutes * 60 + seconds
    pace_seconds = total_seconds / miles
    pace_seconds = round(pace_seconds)
    pace_minutes = pace_seconds // 60
    pace_remaining_seconds = pace_seconds % 60
    return f"{pace_minutes:02d}:{pace_remaining_seconds:02d}"
