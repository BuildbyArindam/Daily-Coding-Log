"""
Problem: Acronym Builder
Platform: FreeCodeCamp (Daily Coding Challenge)
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/09-08
Date Solved: 2026-09-05
Difficulty: Easy
Topics: String Manipulation, Hashing/Set Lookup, Parsing

Approach:
Split the input into words. Build the acronym by taking the first letter
(uppercased) of each word, except words found in a small "ignore" set
(short articles/conjunctions/prepositions) — the first word is always
included even if it appears in the ignore set.

Time Complexity: O(n) — n = total characters in the string (one pass to
split + one pass over the words)
Space Complexity: O(w) — w = number of words, for the split list and
the output string
"""


# ---------------------------- Solution ------------------------------


def build_acronym(s):
    words = s.split()
    ignore = {"a", "for", "an", "and", "by", "of"}
    acronym = ""
    for i, word in enumerate(words):
        if i == 0 or word.lower() not in ignore:
            acronym += word[0].upper()
    return acronym
