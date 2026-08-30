"""
Problem: Jbelmud Text
Platform: FreeCodeCamp — Daily Coding Challenge (08-15)
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/08-15
Date Solved: 2026-08-30
Difficulty: Easy
Topics: String Manipulation, Sorting

Approach:
Split the input into words. For each word longer than 2 characters,
keep the first and last letters fixed and sort the middle letters
alphabetically, then rejoin. Words of length <= 2 are left unchanged.

Time Complexity: O(n * k log k) — n words, k = avg word length (sorting dominates)
Space Complexity: O(n * k) — result list and joined middle strings
"""


# ------------------------- Solution -------------------------------


def jbelmu(text):
    words = text.split()
    result = []
    for word in words:
        if len(word) <= 2:
            result.append(word)
        else:
            first = word[0]
            last = word[-1]
            middle = ''.join(sorted(word[1:-1]))
            result.append(first + middle + last)
    return ' '.join(result)
