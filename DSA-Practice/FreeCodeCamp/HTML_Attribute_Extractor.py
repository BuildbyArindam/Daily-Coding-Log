"""
Problem: HTML Attribute Extractor
Platform: FreeCodeCamp
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/10-19
Date: 2026-09-10
Difficulty: Easy
Topics: String Manipulation, Regex, Parsing

Approach:
Use regex to find all key="value" pairs inside an HTML tag string.
Pattern (\w+)="([^"]*)" captures the attribute name and its quoted value,
then formats each match as "name, value".

Time Complexity: O(n) — regex scan is linear in the length of the input string
Space Complexity: O(k) — k = number of attributes found, for storing matches/results
"""


# ------------------------ Solution ---------------------------------------


import re
def extract_attributes(element):
    attributes = re.findall(r'(\w+)="([^"]*)"', element)
    return [f"{attribute}, {value}" for attribute, value in attributes]
