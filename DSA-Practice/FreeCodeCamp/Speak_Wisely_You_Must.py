"""
Problem: Speak Wisely, You Must
Platform: FreeCodeCamp (Daily Coding Challenge #10-22)
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/10-22
Date Solved: 2026-09-11

Difficulty: Medium 
Topics: Strings, String Manipulation, Parsing

Approach:
    Scan the words for the first occurrence of a Yoda-style keyword
    ("have", "must", "are", "will", "can"). Everything up to and including
    that keyword becomes the trailing clause (lowercased); everything after
    it becomes the leading clause (capitalized). Trailing punctuation is
    stripped before reordering and reattached at the end.

Time Complexity:  O(n) — n = number of words; single pass plus O(n) slicing/joining
Space Complexity: O(n) — new lists created for words, first_part, second_part
"""


# -------------------------------- Solution ------------------------------


def wise_speak(sentence):
    words = sentence.split()
    keywords = {"have", "must", "are", "will", "can"}
    for i, word in enumerate(words):
        if word.rstrip(".,!?;:") in keywords:
            punctuation = ""
            if words[-1][-1] in ".,!?;:":
                punctuation = words[-1][-1]
                words[-1] = words[-1][:-1]
            first_part = words[:i + 1]
            second_part = words[i + 1:]
            first_part = [word.lower() for word in first_part]
            second_part[0] = second_part[0][0].upper() + second_part[0][1:]
            return " ".join(second_part) + ", " + " ".join(first_part) + punctuation
    return sentence
