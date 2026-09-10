"""
Problem: 24 to 12
Platform: FreeCodeCamp (Daily Coding Challenge)
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/10-13
Date Solved: 2026-09-10
Difficulty: Easy
Topics: Strings, Conditionals/Branching, Time Formatting & Parsing

Approach:
    Parse the hour and minute from the 24-hour "HHMM" string.
    Handle three cases:
        - hour == 0  -> 12 AM (midnight)
        - hour < 12  -> same hour, AM
        - hour == 12 -> 12 PM (noon)
        - hour > 12  -> subtract 12, PM
    Return formatted "H:MM AM/PM" string.

Time Complexity:  O(1) - fixed-length input, constant operations
Space Complexity: O(1) - no extra data structures used
"""


# ------------------------ Solution --------------------------------------


def to_12(time):
    hour = int(time[:2])
    minute = time[2:]
    if hour == 0:
        hour = 12
        period = "AM"
    elif hour < 12:
        period = "AM"
    elif hour == 12:
        period = "PM"
    else:
        hour -= 12
        period = "PM"
    return f"{hour}:{minute} {period}"
