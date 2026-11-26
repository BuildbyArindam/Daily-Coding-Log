"""
Problem   : Range Vowel Count Queries
Platform  : GeeksforGeeks
Link      : https://www.geeksforgeeks.org/problems/range-vowel-count-queries-static/1
Difficulty: Medium
Topics    : Prefix Sum, Strings
Date      : 2026-11-26

Approach  : Build a prefix-sum array where running[i] holds the number of
            vowels in s[0..i-1]. Each query [lo, hi] (inclusive) is then
            answered in O(1) as running[hi + 1] - running[lo].

Time      : O(n + q) -> O(n) to build the prefix array, O(1) per query
Space     : O(n)     -> prefix array (excluding the output list)
"""


# ------------------------------------------- Solution ---------------------------------------------------------


class Solution:
    def countVowels(self, s: str, queries: list[list[int]]) -> list[int]:
        # code here
        vowel_bank = frozenset("aeiou")
        total_len = len(s)
        running = [0] * (total_len + 1)
        for pos, ch in enumerate(s):
            running[pos + 1] = running[pos] + (ch in vowel_bank)
        return [running[hi + 1] - running[lo] for lo, hi in queries]
