"""
Problem   : Dis-Card
Platform  : CodeChef
Link      : https://www.codechef.com/problems/DISCARD2
Date      : 2026-08-28
Difficulty: Easy
Topics    : Binary Search, Range Minimum Queries, Segment Tree

Approach:
For each K, let x_K = pos of K in P, y_K = pos of K in Q. Discarding K last
requires every other element to appear before K in P or in Q. For a chosen
cut point i (>= x_K) in P, the cost is:
    (i - x_K) + max(0, suffix_max(y over P[i+1..n]) - y_K)
Precompute suffix maxima of Q-positions along P (suf) and, symmetrically,
suffix maxima of P-positions along Q (bestP) to get a baseline candidate
in O(1). For the remaining case, build a segment tree over C[i] = i + suf[i]
and take a range-min query over (p, r0) to find the optimal cut point.

Time complexity : O(N log N) per test case (segment tree build + one
                   range-min query per K)
Space complexity: O(N) (segment tree + auxiliary arrays)
"""


# ---------------------------- Solution -----------------------------------


import sys

def solve_case(n, P, Q):
    depc = [0] * (n + 1)
    deqc = [0] * (n + 1)
    for i, x in enumerate(P, 1):
        depc[x] = i
    for i, x in enumerate(Q, 1):
        deqc[x] = i
    suf = [0] * (n + 1)
    mx = 0
    for i in range(n, 0, -1):
        v = deqc[P[i - 1]]
        if v > mx:
            mx = v
        suf[i - 1] = mx
    bestP = [0] * (n + 1)
    mx = 0
    for q in range(n - 1, 0, -1):
        v = depc[Q[q]] 
        if v > mx:
            mx = v
        bestP[q] = mx
    size = 1
    while size < n + 1:
        size <<= 1
    INF = 10**18
    seg = [INF] * (2 * size)
    for r in range(1, n + 1):
        seg[size + r] = r + suf[r]
    for i in range(size - 1, 0, -1):
        left = seg[i << 1]
        right = seg[i << 1 | 1]
        seg[i] = left if left < right else right

    def range_min(l, r):
        l += size
        r += size
        ans = INF
        while l < r:
            if l & 1:
                if seg[l] < ans:
                    ans = seg[l]
                l += 1
            if r & 1:
                r -= 1
                if seg[r] < ans:
                    ans = seg[r]
            l >>= 1
            r >>= 1
        return ans
    ans = [0] * (n + 1)
    for k in range(1, n + 1):
        p = depc[k]
        q = deqc[k]
        r0 = max(p, bestP[q])
        best = r0 - p
        if p < r0:
            mn = range_min(p, r0)
            cand = mn - p - q
            if cand < best:
                best = cand
        ans[k] = best
    return ans[1:]

def main():
    input = sys.stdin.buffer.readline
    T = int(input())
    out = []
    for _ in range(T):
        n = int(input())
        P = list(map(int, input().split()))
        Q = list(map(int, input().split()))
        res = solve_case(n, P, Q)
        out.append(" ".join(map(str, res)))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
