"""
Problem   : Sort the Array
Platform  : Code360 (Naukri)
Link      : https://www.naukri.com/code360/problems/sort-the-array_3849867?kunjiRedirection=true
Date      : 2026-08-29
Difficulty: Hard
Topics    : Hashing, Greedy, Interval Scheduling / Merging

Approach:
For each distinct value, record its first and last index of occurrence.
Sort distinct values. A "chain" of values can stay in place (already sorted)
as long as each next value's first occurrence starts after the previous
value's last occurrence ends (last[prev] < first[curr]) — i.e. their index
ranges don't overlap. Find the longest such chain via a linear scan; the
answer is (number of distinct values - longest chain), since every value
outside the longest non-overlapping chain must be removed/relocated to
make the array sortable by value blocks.

Time complexity : O(N log N)  — dominated by sorting the distinct values
Space complexity: O(N)        — first/last hashmaps + values list
"""


# ----------------------------- Solution -------------------------------------


from sys import *
from collections import *
from math import *
from typing import *

def sortArray(N: int, A: List[int]) -> int:
    first = {}
    last = {}
    for i, x in enumerate(A):
        if x not in first:
            first[x] = i
        last[x] = i
    values = sorted(first)
    longest = 1
    current = 1
    for i in range(1, len(values)):
        prev = values[i - 1]
        curr = values[i]
        if last[prev] < first[curr]:
            current += 1
        else:
            current = 1
        longest = max(longest, current)
    return len(values) - longest
