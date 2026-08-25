"""
Problem: Minimum Moves to Sort Permutation
Platform: GeeksforGeeks
Link: https://www.geeksforgeeks.org/problems/morning-assembly3038/1
Date: 2026-08-25
Difficulty: Easy
Topics: Hash, Dynamic Programming, Arrays

Approach:
Build a position array `pos` where pos[v] = index of value v in arr.
A permutation is "sorted" in the required sense along any stretch of
consecutive values v, v+1, v+2, ... that also appear in increasing
index order in arr (i.e., pos[v] < pos[v+1]). Track the longest such
run of consecutive values using a simple running-length scan (1D DP:
current[x] depends only on current[x-1]). The minimum moves needed is
n minus the length of this longest run, since every element outside
the run must be moved.

Time Complexity: O(n) — one pass to build pos, one pass to scan runs
Space Complexity: O(n) — for the pos array
"""


# ----------------------- Solution ----------------------------


class Solution:
    def minMoves(self, arr):
        n = len(arr)
        pos = [0] * (n + 1)
        for i, value in enumerate(arr):
            pos[value] = i
        longest = 1
        current = 1
        for x in range(1, n):
            if pos[x] < pos[x + 1]:
                current += 1
            else:
                current = 1
            longest = max(longest, current)
        return n - longest
