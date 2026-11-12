"""
Problem   : Tasting Passes on the Lantern Promenade
Platform  : Unstop 
Link      : https://unstop.com/code/practice/671342
Date      : 2026-11-12
Difficulty: Hard
Topics    : Wavelet Matrix (offline), Coordinate Compression, Range Queries

Approach
  For each query (l, r, budget), buy items in the range cheapest-first until
  the budget runs out. Compress prices to ranks, then process the rank bits
  from MSB to LSB, building one wavelet-matrix level per bit and moving all
  queries down together.
  At each level, check whether the whole "bit = 0" (cheaper) half of the
  current range fits in the budget:
    - fits: buy all of it (add its quantity, subtract its cost), then descend
            into the "bit = 1" half.
    - not:  descend into the "bit = 0" half.
  At the leaf, the price is a single value u, so buy min(stock, budget // u).
  Output: (items bought, leftover budget).

Complexity
  Time  : O((N + Q) * log D), D = number of distinct prices
  Space : O(N + Q)
"""


# ----------------------------------------- Solution --------------------------------------------------------------


import sys
from itertools import accumulate

def solve():
    data = sys.stdin.buffer.read().split()
    n, q = int(data[0]), int(data[1])
    prices = list(map(int, data[2:2 + n]))
    stock = list(map(int, data[2 + n:2 + 2 * n]))
    base = 2 + 2 * n
    L = [0] * q
    R = [0] * q
    W = [0] * q
    for j in range(q):
        t = base + 3 * j
        L[j] = int(data[t]) - 1
        R[j] = int(data[t + 1])
        W[j] = int(data[t + 2])
    vals = sorted(set(prices))
    D = len(vals)
    where = {v: i for i, v in enumerate(vals)}
    rk = [where[v] for v in prices]
    qt = stock[:]
    ct = [prices[i] * stock[i] for i in range(n)]
    depth = max(1, (D - 1).bit_length())
    got = [0] * q
    path = [0] * q
    rng = range(q)
    for k in range(depth - 1, -1, -1):
        low = [((x >> k) & 1) ^ 1 for x in rk] 
        zc = list(accumulate(low, initial=0))
        zq = list(accumulate([a * b for a, b in zip(qt, low)], initial=0))
        zw = list(accumulate([a * b for a, b in zip(ct, low)], initial=0))
        total_zero = zc[n]
        for j in rng:
            a = L[j]
            b = R[j]
            need = zw[b] - zw[a]
            m = W[j]
            if need <= m:
                W[j] = m - need
                got[j] += zq[b] - zq[a]
                path[j] = path[j] * 2 + 1
                L[j] = total_zero + a - zc[a]
                R[j] = total_zero + b - zc[b]
            else:
                path[j] = path[j] * 2
                L[j] = zc[a]
                R[j] = zc[b]
        zeros = [i for i in range(n) if low[i]]
        ones = [i for i in range(n) if not low[i]]
        order = zeros + ones
        rk = [rk[i] for i in order]
        qt = [qt[i] for i in order]
        ct = [ct[i] for i in order]
    pre = list(accumulate(qt, initial=0))
    out = []
    last = D - 1
    for j in rng:
        have = pre[R[j]] - pre[L[j]]
        node = path[j]
        if node > last:
            node = last
        u = vals[node]
        take = W[j] // u
        if have < take:
            take = have
        out.append("%d %d" % (got[j] + take, W[j] - take * u))
    sys.stdout.write("\n".join(out) + "\n")

solve()
