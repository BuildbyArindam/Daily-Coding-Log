"""
Problem: CSV Header Parser
Platform: FreeCodeCamp — Daily Coding Challenge
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/09-28
Date Solved: 2026-09-06
Difficulty: Easy
Topics: String Manipulation, Parsing, List Comprehension

Approach:
Split the input CSV header line on commas, then strip leading/trailing
whitespace from each resulting field to normalize headers that may have
inconsistent spacing (e.g. "name, age , email").

Time Complexity: O(n) — n = length of the input string (one pass to split,
one pass to strip each token)
Space Complexity: O(n) — output list holds all header strings
"""


# ----------------------- Solution ---------------------------


def get_headings(csv):
    return [heading.strip() for heading in csv.split(",")]
