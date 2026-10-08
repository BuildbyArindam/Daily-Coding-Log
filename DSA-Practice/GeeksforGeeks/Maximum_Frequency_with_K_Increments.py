"""
Problem   : Maximum Frequency with K Increments
Platform  : GeeksforGeeks
Link      : https://www.geeksforgeeks.org/problems/maximum-frequency-1662528911/1
Difficulty: Medium
Topics    : Sliding Window, Sorting
Date      : 2026-10-08

Approach:
    Sort the array, then use a sliding window. For a window [left, right],
    the best target value is arr[right], the largest element in the window.
    Raising every element to that value costs
        arr[right] * window_size - window_sum
    If the cost exceeds k, shrink the window from the left until it fits.
    The answer is the largest valid window size seen.

Complexity:
    Time : O(n log n), dominated by sorting; the two-pointer pass is O(n)
    Space: O(1) extra, ignoring the sort's internal space
"""


# ---------------------------------------------- Solution --------------------------------------------------------


class Solution:
    def maxFrequency(self, arr, k):
        # code here
        arr.sort()
        left = 0
        total = 0
        ans = 1
        for right in range(len(arr)):
            total += arr[right]
            while arr[right] * (right - left + 1) - total > k:
                total -= arr[left]
                left += 1
            ans = max(ans, right - left + 1)
        return ans
