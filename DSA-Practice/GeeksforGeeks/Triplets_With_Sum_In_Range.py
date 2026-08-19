"""
Problem   : Triplets with Sum in Range
Platform  : GeeksforGeeks
Link      : https://www.geeksforgeeks.org/problems/triplets-with-sum-with-given-range/1
Difficulty: Medium
Topic     : Sorting
Date      : 2026-08-19

Approach:
Reduce "count triplets with sum in [l, r]" to countLEQ(r) - countLEQ(l-1),
where countLEQ(x) counts triplets with sum <= x. For each fixed index i,
use a two-pointer sweep over the sorted remainder of the array: if
arr[i]+arr[left]+arr[right] <= x, all pairs between left and right also
qualify, so add (right-left) and move left forward; otherwise shrink
from the right.

Time complexity : O(n^2) — sort is O(n log n), dominated by two nested
                   two-pointer passes (each O(n^2)), called twice.
Space complexity: O(1) extra (in-place two-pointer, ignoring sort's own space).
"""


# ------------------------- Solution ---------------------------


class Solution:
    def countTriplets(self, arr: list[int], l: int, r: int) -> int:
        # code here
        def count_leq(x: int) -> int:
            arr.sort()
            n = len(arr)
            count = 0
            for i in range(n - 2):
                left, right = i + 1, n - 1
                while left < right:
                    total = arr[i] + arr[left] + arr[right]
                    if total <= x:
                        count += right - left
                        left += 1
                    else:
                        right -= 1
            return count
        return count_leq(r) - count_leq(l - 1)
