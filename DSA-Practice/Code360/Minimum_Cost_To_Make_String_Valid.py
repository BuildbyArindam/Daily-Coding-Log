"""
Problem      : Minimum Cost To Make String Valid
Platform     : Code360 (Naukri)
Link         : https://www.naukri.com/code360/problems/minimum-cost-to-make-string-valid_1115770
Difficulty   : Medium
Date Solved  : 2026-08-24
Topics       : Stack, Greedy, String

Approach:
- If the string length is odd, it can never be balanced -> return -1.
- Track a running `balance` (treat '{' as +1, '}' as -1) instead of an
  actual stack, since only the count of unmatched opens matters.
- Whenever balance goes negative, we have an unmatched '}'. Fix it greedily
  by "flipping" it to a '{' (cost += 1) and reset balance to 1, since a
  flipped bracket is now an open one.
- After the scan, any leftover positive balance represents unmatched '{'
  brackets. Each pair of them needs one flip to close ( '{{' -> '{}' costs 1),
  so add balance // 2 to the cost.

Time Complexity  : O(n) — single pass over the string
Space Complexity : O(1) — only counters used, no extra data structure
"""


# ------------------------- Solution ------------------------------


from os import *
from sys import *
from collections import *
from math import *

def findMinimumCost(str):
	# Write your code here.
	n = len(str)
	if n % 2 != 0:
		return -1
	balance = 0
	cost = 0
	for ch in str:
		if ch == '{':
			balance += 1
		else:
			balance -= 1
			if balance < 0:
				cost += 1
				balance = 1
	cost += balance // 2
	return cost
