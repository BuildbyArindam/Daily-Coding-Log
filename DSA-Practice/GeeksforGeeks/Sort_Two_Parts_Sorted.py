# Problem: Sort Two Parts Sorted
# Link: https://www.geeksforgeeks.org/problems/sort-the-half-sorted2157/1
# Platform: GeeksforGeeks 
# Difficulty: Easy
# Date: 2026-10-11
# Topics: Two Pointers, Sorting
#
# Approach:
#   The array is made of two already-sorted parts. Python's built-in sort
#   (Timsort) detects existing sorted runs and merges them, so this is
#   effectively one merge pass over the two parts.
#   (Manual alternative: two-pointer merge into a temp array.)
#
# Time Complexity:  O(n) in practice for two sorted runs (O(n log n) worst case)
# Space Complexity: O(n) auxiliary for the merge step


# ---------------------------------------- Solution ---------------------------------------------------------


class Solution:
    def mergeTwoParts(self, arr):
        arr.sort()
        return arr
