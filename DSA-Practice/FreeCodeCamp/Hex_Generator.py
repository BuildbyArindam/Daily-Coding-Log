"""
Problem: Hex Generator
Platform: FreeCodeCamp — Daily Coding Challenge
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/08-31
Date Solved: 2026-08-31
Difficulty: Easy
Topics: Randomization/Simulation, String Formatting, Conditional Logic

Approach:
Generate a random RGB hex color where a given channel (red/green/blue)
is dominant — i.e., strictly greater than the other two channels.
Pick the dominant value first (1-255), then pick the other two channels
in [0, dominant-1] so the dominance constraint always holds. Retry if
the generated hex matches the last one produced for that color (avoids
immediate repeats), tracked via a function attribute cache.

Time Complexity:  O(1) expected (rejection loop only re-triggers on a
                   repeat collision, which is rare given the value space)
Space Complexity: O(1) — only a small dict keyed by color name
"""


# -------------------------- Solution --------------------------------


import random

def generate_hex(color):
    if color not in ("red", "green", "blue"):
        return "Invalid color"
    if not hasattr(generate_hex, "last_values"):
        generate_hex.last_values = {}
    while True:
        dominant = random.randint(1, 255)
        other1 = random.randint(0, dominant - 1)
        other2 = random.randint(0, dominant - 1)
        if color == "red":
            rgb = (dominant, other1, other2)
        elif color == "green":
            rgb = (other1, dominant, other2)
        else:  
            rgb = (other1, other2, dominant)
        hex_color = f"{rgb[0]:02X}{rgb[1]:02X}{rgb[2]:02X}"
        if generate_hex.last_values.get(color) != hex_color:
            generate_hex.last_values[color] = hex_color
            return hex_color
