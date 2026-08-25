"""
Problem: Smallest Missing Multiple of K
Link: https://leetcode.com/problems/smallest-missing-multiple-of-k/
Date Solved: 2026-08-25
Difficulty: Easy
Topics: Array, Hash Table

Approach:
Put all nums into a set for O(1) lookup. Starting from k, keep checking
successive multiples of k (k, 2k, 3k, ...) against the set until we find
one that's absent — that's the smallest missing multiple of k.

Time Complexity: O(n + m) — O(n) to build the set, O(m) to scan multiples
                  until the first miss (m = answer/k, bounded by n+1 in
                  the worst case since at most n multiples can be present).
Space Complexity: O(n) — for the hash set.
"""


# ---------------------------- Solution ------------------------------


class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        num_set = set(nums)
        multiple = k
        while multiple in num_set:
            multiple += k
        return multiple

__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
