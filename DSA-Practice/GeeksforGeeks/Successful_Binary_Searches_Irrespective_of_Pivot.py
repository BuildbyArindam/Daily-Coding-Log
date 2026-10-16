"""
Problem   : Successful Binary Searches Irrespective of Pivot
Platform  : GeeksforGeeks
Link      : https://www.geeksforgeeks.org/problems/count-always-found/1
Difficulty: Medium
Topics    : Arrays, Constructive Algorithms
Date      : 2026-10-16

Approach:
    An element is found by binary search for any pivot choice only if every
    element to its left is smaller and every element to its right is larger.
    Precompute prefix maximums and suffix minimums, then count indices i where
    prefix_max[i-1] < arr[i] < suffix_min[i+1].

Time Complexity : O(n)  (three linear passes)
Space Complexity: O(n)  (prefix_max and suffix_min arrays)
"""


# -------------------------------------------------- Solution ----------------------------------------------------------


class Solution:
    def countAlwaysFound(self, arr):
        # code here
        n = len(arr)
        prefix_max = [0] * n
        suffix_min = [0] * n
        prefix_max[0] = arr[0]
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i - 1], arr[i])
        suffix_min[n - 1] = arr[n - 1]
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(suffix_min[i + 1], arr[i])
        count = 0
        for i in range(n):
            left_ok = (i == 0 or prefix_max[i - 1] < arr[i])
            right_ok = (i == n - 1 or suffix_min[i + 1] > arr[i])
            if left_ok and right_ok:
                count += 1
        return count
