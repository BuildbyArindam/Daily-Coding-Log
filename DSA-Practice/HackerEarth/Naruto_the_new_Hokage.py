"""
Problem   : Naruto - The New Hokage
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/data-structures/advanced-data-structures/segment-trees/practice-problems/algorithm/road-to-dmg-8883b64f/
Difficulty: Medium
Topics    : Advanced Data Structures, Segment Trees

Approach:
    Segment tree where each node stores the sum of the p-th powers
    (p = 0..10) of all elements in its range, i.e. sums[p][node] = sum(a_i^p).
    Range-add updates are handled with lazy propagation: instead of
    eagerly recomputing all 11 power-sums on every push, an "add" lazy
    value is stacked at each node. When power-sums for a range are
    actually needed (query or a lazy value must be pushed down for a
    partial update), the binomial theorem is used to expand
    sum((a_i + k)^p) in terms of the stored sum(a_i^j) for j <= p and
    powers of k, using precomputed Pascal's-triangle coefficients (C).
    A "dirty" flag marks nodes whose stored sums are stale w.r.t. their
    children's pending lazy adds, and `ensure()` lazily rebuilds them
    top-down only when required.

Time complexity : O((n + q) * P^2 * log n), P = 11 (powers 0..10)
Space complexity : O(P * n) for the sums table + O(n) for lazy/dirty arrays
"""


# ----------------------------- Solution ----------------------------------------


import sys
MOD = 1000000007
MAXP = 10
C = [[0] * 11 for _ in range(11)]
for n in range(11):
    C[n][0] = C[n][n] = 1
    for r in range(1, n):
        C[n][r] = C[n - 1][r - 1] + C[n - 1][r]

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    pos = 0
    T = data[pos]
    pos += 1
    ans = []
    for _ in range(T):
        n = data[pos]
        pos += 1
        a = data[pos:pos + n]
        pos += n
        q = data[pos]
        pos += 1
        size = 4 * n + 5
        sums = [[0] * size for _ in range(11)]
        lazy = [0] * size
        dirty = bytearray(size)
        def build(node, l, r):
            if l == r:
                x = a[l] % MOD
                sums[0][node] = 1
                sums[1][node] = x
                v = x
                for p in range(2, 11):
                    v = (v * x) % MOD
                    sums[p][node] = v
                return
            mid = (l + r) >> 1
            lc = node << 1
            rc = lc | 1
            build(lc, l, mid)
            build(rc, mid + 1, r)
            s0 = sums[0]
            s1 = sums[1]
            s2 = sums[2]
            s3 = sums[3]
            s4 = sums[4]
            s5 = sums[5]
            s6 = sums[6]
            s7 = sums[7]
            s8 = sums[8]
            s9 = sums[9]
            s10 = sums[10]
            s0[node] = s0[lc] + s0[rc]
            s1[node] = s1[lc] + s1[rc]
            s2[node] = s2[lc] + s2[rc]
            s3[node] = s3[lc] + s3[rc]
            s4[node] = s4[lc] + s4[rc]
            s5[node] = s5[lc] + s5[rc]
            s6[node] = s6[lc] + s6[rc]
            s7[node] = s7[lc] + s7[rc]
            s8[node] = s8[lc] + s8[rc]
            s9[node] = s9[lc] + s9[rc]
            s10[node] = s10[lc] + s10[rc]
            if s0[node] >= MOD:
                s0[node] %= MOD
            if s1[node] >= MOD:
                s1[node] %= MOD
            if s2[node] >= MOD:
                s2[node] %= MOD
            if s3[node] >= MOD:
                s3[node] %= MOD
            if s4[node] >= MOD:
                s4[node] %= MOD
            if s5[node] >= MOD:
                s5[node] %= MOD
            if s6[node] >= MOD:
                s6[node] %= MOD
            if s7[node] >= MOD:
                s7[node] %= MOD
            if s8[node] >= MOD:
                s8[node] %= MOD
            if s9[node] >= MOD:
                s9[node] %= MOD
            if s10[node] >= MOD:
                s10[node] %= MOD
        build(1, 0, n - 1)
        def rebuild(node):
            lc = node << 1
            rc = lc | 1
            kl = lazy[lc]
            if kl:
                lp = [1] * 11
                for i in range(1, 11):
                    lp[i] = (lp[i - 1] * kl) % MOD
            else:
                lp = None
            kr = lazy[rc]
            if kr:
                rp = [1] * 11
                for i in range(1, 11):
                    rp[i] = (rp[i - 1] * kr) % MOD
            else:
                rp = None
            left_actual = [0] * 11
            right_actual = [0] * 11
            if kl:
                for p in range(11):
                    total = 0
                    cp = C[p]
                    sp = 0
                    for j in range(p + 1):
                        total += cp[j] * sums[j][lc] * lp[p - j]
                    left_actual[p] = total % MOD
            else:
                for p in range(11):
                    left_actual[p] = sums[p][lc]
            if kr:
                for p in range(11):
                    total = 0
                    cp = C[p]
                    for j in range(p + 1):
                        total += cp[j] * sums[j][rc] * rp[p - j]
                    right_actual[p] = total % MOD
            else:
                for p in range(11):
                    right_actual[p] = sums[p][rc]
            for p in range(11):
                v = left_actual[p] + right_actual[p]
                if v >= MOD:
                    v -= MOD
                sums[p][node] = v
            dirty[node] = 0
        def ensure(node, l, r):
            if not dirty[node] or l == r:
                return
            mid = (l + r) >> 1
            ensure(node << 1, l, mid)
            ensure(node << 1 | 1, mid + 1, r)
            rebuild(node)
        def push(node):
            k = lazy[node]
            if k:
                lc = node << 1
                rc = lc | 1
                x = lazy[lc] + k
                if x >= MOD:
                    x -= MOD
                lazy[lc] = x
                x = lazy[rc] + k
                if x >= MOD:
                    x -= MOD
                lazy[rc] = x
                lazy[node] = 0
                dirty[node] = 1
        def update(node, l, r, ql, qr, k):
            if ql <= l and r <= qr:
                x = lazy[node] + k
                if x >= MOD:
                    x -= MOD
                lazy[node] = x
                return
            if lazy[node]:
                push(node)
            mid = (l + r) >> 1
            lc = node << 1
            rc = lc | 1
            if ql <= mid:
                update(lc, l, mid, ql, qr, k)
            if qr > mid:
                update(rc, mid + 1, r, ql, qr, k)
            dirty[node] = 1
        def query(node, l, r, ql, qr, p, add):
            if ql <= l and r <= qr:
                ensure(node, l, r)
                k = add + lazy[node]
                if k >= MOD:
                    k -= MOD
                if k == 0:
                    return sums[p][node]
                kp = [1] * (p + 1)
                for i in range(1, p + 1):
                    kp[i] = (kp[i - 1] * k) % MOD
                cp = C[p]
                total = 0
                for j in range(p + 1):
                    total += cp[j] * sums[j][node] * kp[p - j]
                return total % MOD
            new_add = add + lazy[node]
            if new_add >= MOD:
                new_add -= MOD
            mid = (l + r) >> 1
            res = 0
            if ql <= mid:
                res += query(node << 1, l, mid, ql, qr, p, new_add)
            if qr > mid:
                res += query(node << 1 | 1, mid + 1, r, ql, qr, p, new_add)
            return res % MOD
        for _ in range(q):
            typ = data[pos]
            pos += 1
            if typ == 1:
                i = data[pos] - 1
                k = data[pos + 1]
                pos += 2
                update(1, 0, n - 1, i, i, k % MOD)
            elif typ == 2:
                l = data[pos] - 1
                r = data[pos + 1] - 1
                k = data[pos + 2]
                pos += 3
                update(1, 0, n - 1, l, r, k % MOD)
            else:
                l = data[pos] - 1
                r = data[pos + 1] - 1
                p = data[pos + 2]
                pos += 3
                ans.append(
                    str(query(1, 0, n - 1, l, r, p, 0))
                )
    sys.stdout.write("\n".join(ans))

if __name__ == "__main__":
    solve()
