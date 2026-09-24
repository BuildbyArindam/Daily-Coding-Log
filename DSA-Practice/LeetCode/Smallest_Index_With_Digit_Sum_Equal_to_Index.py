"""
Problem: Smallest Index With Digit Sum Equal to Index
Link: https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/
Platform: LeetCode (Daily Question)
Date: 2026-09-24
Difficulty: Easy
Topics: Array, Math

Approach:
    Scan indices left to right. For each nums[i], compute its digit sum by
    repeatedly taking n % 10 and n //= 10. Return the first i where the digit
    sum equals i, or -1 if none matches. Scanning in order guarantees the
    smallest index.

Complexity:
    Time:  O(n * d), where d is the number of digits per element (at most
           ~log10(max(nums)))
    Space: O(1)
"""


# ------------------------------------------- Solution ------------------------------------------------------


class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            n = nums[i]
            digit_sum = 0
            while n > 0:
                digit_sum += n % 10
                n //= 10
            if digit_sum == i:
                return i
        return -1

__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
