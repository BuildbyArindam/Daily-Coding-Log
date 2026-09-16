# Problem: Dominant Pairs
# Platform: GeeksforGeeks
# Link: https://www.geeksforgeeks.org/problems/dominant-pairs/1
# Date: 2026-09-16
# Difficulty: Easy 
# Topic: two-pointer-algorithm, Sorting
#
# Approach:
# - Split the array into left and right halves.
# - Build a frequency array + prefix sums for the right half.
# - For each element in the left half, count right-half elements
#   satisfying arr[i] >= 5 * arr[j] using prefix sums.
#
# Time: O(n + V), where V = 20001 (value range)
# Space: O(V)


# ------------------------------- Solution -----------------------------------------


class Solution:
    def dominantPairs(self, arr: list[int]) -> int:
        # code here
        n = len(arr)
        m = n // 2
        OFFSET = 10000
        SIZE = 20001
        freq = [0] * SIZE
        for i in range(m, n):
            freq[arr[i] + OFFSET] += 1
        for i in range(1, SIZE):
            freq[i] += freq[i - 1]
        ans = 0
        for i in range(m):
            limit = arr[i] // 5
            if limit < -10000:
                continue
            if limit >= 10000:
                ans += m
            else:
                ans += freq[limit + OFFSET]
        return ans
