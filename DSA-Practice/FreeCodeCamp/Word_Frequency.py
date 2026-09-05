"""
Problem: Word Frequency
Platform: FreeCodeCamp - Daily Coding Challenge
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/09-14
Date Solved: 2026-09-05
Difficulty: Easy-Medium
Topics: String Manipulation, Hashing/Dictionary, Frequency Counting, Sorting

Approach:
Lowercase the paragraph and strip basic punctuation (",", ".", "!"),
then split into words. Count occurrences with a dict, tracking each
word's first-seen index to break ties in original order. Sort words
by (-count, first_seen_index) and return the top 3.

Time Complexity: O(n log n) — n = number of words (dominated by the sort;
                  counting itself is O(n))
Space Complexity: O(n) — for the words list, counts dict, and first_seen dict
"""


# ---------------------- Solution ----------------------------------


def get_words(paragraph):
    paragraph = paragraph.lower()
    paragraph = paragraph.replace(",", "").replace(".", "").replace("!", "")
    words = paragraph.split()
    counts = {}
    first_seen = {}
    for i, word in enumerate(words):
        if word not in counts:
            counts[word] = 0
            first_seen[word] = i
        counts[word] += 1
    sorted_words = sorted(
        counts,
        key=lambda word: (-counts[word], first_seen[word])
    )
    return sorted_words[:3]
