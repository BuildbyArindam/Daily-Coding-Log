"""
Problem: Slug Generator
Platform: FreeCodeCamp - Daily Coding Challenge (09-17)
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/09-17
Date Solved: 2026-09-06
Difficulty: Easy
Topics: String Manipulation, Regular Expressions, Parsing, URL Encoding

Approach:
    1. Lowercase the input string.
    2. Strip out any character that isn't a lowercase letter, digit, or space.
    3. Collapse repeated spaces into a single space.
    4. Trim leading/trailing whitespace.
    5. Replace remaining spaces with '%20' to produce a URL-safe slug.

Time Complexity:  O(n) - each regex pass and replace scans the string once.
Space Complexity: O(n) - new string created at each transformation step.
"""


# ---------------------- Solution -------------------------------


import re
def generate_slug(str):
    str = str.lower()
    str = re.sub(r'[^a-z0-9 ]', '', str)
    str = re.sub(r' +', ' ', str)
    str = str.strip()
    str = str.replace(' ', '%20')
    return str
