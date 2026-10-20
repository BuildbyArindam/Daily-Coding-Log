"""
Problem   : Largest with Same Parity Adjacent Swaps
Platform  : GeeksforGeeks
Link      : https://www.geeksforgeeks.org/problems/even-swap/1
Difficulty: Medium
Topics    : Arrays, Sorting
Date      : 2026-10-20

Approach:
    Adjacent elements can only be swapped when they share the same parity, so an
    element can never cross an element of opposite parity. This splits the array
    into maximal runs of same-parity elements, and each run can be rearranged
    freely. To get the lexicographically largest array, sort each run in
    descending order.

Complexity:
    Time  : O(n log n) worst case (sorting the runs; the scan itself is O(n))
    Space : O(n) worst case for the temporary sorted slices
            (the input array is modified in place)
"""


# --------------------------------------------- Solution -------------------------------------------------------


class Solution:
    def lexicographicallyLargest(self, arr: list[int]) -> list[int]:
        # code here
        n = len(arr)
        i = 0
        while i < n:
            j = i
            while j < n and arr[j] % 2 == arr[i] % 2:
                j += 1
            arr[i:j] = sorted(arr[i:j], reverse=True)
            i = j
        return arr
