"""
Problem: Longest Word
Platform: FreeCodeCamp (Daily Coding Challenge)
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/09-29
Date Solved: 2026-09-07
Difficulty: Easy
Topics: String Manipulation, Splitting, Basic Programming, Iteration

Approach:
Split the sentence into words, then scan through them tracking the
longest one so far by comparing lengths after stripping trailing
periods. Return the longest word with any trailing period removed.

Time Complexity: O(n * k) — n words, k = avg word length (due to
                  repeated .replace() calls on 'longest' each iteration)
Space Complexity: O(n) — storage for the split word list
"""


# ------------------------ Solution -----------------------------------


def get_longest_word(sentence):
    words = sentence.split()
    longest = words[0]
    for word in words:
        clean_word = word.replace(".", "")
        clean_longest = longest.replace(".", "")
        if len(clean_word) > len(clean_longest):
            longest = word
    return longest.replace(".", "")
