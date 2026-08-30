"""
Problem: Message Decoder
Platform: FreeCodeCamp (Daily Coding Challenge)
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/08-22
Date Solved: 2026-08-30
Difficulty: Easy
Topics: String Manipulation, Caesar Cipher, Modular Arithmetic

Approach:
Reverse a Caesar cipher shift. For each alphabetic character, shift it
backward by `shift` positions using modular arithmetic (mod 26) to wrap
around the alphabet correctly, preserving original case. Non-alphabetic
characters are copied unchanged.

Time Complexity: O(n) — single pass over the message string
Space Complexity: O(n) — result string grows with input length
"""


# ------------------------ Solution --------------------------------


def decode(message, shift):
    result = ""
    for char in message:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            decoded = chr((ord(char) - start - shift) % 26 + start)
            result += decoded
        else:
            result += char
    return result
