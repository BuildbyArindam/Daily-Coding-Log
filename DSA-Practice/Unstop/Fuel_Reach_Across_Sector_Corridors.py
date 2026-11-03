"""
Problem   : Fuel Reach Across Sector Corridors
Platform  : Unstop 
Link      : https://unstop.com/code/practice/670114
Date      : 2026-11-03
Difficulty: Hard
Topics    : Graph, DSU, Segment Tree, Offline Queries, Offline Dynamic Connectivity

Approach
--------
Each corridor (u, v) is only active during [s, e], and each query (t, a) asks for
the size and total litres of the component containing `a` at time t. This is
offline dynamic connectivity:
  1. Compress the query timestamps; only these times matter.
  2. Build a segment tree over the compressed timeline. Each corridor is added
     to the O(log M) nodes that exactly cover its active interval.
  3. DFS the segment tree. On entering a node, union its corridors in a DSU
     (union by size, no path compression) and push each merge onto a rollback
     stack. At a leaf, answer that timestamp's queries from the component root.
     On exit, undo the merges back to the checkpoint.
  4. The DSU tracks both member count and litre sum per component, and both
     are restored on rollback.

Complexity
----------
Time  : O((K log M) * log A + Q log A), M = distinct query times (M <= Q)
Space : O(A + K log M + Q)
"""


# ----------------------------------------------- Solution ---------------------------------------------------------------


import sys
from bisect import bisect_left, bisect_right

def main():
    tok = sys.stdin.buffer.read().split()
    A, K, Q = int(tok[0]), int(tok[1]), int(tok[2])
    pos = 3
    boss = list(range(A + 1))
    members = [1] * (A + 1)
    litres = [0] + [int(x) for x in tok[pos:pos + A]]
    pos += A

    raw = []
    for _ in range(K):
        raw.append((int(tok[pos]), int(tok[pos + 1]), int(tok[pos + 2]), int(tok[pos + 3])))
        pos += 4

    asks = []
    for _ in range(Q):
        asks.append((int(tok[pos]), int(tok[pos + 1])))
        pos += 2

    stamps = sorted({t for t, _ in asks})
    M = len(stamps)
    width = 1
    while width < M:
        width <<= 1

    bucket = [[] for _ in range(M)]
    for qi, (t, a) in enumerate(asks):
        bucket[bisect_left(stamps, t)].append((qi, a))

    seg = [[] for _ in range(2 * width)]
    for u, v, s, e in raw:
        lo = bisect_left(stamps, s)
        hi = bisect_right(stamps, e)
        if lo >= hi:
            continue
        lo += width
        hi += width
        while lo < hi:
            if lo & 1:
                seg[lo].append((u, v))
                lo += 1
            if hi & 1:
                hi -= 1
                seg[hi].append((u, v))
            lo >>= 1
            hi >>= 1

    trail = []
    out_cnt = [0] * Q
    out_sum = [0] * Q

    def top(x):
        while boss[x] != x:
            x = boss[x]
        return x

    def explore(node, left, right):
        if left >= M:
            return
        checkpoint = len(trail)
        for u, v in seg[node]:
            ru, rv = top(u), top(v)
            if ru != rv:
                if members[ru] < members[rv]:
                    ru, rv = rv, ru
                boss[rv] = ru
                members[ru] += members[rv]
                litres[ru] += litres[rv]
                trail.append(rv)
        if right - left == 1:
            for qi, a in bucket[left]:
                r = top(a)
                out_cnt[qi] = members[r]
                out_sum[qi] = litres[r]
        else:
            mid = (left + right) >> 1
            explore(2 * node, left, mid)
            explore(2 * node + 1, mid, right)
        while len(trail) > checkpoint:
            c = trail.pop()
            p = boss[c]
            members[p] -= members[c]
            litres[p] -= litres[c]
            boss[c] = c
    explore(1, 0, width)
    sys.stdout.write("\n".join("%d %d" % (out_cnt[i], out_sum[i]) for i in range(Q)) + "\n")

main()
