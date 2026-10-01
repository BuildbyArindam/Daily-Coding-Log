"""
Problem   : The Monk and Kundan
Platform  : HackerEarth (Codemonk)
Link      : https://www.hackerearth.com/practice/codemonk/9/1483402/
Difficulty: Easy
Topics    : Strings, Implementation
Date      : 2026-10-01

Approach:
    Each character has a fixed value equal to its index in the custom
    ordering "a-z", "1-0", "A-Z". For every word, add (position of the
    character in the word + its index in the ordering) for each
    character. Sum this over all words, then multiply by the number of
    words to get the answer.

Complexity:
    Time  : O(L) per test case, where L is the total number of characters.
            str.index() scans at most 62 chars, so it is a constant factor.
    Space : O(1) extra, apart from the input words.
"""


# ------------------------------------ Solution ------------------------------------------------


initial = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
T = int(input())
for _ in range(T):
    strings = input().split()
    total = 0
    for s in strings:
        for i, ch in enumerate(s):
            total += i + initial.index(ch)
    answer = total * len(strings)
    print(answer)
