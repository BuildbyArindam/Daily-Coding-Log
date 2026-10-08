"""
Problem   : The Exposure Ledger (Unstop)
Link      : https://unstop.com/code/practice/661681
Date      : 2026-10-08
Difficulty: Hard
Topics    : Persistent Segment Tree, Fenwick Tree, Coordinate Compression,
            Range Queries, K-th Order Statistics

Approach
--------
The queries split into two independent problems on a static array and a
dynamic flag set.

1. RANK l r k (k-th smallest in a[l..r]):
   - Coordinate-compress values to ranks 1..m.
   - Build a persistent segment tree over value ranks, one version per prefix
     (roots[i] = tree after inserting a[1..i]).
   - The tree for a[l..r] is roots[r] - roots[l-1], found by subtracting node
     counts. Descend from the root: go left if k <= left_count, otherwise
     subtract left_count and go right.

2. FLAG i (toggle) and the range-count query:
   - Keep a Fenwick Tree (BIT) over positions plus a `flagged` bytearray.
   - FLAG toggles the bit and adds +1 or -1 to the BIT.
   - The range-count query is bit_sum(r) - bit_sum(l-1).

Complexity
----------
Time  : O((N + Q) log N) overall
        - Build: O(N log m)
        - RANK: O(log m)
        - FLAG / range count: O(log N)
Space : O(N log m) for the persistent tree nodes (~N * (log m + 1)),
        plus O(N) for the BIT and flags.
"""


# --------------------------------------- Solution -----------------------------------------------------


import sys
from array import array

input = sys.stdin.buffer.readline
N, Q = map(int, input().split())
a = list(map(int, input().split()))
values = sorted(set(a))
m = len(values)
rank = {v: i + 1 for i, v in enumerate(values)}
left = array('i', [0])
right = array('i', [0])
cnt = array('i', [0])
roots = array('i', [0]) * (N + 1)

def update(prev, lo, hi, pos):
    new = len(cnt)
    left.append(left[prev])
    right.append(right[prev])
    cnt.append(cnt[prev] + 1)
    if lo != hi:
        mid = (lo + hi) >> 1
        if pos <= mid:
            child = update(left[prev], lo, mid, pos)
            left[new] = child
        else:
            child = update(right[prev], mid + 1, hi, pos)
            right[new] = child
    return new

for i, x in enumerate(a, 1):
    roots[i] = update(roots[i - 1], 1, m, rank[x])

def kth(root_r, root_l, lo, hi, k):
    while lo != hi:
        mid = (lo + hi) >> 1
        left_count = cnt[left[root_r]] - cnt[left[root_l]]
        if k <= left_count:
            root_r = left[root_r]
            root_l = left[root_l]
            hi = mid
        else:
            k -= left_count
            root_r = right[root_r]
            root_l = right[root_l]
            lo = mid + 1
    return lo

bit = [0] * (N + 1)
flagged = bytearray(N + 1)

def bit_add(i, delta):
    while i <= N:
        bit[i] += delta
        i += i & -i

def bit_sum(i):
    s = 0
    while i > 0:
        s += bit[i]
        i -= i & -i
    return s
out = []
for _ in range(Q):
    parts = input().split()
    op = parts[0]
    if op == b'RANK':
        l = int(parts[1])
        r = int(parts[2])
        k = int(parts[3])
        compressed = kth(roots[r], roots[l - 1], 1, m, k)
        out.append(str(values[compressed - 1]))
    elif op == b'FLAG':
        i = int(parts[1])
        if flagged[i]:
            flagged[i] = 0
            bit_add(i, -1)
        else:
            flagged[i] = 1
            bit_add(i, 1)
    else:  
        l = int(parts[1])
        r = int(parts[2])
        out.append(str(bit_sum(r) - bit_sum(l - 1)))
sys.stdout.write('\n'.join(out))
