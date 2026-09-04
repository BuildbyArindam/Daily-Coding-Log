"""
Problem: Word Blender
Platform: FreeCodeCamp — Daily Coding Challenge
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/07-21
Date Solved: 2026-09-04
Difficulty: Easy
Topics: String Manipulation / Slicing

Approach:
Take the first half of word1 (using integer division, so odd-length
words round down) and the second half of word2 (rounding down means
the "extra" middle character on odd-length word2 goes to the second
half). Concatenate the two slices to form the blended word.

Time Complexity: O(n + m) — slicing and concatenating both words
Space Complexity: O(n + m) — new string created for the result
"""


# ------------------------- Solution ----------------------------


def blend_words(word1, word2):
    first_half = word1[: len(word1) // 2]
    second_half = word2[len(word2) // 2 :]
    return first_half + second_half
