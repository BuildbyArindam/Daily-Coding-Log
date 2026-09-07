"""
Problem: Longest Contiguous Subarray With Absolute Diff Bounded by a Limit
Platform: Code360 (Naukri)
Link: https://www.naukri.com/code360/problems/longest-contiguous-subarray-with-absolute-diff-bounded-by-a-limit_977250
Difficulty: Easy
Date Solved: 2026-09-07
Topic: Sliding Window / Two Pointers / Monotonic Deque

Approach:
Maintain two monotonic deques over the current window [left, right] —
a decreasing deque (max_dq) for the window max and an increasing deque
(min_dq) for the window min. Expand `right` one step at a time, pushing
into both deques while popping from the back any indices whose values
are dominated by arr[right]. If the current window's max - min exceeds
`limit`, shrink from the left (popping front indices from either deque
if they equal `left`) until the constraint holds again. Track the best
window length seen.

Time Complexity: O(n) — each index is pushed/popped from each deque at most once
Space Complexity: O(n) — worst case both deques hold up to n indices
"""


# -------------------------- Solution ---------------------------------


from os import *
from sys import *
from collections import *
from math import *
from builtins import open

def getLongestSubarray(arr, limit):
	max_dq = deque()
	min_dq = deque()
	left = 0
	ans = 0
	for right in range(len(arr)):
		while max_dq and arr[max_dq[-1]] < arr[right]:
			max_dq.pop()
		max_dq.append(right)
		while min_dq and arr[min_dq[-1]] > arr[right]:
			min_dq.pop()
		min_dq.append(right)
		while arr[max_dq[0]] - arr[min_dq[0]] > limit:
			if max_dq[0] == left:
				max_dq.popleft()
			if min_dq[0] == left:
				min_dq.popleft()
			left += 1
		ans = max(ans, right - left + 1)
	return ans
