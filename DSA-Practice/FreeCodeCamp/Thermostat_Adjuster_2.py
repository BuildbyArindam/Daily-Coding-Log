"""
Problem: Thermostat Adjuster 2
Platform: FreeCodeCamp - Daily Coding Challenge
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/10-21
Date Solved: 2026-09-10
Difficulty: Easy
Topics: Conditionals, Temperature Conversion, Basic Arithmetic

Approach:
Convert the target Celsius temperature to Fahrenheit using the
standard formula (C * 1.8 + 32), then compare it against the
current Fahrenheit reading. Return "Heat" if the room needs to
warm up, "Cool" if it needs to cool down, or "Hold" if already
at target — including the temperature difference rounded to 1
decimal place in the Heat/Cool cases.

Time Complexity: O(1) - fixed number of arithmetic ops and comparisons
Space Complexity: O(1) - no extra data structures used
"""


# --------------------------- Solution --------------------------------


def adjust_thermostat(current_f, target_c):
    target_f = (target_c * 1.8) + 32
    if current_f < target_f:
        difference = round(target_f - current_f, 1)
        return f"Heat: {difference:.1f} degrees Fahrenheit"
    elif current_f > target_f:
        difference = round(current_f - target_f, 1)
        return f"Cool: {difference:.1f} degrees Fahrenheit"
    else:
        return "Hold"
