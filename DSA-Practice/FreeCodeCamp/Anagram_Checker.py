"""
Problem: Anagram Checker
Platform: FreeCodeCamp - Daily Coding Challenge
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/08-16
Date Solved: 2026-08-30
Difficulty: Easy
Topic: String Manipulation, Sorting, Hashing/frequency-counting

Approach:
Normalize both strings by stripping spaces and lowercasing, then compare
their sorted character sequences. Two strings are anagrams if and only if
they contain the same characters with the same frequencies, which sorting
reveals directly.

Time Complexity: O(n log n) - dominated by sorting each string
Space Complexity: O(n) - sorted() returns new lists for each string
"""


# ------------------------- Solution --------------------------------


def are_anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    return sorted(str1) == sorted(str2)
