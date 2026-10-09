"""
Problem   : Minimum Operations to Reach n
Platform  : GeeksforGeeks
Link      : https://www.geeksforgeeks.org/problems/find-optimum-operation4504/1
Date      : 2026-10-09
Difficulty: Easy
Topics    : Dynamic Programming, Greedy, Bit Manipulation

Approach  : Start from 0 and reach n using "add 1" or "multiply by 2".
            Work backwards from n: halve when even, subtract 1 when odd.
            In binary, each set bit costs one "+1" and each shift costs one
            "x2". The first set bit is created by a "+1" with no doubling
            before it, so the total is:
                (number of bits - 1) doublings + (number of set bits) increments
                = bits + ones - 1

Time      : O(log n), one pass over the bits of n
Space     : O(1)
"""


# ---------------------------------------------- Solution ---------------------------------------------------------


class Solution:
    def minOperation(self, n):
        # code here
        bits = 0
        ones = 0
        while n > 0:
            bits += 1
            ones += n & 1
            n >>= 1
        return bits + ones - 1
