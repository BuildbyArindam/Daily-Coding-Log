"""
Problem: Bird and Max Fruit Gathering
Platform: GeeksforGeeks
Link: https://www.geeksforgeeks.org/problems/bird-and-maximum-fruit-gathering--170645/1
Date: 2026-09-04
Difficulty: Easy
Topic: Arrays / Sliding Window (Circular)

Approach:
A bird can start at any index and eats fruit from m consecutive trees,
wrapping around the array circularly. Use a fixed-size sliding window of
length m over the circular array: initialize the window sum for the first
m elements, then slide it one position at a time (subtracting the element
leaving the window, adding the element entering via circular indexing
(start + m - 1) % n), tracking the maximum sum seen.

Time Complexity: O(n)  — single pass sliding the window across all n starts
Space Complexity: O(1) — only window_sum and max_sum are tracked
"""


# ------------------------ Solution --------------------------------


class Solution:
    def maxFruits(self, arr: list[int], m: int) -> int:
        """ code here """
        n = len(arr)
        if m == n:
            return sum(arr)
        window_sum = sum(arr[:m])
        max_sum = window_sum
        for start in range(1, n):
            window_sum -= arr[start - 1]
            window_sum += arr[(start + m - 1) % n]
            max_sum = max(max_sum, window_sum)
        return max_sum
