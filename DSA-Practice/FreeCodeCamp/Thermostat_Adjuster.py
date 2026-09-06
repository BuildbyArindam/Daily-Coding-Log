"""
Problem: Thermostat Adjuster
Platform: FreeCodeCamp - Daily Coding Challenge
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/09-15
Date Solved: 2026-09-06

Difficulty: Easy
Topics: Conditional Logic, Basic Programming, Simulation

Approach:
Compare current temp to target temp and return the corresponding
thermostat action - "heat" if below target, "cool" if above,
"hold" if equal. Straightforward if-elif-else branching, no
edge cases beyond the three comparison outcomes.

Time Complexity: O(1) - constant number of comparisons
Space Complexity: O(1) - no extra data structures used
"""


# ---------------------- Solution ------------------------------


def adjust_thermostat(temp, target):
    if temp < target:
        return "heat"
    elif temp > target:
        return "cool"
    else:
        return "hold"
