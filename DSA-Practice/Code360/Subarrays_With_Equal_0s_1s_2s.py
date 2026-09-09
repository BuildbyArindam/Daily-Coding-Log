"""
Problem   : Subarrays With Equal 0's, 1's and 2's
Platform  : Code360 (Naukri)
Link      : https://www.naukri.com/code360/problems/subarrays-with-equal-0-s-1-s-and-2-s_2825370
Difficulty: Hard
Date      : 2026-09-09
Topics    : Arrays, Hashing, Prefix Sum

Approach:
    For a subarray to have equal counts of 0s, 1s, and 2s, the running
    differences (count0 - count1) and (count1 - count2) at the end of the
    subarray must match the differences at its start. So we track the pair
    of prefix differences (count0 - count1, count1 - count2) as we scan the
    array, and use a hash map to count how many times each pair-state has
    occurred before. Every time we see a repeated state, all those earlier
    positions form a valid subarray ending at the current index.

Time Complexity  : O(n)  -> single pass, O(1) hashmap ops
Space Complexity : O(n)  -> hashmap can hold up to O(n) distinct states
"""


# ----------------------- Solution ------------------------------------


from os import *
from sys import *
from collections import *
from math import *
from typing import List

def countSubarrays(n: int, arr: List[int]) -> int:
    freq = defaultdict(int)
    freq[(0, 0)] = 1
    count0 = 0
    count1 = 0
    count2 = 0
    ans = 0
    for x in arr:
        if x == 0:
            count0 += 1
        elif x == 1:
            count1 += 1
        else:
            count2 += 1
        state = (count0 - count1, count1 - count2)
        ans += freq[state]
        freq[state] += 1
    return ans
