"""
Problem   : Query multiples
Platform  : HackerEarth 
Link      : https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/query-multiples-6cf951be/
Date      : 2026-10-03
Difficulty: Easy
Topics    : Binary Search, Math, Searching

Approach
--------
For each query (i, X), count indices j >= i where arr[j] is a multiple of X.
1. Bucket the 1-based positions of every value (values are bounded by MAX_A).
2. On the first query for a given X, merge the position lists of X, 2X, 3X, ...
   up to MAX_A and sort them. Cache the result per X.
3. Answer each query with binary search: count = len(list) - bisect_left(list, i).

Complexity
----------
Let A = MAX_A = 20000, D = number of distinct X values queried,
m_X = number of array elements divisible by X (m_X <= N).
Time  : O(N + A)               preprocessing
        + sum over distinct X of O(A/X + m_X log m_X)   building each list
        + O(Q log N)           binary search per query
        (sum of A/X over distinct X is at most A ln A, so the scan cost is small)
Space : O(N + A) for the position buckets
        + O(sum of m_X) for the cached lists (worst case O(D * N))
"""


# --------------------------------------- Solution -------------------------------------------------


import sys
from bisect import bisect_left
input = sys.stdin.readline
N, Q = map(int, input().split())
arr = list(map(int, input().split()))
MAX_A = 20000
positions = [[] for _ in range(MAX_A + 1)]
for idx, value in enumerate(arr, start=1):
    positions[value].append(idx)
multiple_positions = {}
answers = []
for _ in range(Q):
    i, X = map(int, input().split())
    if X not in multiple_positions:
        pos_list = []
        for multiple in range(X, MAX_A + 1, X):
            pos_list.extend(positions[multiple])
        pos_list.sort()
        multiple_positions[X] = pos_list
    pos_list = multiple_positions[X]
    answer = len(pos_list) - bisect_left(pos_list, i)
    answers.append(str(answer))
sys.stdout.write("\n".join(answers))
