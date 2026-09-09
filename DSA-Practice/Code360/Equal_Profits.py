"""
Problem: Equal Profits
Platform: Code360 (Naukri)
Link: https://www.naukri.com/code360/problems/equal-profits_3839601?kunjiRedirection=true
Difficulty: Medium
Topics: Hashing, Arrays, Prefix-Sum Technique
Date Solved: 2026-09-09

Approach:
Define profit[i] = cost[i] - (i + 1). Two indices i < j form a valid
pair iff cost[j] - cost[i] == j - i, which rearranges to
profit[i] == profit[j]. So the problem reduces to counting pairs of
equal values in the profit array. Use a hashmap to track frequency of
each profit value seen so far; for each index, add its current
frequency to the answer, then increment it.

Time Complexity: O(n)   -- single pass, O(1) hashmap ops
Space Complexity: O(n)  -- hashmap can hold up to n distinct profit values
"""


# ------------------------- Solution -----------------------------------


from os import *
from sys import *
from collections import *
from math import *
from typing import *
from builtins import open

def numberOfPairs(n: int, cost: List[int]) -> int:
    freq = defaultdict(int)
    pairs = 0
    for i in range(n):
        profit = cost[i] - (i + 1)
        pairs += freq[profit]
        freq[profit] += 1
    return pairs
