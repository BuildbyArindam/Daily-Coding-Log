"""
Problem   : Xsquare And Number List
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/xsquare-and-number-list/
Difficulty: Medium
Topics    : Binary Search, Sorting, Implementation, Combinatorics
Date      : 2026-10-08

Approach:
    A query "op K" asks about subsets by their maximum element. Sort S once,
    then use binary search to get:
        c_lt = number of elements < K   (bisect_left)
        c_le = number of elements <= K  (bisect_right)
    Using precomputed powers of 2 (mod 1e9+7):
        '<' : 2^c_lt                  (every chosen element is < K)
        '>' : 2^N - 2^c_le            (all subsets minus those with every element <= K)
        '=' : 2^c_le - 2^c_lt         (all elements <= K, minus all elements < K)

Time Complexity : O(N log N + Q log N)  -> sort + one binary search pair per query
Space Complexity: O(N)                  -> sorted list + powers-of-2 table
"""


# --------------------------------------- Solution -----------------------------------------------


import sys
from bisect import bisect_left, bisect_right

MOD = 1000000007
input = sys.stdin.buffer.readline
N, Q = map(int, input().split())
S = list(map(int, input().split()))
S.sort()
powers = [1] * (N + 1)
for i in range(1, N + 1):
    powers[i] = (powers[i - 1] * 2) % MOD
total = powers[N]
out = []
for _ in range(Q):
    parts = input().split()
    op = parts[0]
    K = int(parts[1])
    c_lt = bisect_left(S, K)
    c_le = bisect_right(S, K)
    if op == b'<':
        ans = powers[c_lt]
    elif op == b'>':
        ans = (total - powers[c_le]) % MOD
    else:  
        ans = (powers[c_le] - powers[c_lt]) % MOD
    out.append(str(ans))
sys.stdout.write('\n'.join(out))
