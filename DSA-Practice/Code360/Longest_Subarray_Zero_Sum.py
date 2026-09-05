"""
Problem   : Longest Subarray with Zero Sum
Platform  : Code360 (Naukri)
Link      : https://www.naukri.com/code360/problems/longest-subarray-zero-sum_757507?kunjiRedirection=true
Difficulty: Medium
Topic     : Hashing, Prefix Sum, Arrays
Date      : 2026-09-05

Approach:
    Maintain a running prefix sum while scanning the array. Store the
    first index at which each prefix-sum value occurs in a hashmap
    (seeded with {0: -1} to handle a zero-sum subarray starting at index 0).
    If the same prefix sum reappears at index i, the subarray between
    the first occurrence and i sums to zero — update max_length with
    that span. Only the *first* occurrence of each sum is kept, since
    keeping the earliest start maximizes subarray length.

Time complexity : O(n)  — single pass, O(1) amortized hashmap ops
Space complexity: O(n)  — hashmap can store up to n distinct prefix sums
"""


# ------------------------- Solution --------------------------------------


def lengthOfLongestSubarray(arr, n):
    first_index = {0: -1}
    prefix_sum = 0
    max_length = 0
    for i in range(n):
        prefix_sum += arr[i]
        if prefix_sum in first_index:
            max_length = max(max_length, i - first_index[prefix_sum])
        else:
            first_index[prefix_sum] = i
    return max_length
