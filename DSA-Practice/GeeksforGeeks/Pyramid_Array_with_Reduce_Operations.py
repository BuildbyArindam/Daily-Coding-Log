"""
Problem   : Pyramid Array with Reduce Operations
Platform  : GeeksforGeeks
Link      : https://www.geeksforgeeks.org/problems/pyramid-form3044/1
Difficulty: Medium
Topics    : Dynamic Programming
Date      : 2026-09-23

Approach:
    A pyramid of height h looks like 1, 2, ..., h, ..., 2, 1 and sums to h^2,
    so the operations needed are sum(arr) - h^2 for the largest feasible h.
    - inc[i]: tallest left slope ending at i, inc[i] = min(arr[i], inc[i-1] + 1)
    - dec[i]: tallest right slope starting at i, dec[i] = min(arr[i], dec[i+1] + 1)
    - A pyramid peaking at i has height min(inc[i], dec[i]);
      take the maximum over all i.

Complexity:
    Time : O(n), three linear passes
    Space: O(n), for the inc and dec arrays
"""


# ---------------------------------------------- Solution -------------------------------------------


class Solution:
    def formPyramid(self, arr):
        # code here 
        n = len(arr)
        total = sum(arr)
        inc = [0] * n
        inc[0] = 1
        for i in range(1, n):
            inc[i] = min(arr[i], inc[i - 1] + 1)
        dec = [0] * n
        dec[n - 1] = 1
        for i in range(n - 2, -1, -1):
            dec[i] = min(arr[i], dec[i + 1] + 1)
        largest = 1
        for i in range(n):
            peak = min(inc[i], dec[i])
            if peak > largest:
                largest = peak
        return total - largest * largest
