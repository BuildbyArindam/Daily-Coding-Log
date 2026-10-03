"""
Problem   : 1160. Find Words That Can Be Formed by Characters
Platform  : LeetCode (Easy)
Link      : https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/
Date      : 2026-10-03
Topics    : Array, Hash Table, String, Counting

Approach  : Count the frequency of each character in `chars`. For every word,
            count its characters and check that no character appears more
            times in the word than it is available in `chars`. If the word
            is "good", add its length to the running total.

Complexity: Time  - O(N + W), where N = len(chars) and W = total characters
                    across all words
            Space - O(1), since each counter holds at most 26 lowercase letters
"""


# ----------------------------------------- Solution -----------------------------------------------


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_count = collections.Counter(chars)
        total_length = 0
        for word in words:
            word_count = collections.Counter(word)
            if all(word_count[char] <= char_count[char] for char in word_count):
                total_length += len(word)

        return total_length
