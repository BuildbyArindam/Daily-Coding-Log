"""
Problem: Sentence Capitalizer
Platform: FreeCodeCamp (Daily Coding Challenge)
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/09-16
Date Solved: 2026-09-06
Difficulty: Easy
Topics: String Manipulation, Iteration, Conditional Logic

Approach:
Single left-to-right scan over the paragraph, tracking a boolean flag
(`capitalize_next`) that's set whenever a sentence-ending punctuation
mark (. ? !) is seen. The next alphabetic character after such a mark
(or at the very start) gets uppercased; everything else is passed
through unchanged.

Time Complexity: O(n)  — one pass over the string, n = len(paragraph)
Space Complexity: O(n) — result list holds one entry per character
"""


# ---------------------- Solution ---------------------------


def capitalize(paragraph):
    result = []
    capitalize_next = True
    for char in paragraph:
        if capitalize_next and char.isalpha():
            result.append(char.upper())
            capitalize_next = False
        else:
            result.append(char)
        if char in ".?!":
            capitalize_next = True
    return "".join(result)
