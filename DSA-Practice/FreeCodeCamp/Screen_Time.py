"""
Problem: Screen Time
Platform: FreeCodeCamp - Daily Coding Challenge (09-12)
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/09-12
Date Solved: 2026-09-05
Difficulty: Easy‑Medium
Topics: Arrays, Sliding Window, Prefix/Rolling Average, Simulation

Approach:
Check three conditions across a 7-day hours list:
  1. Any single day >= 10 hours -> True
  2. Any 3-day rolling window average >= 8 -> True
  3. Weekly average >= 6 -> True
Return False if none trigger.

Time Complexity: O(n) — single pass + fixed-size (5) window scan
Space Complexity: O(1) auxiliary
"""


# ----------------------- Solution ----------------------------


def too_much_screen_time(hours):
    for day in hours:
        if day >= 10:
            return True
    for i in range(5):
        if sum(hours[i:i+3]) / 3 >= 8:
            return True
    if sum(hours) / 7 >= 6:
        return True
    return False
