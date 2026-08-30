"""
Problem: Spoken Duration
Platform: FreeCodeCamp Daily Coding Challenge (08-05)
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/08-05
Date Solved: 2026-08-30

Approach:
Convert total seconds into hours, minutes, and seconds using integer
division and modulo. Build a list of non-zero unit strings (with correct
singular/plural form), then join them into a natural-language phrase
with commas and a trailing "and".

Time Complexity: O(1) — fixed number of arithmetic ops and at most 3 parts
Space Complexity: O(1) — output size bounded by 3 parts
"""


# ----------------------------- Solution ---------------------------------


def get_spoken_duration(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    parts = []
    if hours:
        parts.append(f"{hours} hour" if hours == 1 else f"{hours} hours")
    if minutes:
        parts.append(f"{minutes} minute" if minutes == 1 else f"{minutes} minutes")
    if seconds:
        parts.append(f"{seconds} second" if seconds == 1 else f"{seconds} seconds")
    if len(parts) == 1:
        return parts[0]
    elif len(parts) == 2:
        return f"{parts[0]} and {parts[1]}"
    else:
        return f"{parts[0]}, {parts[1]} and {parts[2]}"
