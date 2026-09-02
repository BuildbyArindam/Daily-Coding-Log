"""
Problem: Pig Latin Converter
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/07-16
Platform: FreeCodeCamp Daily Coding Challenge (07-16)
Date: 2026-09-02
Difficulty: Easy
Topics: String Manipulation, Parsing, Conditional Logic

Approach:
Split input into words. For each word, check if it starts with a vowel —
if so, just append "way". Otherwise, find the index of the first vowel,
move the leading consonant cluster to the end, and append "ay".
Preserve the original capitalization of the first letter.

Time Complexity:  O(n) — n = total characters across all words
                   (each word scanned once for its first vowel, plus
                   linear-time slicing/concatenation)
Space Complexity: O(n) — result list + rebuilt strings proportional
                   to input size
"""


# -------------------------- Solution --------------------------------------


def pig_latin(s):
    vowels = "aeiou"
    words = s.split()
    result = []
    for word in words:
        is_upper = word[0].isupper()
        lower_word = word.lower()
        if lower_word[0] in vowels:
            pig_word = lower_word + "way"
        else:
            vowel_index = 0
            while vowel_index < len(lower_word) and lower_word[vowel_index] not in vowels:
                vowel_index += 1
            pig_word = lower_word[vowel_index:] + lower_word[:vowel_index] + "ay"
        if is_upper:
            pig_word = pig_word.capitalize()
        result.append(pig_word)
    return " ".join(result)
