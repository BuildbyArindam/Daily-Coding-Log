"""
Problem: Pangram
Platform: FreeCodeCamp — Daily Coding Challenge
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/09-03
Date Solved: 2026-09-04
Difficulty: Easy
Topics: String Manipulation, Hashing, Sets

Approach:
Build a set of lowercase alphabetic characters from the sentence,
then compare it against the given set of required letters. If the
two sets are equal, the sentence is a pangram (uses every one of
the given letters exactly, with no missing ones).

Time Complexity: O(n) — n = len(sentence), one pass to build the set
Space Complexity: O(1) — bounded by alphabet size (set holds at most 26 chars)
"""


# -------------------------- Solution -------------------------------


def is_pangram(sentence, letters):
    sentence_letters = set(c.lower() for c in sentence if c.isalpha())
    return sentence_letters == set(letters)
