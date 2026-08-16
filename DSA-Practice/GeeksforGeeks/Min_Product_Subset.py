"""
Problem   : Min Product Subset
Platform  : GeeksforGeeks
Link      : https://www.geeksforgeeks.org/problems/max-and-min-products3347/1
Difficulty: Medium
Topic     : Arrays
Date      : 2026-08-16

Approach:
- Single pass over arr, tracking:
  - product of all non-zero elements
  - count of negative elements
  - the negative element closest to zero (largest_neg)
  - whether a zero exists
- If negative count is odd -> full product is already the minimum (most negative).
- If negative count is even and > 0 -> divide out largest_neg to flip sign,
  giving the most negative possible product.
- If no negatives and a zero exists -> 0 is the minimum.
- If no negatives and no zero -> minimum is the smallest single positive element.

Time Complexity : O(n)
Space Complexity: O(1)
"""


# ----------------------- Solution --------------------------


class Solution:
    def minProd(self, arr):
        product = 1
        neg_count = 0
        largest_neg = -11
        zero = False
        has_positive = False
        for x in arr:
            if x == 0:
                zero = True
            else:
                product *= x
                if x < 0:
                    neg_count += 1
                    largest_neg = max(largest_neg, x)
                else:
                    has_positive = True
        if neg_count % 2 == 1:
            return product
        if neg_count > 0:
            return product // largest_neg
        if zero:
            return 0
        return min(arr)
