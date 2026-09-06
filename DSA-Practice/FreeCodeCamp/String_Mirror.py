"""
Problem: String Mirror
Platform: FreeCodeCamp — Daily Coding Challenge
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/09-23
Date Solved: 2026-09-06
Difficulty: Easy
Topics: String Manipulation, Character Filtering, Two-Pointer/Reversal Check, Palindrome-style Comparison

Approach:
    Strip all non-alphabetic characters from both input strings, then check
    whether the cleaned first string, when reversed, equals the cleaned
    second string.

Time Complexity:  O(n + m)  — one pass to clean each string, one pass to reverse
Space Complexity: O(n + m)  — new filtered strings are created for comparison
"""


# ----------------------- Solution ----------------------------


def is_mirror(str1, str2):
    str1 = ''.join(char for char in str1 if char.isalpha())
    str2 = ''.join(char for char in str2 if char.isalpha())
    return str1[::-1] == str2
