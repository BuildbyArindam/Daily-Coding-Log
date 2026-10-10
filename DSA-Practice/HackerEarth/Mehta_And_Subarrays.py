"""
Problem : Mehta And Subarrays
Platform: HackerEarth
Link    : https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/mehta-and-subarrays/
Date    : 2026-10-10
Difficulty: Medium
Topics  : Binary Search, Sorting, Fenwick Tree, Prefix Sums

Approach:
    Build prefix sums so a subarray (i, j] has sum prefix[j] - prefix[i].
    A subarray is valid when prefix[i] <= prefix[j]. For each j, find the
    earliest index i < j whose prefix value is <= prefix[j]. Coordinate-compress
    the prefix values and keep a Fenwick tree (BIT) over the ranks that stores
    the minimum index seen for each rank prefix. That gives the longest valid
    subarray ending at j. Track the global max length and how many end positions
    achieve it (one subarray per end position, so this counts distinct subarrays).
    Print -1 if no valid subarray exists.

Complexity:
    Time : O(n log n) - sorting/compression plus BIT update and query per index
    Space: O(n)       - prefix array, compressed values, BIT
"""


# -------------------------------------------- Solution ----------------------------------------------------------


import sys
from bisect import bisect_right

data = list(map(int, sys.stdin.buffer.read().split()))
n = data[0]
arr = data[1:n + 1]
prefix = [0] * (n + 1)
for i in range(n):
    prefix[i + 1] = prefix[i] + arr[i]

values = sorted(set(prefix))
m = len(values)
first = {}
for i, s in enumerate(prefix):
    if s not in first:
        first[s] = i

INF = n + 1
bit = [INF] * (m + 1)

def update(i, value):
    while i <= m:
        bit[i] = min(bit[i], value)
        i += i & -i

def query(i):
    result = INF
    while i > 0:
        result = min(result, bit[i])
        i -= i & -i
    return result

max_len = 0
count = 0

for j, s in enumerate(prefix):
    pos = bisect_right(values, s)
    earliest = query(pos)
    if earliest != INF:
        length = j - earliest
        if length > 0:
            if length > max_len:
                max_len = length
                count = 1
            elif length == max_len:
                count += 1
    update(bisect_right(values, s), j)

if max_len == 0:
    print(-1)
else:
    print(max_len, count)
