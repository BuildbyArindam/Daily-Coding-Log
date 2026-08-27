"""
Problem   : Most Frequent Letter (MFRLE)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/MFRLE
Date      : 2026-08-27
Difficulty: Cakewalk / Easy
Topics    : Hashing, Frequency Counting, String Manipulation

Approach:
    Read the entire input, count frequency of each alphabetic
    character (case-insensitive) using collections.Counter.
    Find the maximum frequency, then pick the lexicographically
    smallest character among those with that max frequency.

Complexity:
    Time  : O(N) — N = length of input, single pass to count +
            O(26) to scan the frequency table.
    Space : O(1) — frequency table bounded by 26 lowercase letters.
"""


# ------------------------ Solution --------------------------------


import sys
from collections import Counter

def solve():
    input_data = sys.stdin.read()
    freq = Counter()
    for char in input_data:
        if char.isalpha():
            freq[char.lower()] += 1
    max_count = max(freq.values())
    best_char = min(char for char, count in freq.items() if count == max_count)
    print(best_char)

if __name__ == '__main__':
    solve()
