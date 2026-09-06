"""
Problem   : Digits vs Letters
Platform  : FreeCodeCamp - Daily Coding Challenge (09-22)
Link      : https://www.freecodecamp.org/learn/daily-coding-challenge/09-22
Date      : 2026-09-06
Difficulty: Easy
Topics    : String Manipulation, Character Classification, Conditional Logic

Approach:
    Single pass over the string, counting digit characters (isdigit)
    and alphabetic characters (isalpha) separately. Compare the two
    counts at the end to decide the winner, or return "tie" if equal.

Time Complexity : O(n)  -> single linear scan over the string
Space Complexity: O(1)  -> only two counters used, no extra data structures
"""


# -------------------- Solution -----------------------


def digits_or_letters(s):
    digits = 0
    letters = 0
    for char in s:
        if char.isdigit():
            digits += 1
        elif char.isalpha():
            letters += 1
    if digits > letters:
        return "digits"
    elif letters > digits:
        return "letters"
    else:
        return "tie"
