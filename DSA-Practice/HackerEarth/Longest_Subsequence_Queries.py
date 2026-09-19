"""
Problem   : Longest Subsequence Queries
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/longest-subsequence-queries-9c45a765/
Date      : 2026-09-19
Difficulty: Easy
Topics    : Binary Search, Algorithms

Approach:
Sort the array once, then build a prefix-sum array. For each query k,
binary search (bisect_left) for the position of the smallest prefix sum
that is >= k. The answer is (position - 1), i.e. the count of smallest
elements whose sum stays below k — the longest valid subsequence length.

Time Complexity : O(n log n + q log n) per test case
Space Complexity: O(n) for the prefix-sum array
"""


# -------------------------------------- Solution ------------------------------------------------


import sys
from bisect import bisect_left
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + a[i]
    for _ in range(q):
        k = int(input())
        pos = bisect_left(prefix, k)
        print(pos - 1)
