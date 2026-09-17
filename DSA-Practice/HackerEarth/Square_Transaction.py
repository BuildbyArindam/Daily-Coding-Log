"""
Problem: Square Transaction
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/square-transaction-20/
Date: 2026-09-17
Difficulty: Easy
Topics: Binary Search, Sorting, Algorithms

Approach:
Build a prefix-sum array of transaction amounts (monotonically increasing
since amounts are presumably non-negative). For each query, binary search
(bisect_left) for the first prefix sum >= target and return its 1-indexed
position; if no such prefix exists, return -1.

Time Complexity:  O((T + Q) log T)  — O(T) to build prefix sums, O(log T) per query
Space Complexity: O(T)              — prefix sum array
"""


# ------------------------------- Solution -----------------------------------------------


import sys
from bisect import bisect_left
input = sys.stdin.readline
T = int(input())
transactions = list(map(int, input().split()))
prefix = []
total = 0
for amount in transactions:
    total += amount
    prefix.append(total)
Q = int(input())
out = []
for _ in range(Q):
    target = int(input())
    pos = bisect_left(prefix, target)
    if pos < T:
        out.append(str(pos + 1)) 
    else:
        out.append("-1")
sys.stdout.write("\n".join(out))
