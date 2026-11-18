"""
Problem   : Ridge Trail Ledger
Platform  : Unstop 
Link      : https://unstop.com/code/practice/672528
Date      : 2026-11-18
Difficulty: Hard
Topics    : Array, Fenwick Tree, Offline Queries, Coordinate Compression, Tree

Approach
--------
For each query (lo, hi), sum the distinct-species counts over all
subarrays [l, r] with lo <= l <= r <= hi. The runs are expanded into a flat trail.
1. Process queries offline, bucketed by right endpoint `hi`.
2. Sweep r from 1..n. Keep prev = last occurrence of trail[r]. Adding r makes
   trail[r] a new distinct element for every left endpoint l in [prev+1, r],
   so cnt[l] += 1 on that range, and the increase persists for all later r.
3. Let H[l] = sum over r' <= r of cnt_{r'}[l] (history sum). A range add
   that starts at time t contributes (r - t + 1) = r*1 + (1 - t) at time r,
   so each range stores a slope (coefficient of r) and an intercept.
4. Maintain slope and intercept with range-update / range-query Fenwick trees
   (two BIT pairs, the standard "B1/B2" trick).
5. At r == hi, answer = r*(K[hi] - K[lo-1]) + (C[hi] - C[lo-1]),
   where K and C are the prefix sums of slope and intercept.

Complexity
----------
Time  : O((L + Q) log L), L = total expanded trail length, Q = queries
Space : O(L + Q)
"""


# --------------------------------------------------- Solution -------------------------------------------------------------------


import sys

def climb(tree_a, tree_b, tree_c, tree_e, size, j, d1, d2):
    jd1 = d1 * j
    jd2 = d2 * j
    while j <= size:
        tree_a[j] += d1
        tree_b[j] += jd1
        tree_c[j] += d2
        tree_e[j] += jd2
        j += j & -j

def descend(tree_a, tree_b, tree_c, tree_e, x):
    sa = sb = sc = se = 0
    k = x
    while k > 0:
        sa += tree_a[k]
        sb += tree_b[k]
        sc += tree_c[k]
        se += tree_e[k]
        k &= k - 1
    return (x + 1) * sa - sb, (x + 1) * sc - se

def main():
    raw = sys.stdin.buffer.read().split()
    runs_cnt = int(raw[0])
    qry_cnt = int(raw[1])
    cur = 2
    trail = [None]
    for _ in range(runs_cnt):
        code = raw[cur]
        length = int(raw[cur + 1])
        cur += 2
        trail.extend([code] * length)
    n = len(trail) - 1
    bucket = [[] for _ in range(n + 1)]
    for idx in range(qry_cnt):
        lo = int(raw[cur])
        hi = int(raw[cur + 1])
        cur += 2
        bucket[hi].append((lo, idx))
    size = n + 2
    ta = [0] * (size + 1)
    tb = [0] * (size + 1)
    tc = [0] * (size + 1)
    te = [0] * (size + 1)
    seen = {}
    answer = [0] * qry_cnt
    for r in range(1, n + 1):
        sp = trail[r]
        prev = seen.get(sp, 0)
        seen[sp] = r
        a = prev + 1
        w = 1 - r
        climb(ta, tb, tc, te, size, a, 1, w)
        climb(ta, tb, tc, te, size, r + 1, -1, -w)
        if bucket[r]:
            kr, cr = descend(ta, tb, tc, te, r)
            for lo, idx in bucket[r]:
                kl, cl = descend(ta, tb, tc, te, lo - 1)
                answer[idx] = r * (kr - kl) + (cr - cl)
    sys.stdout.write(" ".join(map(str, answer)) + "\n")

main()
