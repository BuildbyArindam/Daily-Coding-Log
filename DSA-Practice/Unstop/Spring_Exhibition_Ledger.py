"""
Problem   : Spring Exhibition Ledger
Platform  : Unstop 
Link      : https://unstop.com/code/practice/667838
Date      : 2026-10-24
Difficulty: Hard
Topics    : Greedy, Scheduling, Segment Tree (Lazy Range Add / Range Min),
            Offline Processing, Sorting

Approach
--------
For every prefix of the input, report the maximum total profit of a feasible
set of unit-time jobs, each with a deadline and a profit.

- Compress the distinct deadlines into sorted "days".
- Segment tree A stores slack[i] = days[i] - (#chosen jobs with deadline <= days[i]).
  A set is feasible iff every slack is >= 0.
- Add a job: push its profit onto the min-heap for its deadline and do a
  suffix range-add of -1 on the slack tree.
- If some slack goes negative, find the first violating day (descend the tree
  using the range minimum). Among all jobs with deadline <= that day, drop the
  cheapest one, found with a second segment tree over each deadline's heap-min
  (key = profit * 2^18 + index). Then undo the suffix decrement with +1.
- The running total after each step is the answer for that prefix.

Complexity
----------
Time  : O(n log n)  - each job triggers O(1) heap ops plus O(1) tree updates/queries
Space : O(n)        - heaps, two segment trees of size ~2 * (distinct deadlines)

Note: the packed key assumes fewer than 2^18 distinct deadlines.
"""


# ---------------------------------------------- Solution -----------------------------------------------------------------


import sys
from heapq import heappush, heappop

def main():
    raw = sys.stdin.buffer.read().split()
    cnt = int(raw[0])
    dues = raw[1:2 * cnt + 1:2]
    pres = raw[2:2 * cnt + 2:2]
    dues = [int(x) for x in dues]
    pres = [int(x) for x in pres]
    days = sorted(set(dues))
    m = len(days)
    where = {v: i for i, v in enumerate(days)}
    cap = 1
    while cap < m:
        cap <<= 1
    BIG = 1 << 60
    mn = [BIG] * (2 * cap)
    lz = [0] * (2 * cap)
    for i in range(m):
        mn[cap + i] = days[i]
    for p in range(cap - 1, 0, -1):
        mn[p] = min(mn[2 * p], mn[2 * p + 1])
    SH = 1 << 18
    INF = 1 << 62
    pk = [INF] * (2 * cap)
    piles = [[] for _ in range(m)]

    def suffix_add(pos, val):
        lo = pos + cap
        hi = 2 * cap
        a, b = lo, hi
        while a < b:
            if a & 1:
                mn[a] += val
                lz[a] += val
                a += 1
            if b & 1:
                b -= 1
                mn[b] += val
                lz[b] += val
            a >>= 1
            b >>= 1
        q = lo >> 1
        while q:
            mn[q] = (mn[2 * q] if mn[2 * q] < mn[2 * q + 1] else mn[2 * q + 1]) + lz[q]
            q >>= 1

    def first_negative():
        if mn[1] >= 0:
            return -1
        p = 1
        acc = 0
        while p < cap:
            acc += lz[p]
            p <<= 1
            if mn[p] + acc >= 0:
                p |= 1
        return p - cap

    def refresh_leaf(i):
        h = piles[i]
        q = i + cap
        pk[q] = h[0] * SH + i if h else INF
        q >>= 1
        while q:
            l, r = pk[2 * q], pk[2 * q + 1]
            pk[q] = l if l < r else r
            q >>= 1

    def prefix_best(last):
        a, b = cap, last + cap + 1
        best = INF
        while a < b:
            if a & 1:
                if pk[a] < best:
                    best = pk[a]
                a += 1
            if b & 1:
                b -= 1
                if pk[b] < best:
                    best = pk[b]
            a >>= 1
            b >>= 1
        return best
    total = 0
    out = []
    for k in range(cnt):
        i = where[dues[k]]
        w = pres[k]
        heappush(piles[i], w)
        refresh_leaf(i)
        suffix_add(i, -1)
        total += w
        bad = first_negative()
        if bad >= 0:
            key = prefix_best(bad)
            j = key & (SH - 1)
            val = key >> 18
            heappop(piles[j])
            refresh_leaf(j)
            suffix_add(j, 1)
            total -= val
        out.append(total)
    sys.stdout.write(" ".join(map(str, out)) + "\n")

main()
