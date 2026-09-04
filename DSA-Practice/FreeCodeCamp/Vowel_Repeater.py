"""
Problem: Vowel Repeater
Platform: FreeCodeCamp - Daily Coding Challenge
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/09-04
Date Solved: 2026-09-04
Difficulty: Easy
Topics: String Manipulation, Character Counting, Frequency Counting

Approach:
Iterate through the string once. Keep a running count of vowels seen
so far (case-insensitive). Whenever a vowel is hit, append it followed
by (count - 1) lowercase repeats of itself, so each successive vowel
repeats one more time than the last. Non-vowel characters pass through
unchanged.

Time Complexity: O(n) per character scanned, but O(k^2) overall in the
worst case (all/most characters are vowels), since each vowel append
grows with the running count. O(n) when vowels are sparse.
Space Complexity: O(n) to O(k^2) worst case, matching the output length.
"""


# -------------------------- Solution --------------------------------


def repeat_vowels(s):
    vowels = "aeiouAEIOU"
    result = ""
    count = 0
    for char in s:
        if char in vowels:
            count += 1
            result += char + char.lower() * (count - 1)
        else:
            result += char
    return result
