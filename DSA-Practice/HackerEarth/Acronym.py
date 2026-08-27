"""
Problem: Acronym
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/acronym-2/
Date: 2026-08-27
Difficulty: Easy
Topics: Ad-Hoc, Approved, Open, String Manipulation

Approach:
    Read K disliked words into a set for O(1) lookup, then read N sentence
    words. For each sentence word not present in the disliked set, take its
    first character (uppercased) and join them with '.' to form the acronym.

Time Complexity:  O(K + N) — building the disliked set is O(K), scanning
                   the sentence and building the acronym is O(N).
Space Complexity: O(K + N) — set of disliked words plus the output list.
"""


# ------------------------- Solution --------------------------------


import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    k = int(input_data[0])
    idx = 1
    disliked_words = set(input_data[idx:idx + k])
    idx += k
    n = int(input_data[idx])
    idx += 1
    sentence_words = input_data[idx:idx + n]
    acronym_letters = [
        word[0].upper() 
        for word in sentence_words 
        if word not in disliked_words
    ]
    print('.'.join(acronym_letters))

if __name__ == '__main__':
    solve()
