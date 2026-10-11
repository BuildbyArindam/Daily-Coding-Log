"""
Problem   : Starting Game development
Platform  : HackerEarth 
Link      : https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/starting-game-development/
Date      : 2026-10-11
Difficulty: Medium
Topics    : Binary Search, Sorting

Approach  : Each of the N rows holds M level thresholds in sorted order.
            For a query, bisect_right on row i with strength[i] gives how many
            levels that attribute can clear. The player is limited by the weakest
            attribute, so the answer is the minimum count across all N rows.

Time      : O(N*M) to read input + O(Q * N * log M) to answer queries
Space     : O(N*M) for the stored level tables
"""


# ----------------------------------------------- Solution -------------------------------------------------------


import sys
from bisect import bisect_right

input = sys.stdin.readline
N, M, Q = map(int, input().split())
levels = []
for _ in range(N):
    levels.append(list(map(int, input().split())))
for _ in range(Q):
    strength = list(map(int, input().split()))
    ans = M
    for i in range(N):
        level = bisect_right(levels[i], strength[i])
        ans = min(ans, level)
    print(ans)
