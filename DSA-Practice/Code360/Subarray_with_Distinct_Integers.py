"""
Problem: Subarray with Distinct Integers
Link: https://www.naukri.com/code360/problems/subarray-with-distinct-integers_893062?kunjiRedirection=true
Platform: Code360
Date Solved: 2026-09-06
Difficulty: Easy
Topics: Sliding Window, Two Pointers, Hashing, Frequency Counting

Approach:
    Count subarrays with EXACTLY `b` distinct integers using the classic
    "exactly(K) = atMost(K) - atMost(K-1)" trick.
    atMostK(k) counts subarrays with AT MOST k distinct integers via a
    sliding window: expand `right`, and whenever the window's distinct
    count exceeds k, shrink from `left` until it's valid again. Each
    valid window of length L contributes L subarrays ending at `right`.

Time Complexity:  O(n)   — each pointer (left, right) traverses the array once per atMostK call, called twice
Space Complexity: O(k)   — frequency map holds at most k distinct keys at a time
"""


# ------------------------ Solution ------------------------------


from os import *
from sys import *
from collections import *
from math import *

def goodSubarrays(arr, n, b):
	def atMostK(k):
		if k <= 0:
			return 0
		freq = {}
		left = 0
		count = 0
		for right in range(n):
			freq[arr[right]] = freq.get(arr[right], 0) + 1
			while len(freq) > k:
				freq[arr[left]] -= 1
				if freq[arr[left]] == 0:
					del freq[arr[left]]
				left += 1
			count += right - left + 1
		return count
	return atMostK(b) - atMostK(b - 1)
