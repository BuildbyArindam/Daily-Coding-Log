"""
Problem   : Longest Subarray Sum Divisible by K
Platform  : GeeksforGeeks
Link      : https://www.geeksforgeeks.org/problems/longest-subarray-with-sum-divisible-by-k1259/1
Difficulty: Medium
Topics    : Prefix Sum, Arrays, Hash
Date      : 2026-11-22

Approach:
    Track the running prefix sum modulo k. If two prefixes have the same
    remainder, the subarray between them has a sum divisible by k. Store
    the first index at which each remainder appears (seeding remainder 0
    at index -1 to cover subarrays starting at index 0) and, at each
    position, take the distance to that first occurrence as a candidate
    length. Keeping only the first occurrence maximizes the length.

Complexity:
    Time : O(n), one pass with O(1) average hash lookups
    Space: O(min(n, k)), at most one entry per distinct remainder
"""


# ---------------------------------------- Solution ---------------------------------------------------------------


class Solution:
	def longestSubarrayDivK(self, arr, k):
	    # code here
		first_seen = {0: -1}
        best = 0
        running = 0
        for pos in range(len(arr)):
            running = (running + arr[pos]) % k
            if running not in first_seen:
                first_seen[running] = pos
                continue
            span = pos - first_seen[running]
            if span > best:
                best = span
        return best
