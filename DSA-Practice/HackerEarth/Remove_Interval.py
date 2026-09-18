"""
Problem: Remove Interval
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/optimal-division-d75f0043/
Difficulty: Medium
Topics: Binary Search, Algorithms
Date Solved: 2026-09-18

Approach:
Sort interval start points and end points independently into two arrays.
For each interval (L, R), count how many intervals have their start <= R
(via bisect_right on sorted starts) and how many have their end < L
(via bisect_left on sorted ends). The difference gives the number of
intervals that overlap with (L, R), including itself. Removing all but
one of the overlapping intervals leaves a non-overlapping set, so the
cost of "fixing" around this interval is (overlap_count - 1). Take the
minimum of this cost over all intervals.

Time Complexity: O(N log N)  — sorting + binary search per interval
Space Complexity: O(N)       — separate starts/ends arrays
"""


# ------------------------------- Solution -------------------------------------------


import sys
from bisect import bisect_right, bisect_left
input = sys.stdin.readline
N = int(input())
intervals = []
starts = []
ends = []
for _ in range(N):
    L, R = map(int, input().split())
    intervals.append((L, R))
    starts.append(L)
    ends.append(R)
starts.sort()
ends.sort()
minimum_cost = N
for L, R in intervals:
    count_start = bisect_right(starts, R)
    count_end = bisect_left(ends, L)
    overlap_count = count_start - count_end
    removal_cost = overlap_count - 1
    minimum_cost = min(minimum_cost, removal_cost)
print(minimum_cost)
