"""
Problem   : Pet Age Calculator
Platform  : FreeCodeCamp - Daily Coding Challenge
Link      : https://www.freecodecamp.org/learn/daily-coding-challenge/07-14
Date      : 2026-09-02
Difficulty: Easy
Topics    : Hashing, Dictionary Lookup, Conditional Logic

Approach:
Map each pet species to its human-year multiplier in a dict, then
multiply the pet's age by the looked-up multiplier and return the result.

Time Complexity : O(1) — single dict lookup and multiplication
Space Complexity: O(1) — fixed-size dict, no growth with input
"""


# ------------------------- Solution ----------------------------------


def pet_years(pet, age):
    multipliers = {
        "dog": 7,
        "cat": 6,
        "rabbit": 8,
        "hamster": 30,
        "guinea pig": 12,
        "goldfish": 6,
        "bird": 5
    }
    return age * multipliers[pet]
