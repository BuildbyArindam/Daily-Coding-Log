"""
Problem   : The Corridor Census
Platform  : Unstop
Link      : https://unstop.com/code/practice/661534
Difficulty: Medium
Date      : 2026-10-04
Topics    : Mo's Algorithm, Offline Queries, Sorting, Frequency Counting

Problem   : For each query [l, r], find the maximum frequency of any
            value in a[l..r].

Approach  :
  - Compress values to ids 0..k-1 so freq[] can be a plain list.
  - Process queries offline with Mo's algorithm: block size ~ n / sqrt(q),
    sorted by (block, r), with r alternating direction on odd blocks
    to cut pointer travel.
  - Keep freq[x] (occurrences of x in the window) and count_freq[f]
    (how many values occur exactly f times).
  - Track cur_max: on add it can only rise to the new frequency; on
    remove it drops by at most 1, and only if count_freq[cur_max] hits 0.
    This makes add/remove O(1) with no heap or segment tree.
  - Expand the window before shrinking it so frequencies never go negative.

Complexity:
  Time  : O(n*sqrt(q) + q log q)  (pointer moves + sorting queries)
  Space : O(n + q)
"""


# ------------------------------------ Solution ----------------------------------------------


import sys
from math import isqrt

data = list(map(int, sys.stdin.buffer.read().split()))
it = iter(data)
n = next(it)
q = next(it)
mapping = {}
a = [0] * n
next_id = 0
for i in range(n):
    x = next(it)
    if x not in mapping:
        mapping[x] = next_id
        next_id += 1
    a[i] = mapping[x]
block_size = max(1, n // max(1, isqrt(q)))
queries = []
for idx in range(q):
    l = next(it) - 1
    r = next(it) - 1
    b = l // block_size
    ordered_r = r if (b & 1) == 0 else -r
    queries.append((b, ordered_r, l, r, idx))
queries.sort()
freq = [0] * next_id
count_freq = [0] * (n + 1)
answers = [0] * q
cur_l = 0
cur_r = -1
cur_max = 0
for _, _, l, r, idx in queries:
    while cur_l > l:
        cur_l -= 1
        x = a[cur_l]
        f = freq[x]
        if f:
            count_freq[f] -= 1
        f += 1
        freq[x] = f
        count_freq[f] += 1
        if f > cur_max:
            cur_max = f
    while cur_r < r:
        cur_r += 1
        x = a[cur_r]
        f = freq[x]
        if f:
            count_freq[f] -= 1
        f += 1
        freq[x] = f
        count_freq[f] += 1
        if f > cur_max:
            cur_max = f
    while cur_l < l:
        x = a[cur_l]
        f = freq[x]
        count_freq[f] -= 1
        f -= 1
        freq[x] = f
        if f:
            count_freq[f] += 1
        if cur_max > 0 and count_freq[cur_max] == 0:
            cur_max -= 1
        cur_l += 1
    while cur_r > r:
        x = a[cur_r]
        f = freq[x]
        count_freq[f] -= 1
        f -= 1
        freq[x] = f
        if f:
            count_freq[f] += 1
        if cur_max > 0 and count_freq[cur_max] == 0:
            cur_max -= 1
        cur_r -= 1
    answers[idx] = cur_max
sys.stdout.write("\n".join(map(str, answers)))
