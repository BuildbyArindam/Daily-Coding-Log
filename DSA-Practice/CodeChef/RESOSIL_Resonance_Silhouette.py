"""
Problem   : Resonance Silhouette (RESOSIL)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/RESOSIL
Date      : 2026-10-07
Difficulty: Hard
Topics    : Greedy, DP, Segment Tree, Intervals

Approach:
  1. Scan adjacent pairs of A. Each "descent then ascent" pattern defines an
     interval [last_descent, current_ascent] that must contain a '1'.
  2. Drop intervals that already contain a '1' in S (prefix sums), leaving the
     intervals that still need a chosen position.
  3. The remaining intervals have monotone left and right endpoints, so a
     min-cost hitting set is computed with a suffix DP. suff[k] is the cheapest
     way to cover intervals k..m-1, found with a min segment tree over
     positions, processed in decreasing k.
  4. If suff[0] > B, print -1. Otherwise build the answer greedily left to
     right: set a '0' to '1' only if spent + C[i] + suff[next interval]
     still fits in B, so earlier positions get '1' whenever feasible.

Time  : O(N log N) per test case (segment tree updates and queries)
Space : O(N)
"""


# ----------------------------------------- Solution ----------------------------------------------------------


import sys
from bisect import bisect_right as _bsr

def _resolve_case(N, B, A, S, C):
    M = N - 1
    down_mark = -1
    starts, ends = [], []
    for i in range(M):
        ai, aj = A[i], A[i + 1]
        if ai > aj:
            down_mark = i
        elif ai < aj and down_mark != -1:
            starts.append(down_mark)
            ends.append(i)
    pre = [0] * (M + 1)
    for i, ch in enumerate(S):
        pre[i + 1] = pre[i] + (ch == '1')
    Lx, Rx = [], []
    for a, b in zip(starts, ends):
        if pre[b + 1] - pre[a] == 0:
            Lx.append(a)
            Rx.append(b)
    m = len(Lx)
    kfull = [0] * M
    if m:
        p = 0
        for i in range(M):
            while p < m and Lx[p] <= i:
                p += 1
            kfull[i] = p
    suff = [0] * (m + 1)
    if m:
        sz = 1
        while sz < M:
            sz <<= 1
        BIG = float('inf')
        seg = [BIG] * (2 * sz)
        def put(pos, v):
            pos += sz
            if v < seg[pos]:
                seg[pos] = v
                pos >>= 1
                while pos:
                    nv = seg[2 * pos] if seg[2 * pos] < seg[2 * pos + 1] else seg[2 * pos + 1]
                    if seg[pos] == nv:
                        break
                    seg[pos] = nv
                    pos >>= 1
        def get(l, r):
            res = BIG
            l += sz
            r += sz + 1
            while l < r:
                if l & 1:
                    if seg[l] < res:
                        res = seg[l]
                    l += 1
                if r & 1:
                    r -= 1
                    if seg[r] < res:
                        res = seg[r]
                l >>= 1
                r >>= 1
            return res
        buckets = [[] for _ in range(m + 1)]
        lo, hi = Lx[0], Rx[-1]
        for pos in range(lo, hi + 1):
            buckets[kfull[pos]].append(pos)
        for pos in buckets[m]:
            if S[pos] == '0':
                put(pos, C[pos])
        for k in range(m - 1, -1, -1):
            suff[k] = get(Lx[k], Rx[k])
            for pos in buckets[k]:
                if S[pos] == '0':
                    put(pos, C[pos] + suff[k])
    if suff[0] > B:
        return "-1"
    spent = 0
    chars = [None] * M
    for i in range(M):
        if S[i] == '1':
            chars[i] = '1'
        else:
            need = C[i] + suff[kfull[i]]
            if spent + need <= B:
                chars[i] = '1'
                spent += C[i]
            else:
                chars[i] = '0'
    return ''.join(chars)

def main():
    data = sys.stdin.buffer.read().split()
    pos = 0
    T = int(data[pos]); pos += 1
    answers = []
    for _ in range(T):
        N = int(data[pos]); Bv = int(data[pos + 1]); pos += 2
        A = data[pos:pos + N]; pos += N
        A = [int(x) for x in A]
        Sraw = data[pos].decode(); pos += 1
        if N - 1 > 0:
            Carr = data[pos:pos + N - 1]; pos += N - 1
            Carr = [int(x) for x in Carr]
        else:
            Carr = []
        answers.append(_resolve_case(N, Bv, A, Sraw, Carr))
    sys.stdout.write('\n'.join(answers) + '\n')

if __name__ == "__main__":
    main()
