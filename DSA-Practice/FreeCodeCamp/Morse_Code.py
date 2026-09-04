"""
Problem: Morse Code
Platform: FreeCodeCamp — Daily Coding Challenge (07-31)
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/07-31
Date Solved: 2026-09-04
Difficulty: Easy
Topics: String Manipulation, Hashing, Dictionary Lookup, Parsing

Approach:
    Build a static Morse-to-letter lookup dictionary. Split the input
    on triple spaces ("   ") to separate words, then split each word
    on single spaces to get individual letter codes. Map each code to
    its letter via the dictionary and join to rebuild words, then join
    words with a single space.

Time Complexity:  O(n) — n = total length of the code string
                   (each character is processed once across splits/joins)
Space Complexity: O(n) — for the decoded output and intermediate lists
"""


# ------------------------ Solution --------------------------------------


def decode_morse(code):
    morse = {
        ".-": "A", "-...": "B", "-.-.": "C", "-..": "D",
        ".": "E", "..-.": "F", "--.": "G", "....": "H",
        "..": "I", ".---": "J", "-.-": "K", ".-..": "L",
        "--": "M", "-.": "N", "---": "O", ".--.": "P",
        "--.-": "Q", ".-.": "R", "...": "S", "-": "T",
        "..-": "U", "...-": "V", ".--": "W", "-..-": "X",
        "-.--": "Y", "--..": "Z"
    }
    words = code.split("   ")
    decoded_words = []
    for word in words:
        letters = word.split(" ")
        decoded_word = "".join(morse[letter] for letter in letters)
        decoded_words.append(decoded_word)
    return " ".join(decoded_words)
