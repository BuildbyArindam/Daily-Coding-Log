"""
Problem: Longest Matching in Dictionary with Removals
Platform: GeeksforGeeks
Link: https://www.geeksforgeeks.org/problems/find-largest-word-in-dictionary2430/1
Difficulty: Medium
Topics: Strings
Date Solved: 2026-09-22

Approach:
For each character in s, precompute the sorted list of indices where it
occurs (26 buckets). For each candidate word in the dictionary, greedily
match characters against s using binary search (bisect_right) to find the
next valid index strictly after the previous match — this checks subsequence
validity without scanning s repeatedly. Among all words that are valid
subsequences of s, pick the longest; break ties by lexicographically
smallest.

Time Complexity: O(n + sum(len(word) for word in d) * log n)
    - n = len(s) to build the position buckets
    - each character lookup is a binary search over at most n indices
Space Complexity: O(n) for the 26 position buckets
"""


# -------------------------------------------- Solution ----------------------------------------------------


from bisect import bisect_right

class Solution:
    def findLongestWord(self, s: str, d: list) -> str:
        # code here
        positions = [[] for _ in range(26)]
        for i, ch in enumerate(s):
            positions[ord(ch) - ord('a')].append(i)
        ans = ""
        for word in d:
            prev = -1
            possible = True
            for ch in word:
                arr = positions[ord(ch) - ord('a')]
                idx = bisect_right(arr, prev)
                if idx == len(arr):
                    possible = False
                    break
                prev = arr[idx]
            if possible:
                if len(word) > len(ans) or (
                    len(word) == len(ans) and word < ans
                ):
                    ans = word
        return ans
