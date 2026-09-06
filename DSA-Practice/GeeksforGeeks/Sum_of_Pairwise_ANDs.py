"""
Problem: Sum of Pairwise ANDs
Platform: GeeksforGeeks
Link: https://www.geeksforgeeks.org/problems/sum-of-products5049/1
Difficulty: Medium
Topics: Mathematics, Bit Magic
Date: 2026-09-06

Approach:
For each bit position (0-30), count how many numbers seen so far have
that bit set. When processing a new number x, for every set bit in x,
add bit_count[bit] * (1 << bit) to the answer — this accounts for the
AND contribution of x with every previously-seen number that also has
that bit set. Increment bit_count[bit] afterward. This avoids the
O(n^2) pairwise comparison by aggregating per-bit instead of per-pair.

Time Complexity: O(n * 31) ~ O(n), since bit width is fixed at 31
Space Complexity: O(31) ~ O(1) extra space (excluding input array)
"""


# --------------------------- Solution ----------------------------------


class Solution:
    def pairAndSum(self, arr):
        # code here
        bit_count = [0] * 31
        ans = 0
        for x in arr:
            for bit in range(31):
                if x & (1 << bit):
                    ans += bit_count[bit] * (1 << bit)
                    bit_count[bit] += 1
        return ans
