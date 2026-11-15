"""
Problem   : Gantry Drift Audit
Platform  : Unstop 
Link      : https://unstop.com/code/practice/671426
Date      : 2026-11-15
Difficulty: Hard
Topics    : DP, Slope Trick, Convex Optimization, Heap (Priority Queue)

Approach
--------
The DP cost f_i(x) is convex and piecewise linear. Instead of storing it,
keep its breakpoints in two heaps (slope trick):
  - left  : max-heap of breakpoints where the slope is negative
  - right : min-heap of breakpoints where the slope is positive
Each step does two things:
  1. The allowed movement (up/dn) widens the flat minimum. This is done with
     lazy offsets shiftL / shiftR, so no heap element is touched.
  2. The interval [lo, hi] adds the penalty max(0, lo-x) + max(0, x-hi).
     Each side is applied by comparing the opposite heap's top against the
     bound, adding any gap to `base` (the running minimum), and pushing
     and popping one breakpoint.
After the last step, f(z) = base + sum over left breakpoints l > z of (l - z)
                                 + sum over right breakpoints r < z of (z - r).
Each query is answered with sorted breakpoints, prefix sums and binary search.
Output: the minimum cost `base`, the largest left breakpoint (the right end of
the optimal flat region), then f(z) for every query z.

Complexity
----------
Time  : O((n + q) log n)  (heap ops + sorting + one binary search per query)
Space : O(n + q)
"""


# ------------------------------------------------ Solution ------------------------------------------------------------


import sys
from bisect import bisect_left as bl, bisect_right as br
from heapq import heappush as hpush, heappushpop as hpp
from itertools import accumulate as acc

def answer_queries(zs, Lv, Rv):
    pl = [0] + list(acc(Lv))
    pr = [0] + list(acc(Rv))
    nl, nr = len(Lv), len(Rv)
    totL = pl[-1]
    out = []
    for z in zs:
        k = br(Lv, z)                 
        extra = (totL - pl[k]) - z * (nl - k)
        m = bl(Rv, z)              
        extra += z * m - pr[m]
        out.append(extra)
    return out

def main():
    tok = sys.stdin.buffer.read().split()
    n = int(tok[0])
    q = int(tok[1])
    left, right = [], [] 
    shiftL = 0
    shiftR = 0
    base = 0
    p = 2
    for step in range(n):
        if step == 0:
            lo = int(tok[p]); hi = int(tok[p + 1]); p += 2
        else:
            lo = int(tok[p]); hi = int(tok[p + 1])
            up = int(tok[p + 2]); dn = int(tok[p + 3]); p += 4
            shiftL -= dn       
            shiftR += up  
        if left:
            topl = -left[0] + shiftL
            if topl > hi:
                base += topl - hi
        moved = -hpp(left, -(hi - shiftL)) + shiftL
        hpush(right, moved - shiftR)
        topr = right[0] + shiftR
        if lo > topr:
            base += lo - topr
        moved = hpp(right, lo - shiftR) + shiftR
        hpush(left, -(moved - shiftL))
    Lv = sorted(shiftL - x for x in left)
    Rv = sorted(x + shiftR for x in right)
    zs = [int(t) for t in tok[p:p + q]]
    res = answer_queries(zs, Lv, Rv)
    lines = [f"{base} {Lv[-1]}"]
    lines.extend(str(base + r) for r in res)
    sys.stdout.write("\n".join(lines) + "\n")

main()
