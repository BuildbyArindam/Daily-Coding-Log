"""
Problem   : Ember Loads at Cobalt Pottery
Platform  : Unstop 
Link      : https://unstop.com/code/practice/673732
Date      : 2026-11-23
Difficulty: Easy
Topics    : Dynamic Programming, Segment Tree, Monotonic Stack,
            Range Minimum, DP Optimization

Approach
--------
dp[i] = best cost to split the first i items into consecutive groups whose
sizes lie in [A, B], where a group's cost is (max - min). Ties are broken by
fewer groups.

  * The (waste, loads) pair is packed into one integer: (waste << 20) + loads,
    so a single min comparison handles both objectives.
  * For the current i, the cost of the last group starting at j is
    dp[j] + (max(arr[j..i-1]) - min(arr[j..i-1])).
  * Two monotonic stacks (max and min) track where each running max/min
    changes. When a stack pops, the affected range of start positions j gets
    a range-add on the segment tree.
  * The segment tree (range add, range min, non-propagating lazy) holds
    dp[j] + range(j..i-1) for every j. dp[i] is the range-min over
    j in [i-B, i-A], plus 1 load.
  * Unreachable states stay at BIG and are rejected via the HALF threshold.

Complexity
----------
Time  : O(N log N), since each element is pushed/popped once per stack and
        each pop costs one O(log N) range update, plus one O(log N) query per i.
Space : O(N) for the dp array, stacks, and segment tree.
"""


# ------------------------------------------- Solution ---------------------------------------------------------


import sys

def main():
    data = sys.stdin.read().split()
    n, A, B = int(data[0]), int(data[1]), int(data[2])
    arr = [int(x) for x in data[3:3 + n]]
    SH = 20
    M = 1 << SH
    BIG = 1 << 100
    HALF = BIG >> 1
    size = 1
    while size < n + 1:
        size <<= 1
    tree = [BIG] * (2 * size)
    lazy = [0] * (2 * size)
    def bump(lo, hi, val):
        if lo >= hi:
            return
        l = lo + size
        r = hi + size
        p = l
        q = r - 1
        while l < r:
            if l & 1:
                tree[l] += val
                lazy[l] += val
                l += 1
            if r & 1:
                r -= 1
                tree[r] += val
                lazy[r] += val
            l >>= 1
            r >>= 1
        p >>= 1
        while p:
            a = tree[2 * p]
            b = tree[2 * p + 1]
            tree[p] = (a if a < b else b) + lazy[p]
            p >>= 1
        q >>= 1
        while q:
            a = tree[2 * q]
            b = tree[2 * q + 1]
            tree[q] = (a if a < b else b) + lazy[q]
            q >>= 1
    def fetch(lo, hi):
        l = lo + size
        r = hi + size
        left_best = BIG * 4
        right_best = BIG * 4
        while l < r:
            if l & 1:
                if tree[l] < left_best:
                    left_best = tree[l]
                l += 1
            if r & 1:
                r -= 1
                if tree[r] < right_best:
                    right_best = tree[r]
            l >>= 1
            r >>= 1
            left_best += lazy[l - 1]
            right_best += lazy[r]
        u = l - 1
        while u > 1:
            u >>= 1
            left_best += lazy[u]
        w = r
        while w > 1:
            w >>= 1
            right_best += lazy[w]
        return left_best if left_best < right_best else right_best
    dp = [None] * (n + 1)
    dp[0] = 0
    hi_val = []
    hi_beg = []
    lo_val = []
    lo_beg = []
    for i in range(1, n + 1):
        x = arr[i - 1]
        edge = i - 1
        cur_end = edge
        start = edge
        while hi_val and hi_val[-1] <= x:
            v = hi_val.pop()
            s = hi_beg.pop()
            if x != v:
                bump(s, cur_end, (x - v) << SH)
            cur_end = s
            start = s
        hi_val.append(x)
        hi_beg.append(start)
        cur_end = edge
        start = edge
        while lo_val and lo_val[-1] >= x:
            v = lo_val.pop()
            s = lo_beg.pop()
            if x != v:
                bump(s, cur_end, (v - x) << SH)
            cur_end = s
            start = s
        lo_val.append(x)
        lo_beg.append(start)
        if dp[i - 1] is not None:
            bump(i - 1, i, dp[i - 1] - BIG)
        top = i - A
        if top >= 0:
            bottom = i - B
            if bottom < 0:
                bottom = 0
            res = fetch(bottom, top + 1)
            if res < HALF:
                dp[i] = res + 1
    final = dp[n]
    if final is None:
        print("Cobalt plan: impossible")
    else:
        waste = final >> SH
        loads = final & (M - 1)
        print("Cobalt plan: waste " + str(waste) + " with " + str(loads) + " loads")

main()
