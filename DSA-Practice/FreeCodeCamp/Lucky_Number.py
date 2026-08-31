"""
Problem: Lucky Number
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/07-01
Date Solved: 2026-08-31
Platform: FreeCodeCamp (Daily Coding Challenge)
Difficulty: Easy-Medium
Topics: String Manipulation, Frequency Counting, Basic Math

Approach:
Split the full name into first/last. Count vowels and consonants in
each part, take the min/max of (vowels, consonants, length) between
the two names, multiply each min-triplet and max-triplet together,
then subtract smaller product from larger. Return 13 if the result
is 0 (per problem's special-case rule).

Time Complexity: O(n) — single pass over each name's characters
Space Complexity: O(1) — only fixed counters used
"""


# --------------------------- Solution ------------------------------------


def get_lucky_number(name):
    first, last = name.split()
    vowels = "aeiouAEIOU"
    first_vowels = sum(1 for ch in first if ch in vowels)
    first_consonants = len(first) - first_vowels
    last_vowels = sum(1 for ch in last if ch in vowels)
    last_consonants = len(last) - last_vowels
    smaller_vowels = min(first_vowels, last_vowels)
    larger_vowels = max(first_vowels, last_vowels)
    smaller_consonants = min(first_consonants, last_consonants)
    larger_consonants = max(first_consonants, last_consonants)
    smaller_length = min(len(first), len(last))
    larger_length = max(len(first), len(last))
    smaller_value = smaller_vowels * smaller_consonants * smaller_length
    larger_value = larger_vowels * larger_consonants * larger_length
    lucky_number = larger_value - smaller_value
    if lucky_number == 0:
        return 13
    return lucky_number
