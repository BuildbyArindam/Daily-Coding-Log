"""
Problem: Lowercase Words
Platform: FreeCodeCamp — Daily Coding Challenge
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/07-06
Date Solved: 2026-08-31
Difficulty: Easy (related: String Manipulation basics)
Topics: String Manipulation, Word Filtering, Basic Programming

Approach:
Split the input string into words, then filter and keep only the
words that are entirely lowercase using str.islower(), and join
them back with spaces.

Time Complexity: O(n) — n = total characters across all words
                  (each word is scanned once by islower(), plus one
                  pass to split and one to join)
Space Complexity: O(n) — storage for the words list and the output string
"""


# -------------------------- Solution ------------------------------


def get_lowercase_words(s):
    words = s.split()
    lowercase_words = []
    for word in words:
        if word.islower():
            lowercase_words.append(word)
    return " ".join(lowercase_words)
