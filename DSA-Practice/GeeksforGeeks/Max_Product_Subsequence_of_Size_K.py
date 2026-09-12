"""
Problem: Max Product Subsequence of Size K
Platform: GeeksforGeeks
Link: https://www.geeksforgeeks.org/problems/maximum-product4633/1
Date: 2026-09-12
Difficulty: Medium
Topic: Arrays

Approach:
Sort the array. The max product subsequence of size k is built from the
extremes of the sorted array (largest values, and/or pairs of the most
negative values, since two negatives multiply positive). Handle k=1 and
odd k as special cases (pick the largest single element first if k is odd
and the max is non-negative; otherwise take the k smallest since all are
non-positive). For the remaining even count, greedily compare the product
of the next two largest vs next two smallest and take whichever pair
contributes more, moving pointers inward from both ends.

Time Complexity: O(n log n) — dominated by the sort; the two-pointer scan is O(k).
Space Complexity: O(1) extra space (sort is in-place; no auxiliary structures).
"""


# ------------------------ Solution -----------------------------------


class Solution:
    def maxProduct(self, arr: list[int], k: int) -> int:
        # code here
        arr.sort()
        n = len(arr)
        if k == 1:
            return arr[-1]
        if k % 2 == 1:
            if arr[-1] <= 0:
                product = 1
                for i in range(n - k, n):
                    product *= arr[i]
                return product
            product = arr[-1]
            right = n - 2
            left = 0
            k -= 1
        else:
            product = 1
            left = 0
            right = n - 1
        while k > 0:
            left_product = arr[left] * arr[left + 1]
            right_product = arr[right - 1] * arr[right]
            if left_product > right_product:
                product *= left_product
                left += 2
            else:
                product *= right_product
                right -= 2
            k -= 2
        return product
