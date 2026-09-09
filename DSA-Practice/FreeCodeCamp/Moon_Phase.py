"""
Problem: Moon Phase
Platform: FreeCodeCamp - Daily Coding Challenge (Day 10-09)
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/10-09
Date Solved: 2026-09-09
Difficulty: Easy
Topics: Date/Time Manipulation, Modular Arithmetic

Approach:
    Calculate the number of days elapsed between the input date and a known
    reference "New Moon" date (2000-01-06). Take that value modulo 28 (the
    approximate length of a lunar cycle) to find where in the cycle the given
    date falls, then map that day-in-cycle to one of four phases: New,
    Waxing, Full, or Waning (each spanning a 7-day block).

Time Complexity:  O(1) - constant-time date subtraction and arithmetic
Space Complexity: O(1) - no auxiliary data structures used
"""


# ------------------------- Solution ---------------------------------


from datetime import datetime

def moon_phase(date_string):
    date = datetime.strptime(date_string, "%Y-%m-%d")
    reference_date = datetime(2000, 1, 6)
    days_passed = (date - reference_date).days
    cycle_day = (days_passed % 28) + 1
    if 1 <= cycle_day <= 7:
        return "New"
    elif 8 <= cycle_day <= 14:
        return "Waxing"
    elif 15 <= cycle_day <= 21:
        return "Full"
    else:
        return "Waning"
