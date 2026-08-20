"""
Problem   : Update Queries (UPDQS)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/UPDQS
Solved on : 2026-08-20

Difficulty (best-effort, not scraped from CodeChef): Medium-Hard
Topics     (best-effort): Fenwick Tree / BIT, Order Statistics via BIT,
                           Coordinate Compression, Difference Arrays, Offline Processing

Approach:
  - Maintain D[i] = A[i] - A[i-1], the consecutive-difference array of A.
  - The query answer is N*A[0] + Σ (D values, sorted ascending, weighted
    by descending rank), i.e. the smallest difference gets weight (N-1),
    the largest gets weight 1 -- a rank-weighted sum, not a positional one.
  - Since values can repeat/shift across updates, pre-collect every
    difference value that will ever appear (original diffs + all values
    induced by future queries) and coordinate-compress them once, offline.
  - Maintain two Fenwick trees over compressed ranks:
      cnt[] -> count of each value currently present in D
      sm[]  -> sum of values currently present in D
    This supports, for any value v, "sum of and count of all D-values < v"
    in O(log N), which is exactly what's needed to remove v's old
    contribution to the rank-weighted sum and insert its new one.
  - Each point update touches at most 2 entries of D (its neighbors),
    each handled by one `replace(old, new)` call in O(log N).

Complexity:
  Time  : O((N + Q) log N) per test case
          (coordinate compression + 2 Fenwick trees, O(log N) per update)
  Space : O(N + Q) for the array, difference array, and compressed coords
"""


# ---------------------------- Solution ------------------------------


import sys

class Fenwick:
    __slots__ = ("n", "bit")
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)
    def add(self, i, x):
        n = self.n
        bit = self.bit
        while i <= n:
            bit[i] += x
            i += i & -i
    def sum(self, i):
        bit = self.bit
        s = 0
        while i > 0:
            s += bit[i]
            i -= i & -i
        return s

def solve():
    input = sys.stdin.buffer.readline
    T = int(input())
    out = []
    for _ in range(T):
        N, Q = map(int, input().split())
        A = list(map(int, input().split()))
        queries = []
        for _ in range(Q):
            i, x = map(int, input().split())
            queries.append((i - 1, x))
        sim = A[:]
        coords = set()
        for j in range(1, N):
            coords.add(sim[j] - sim[j - 1])
        for idx, x in queries:
            if idx == 0:
                new_d = sim[1] - x
                coords.add(new_d)
            elif idx == N - 1:
                new_d = x - sim[N - 2]
                coords.add(new_d)
            else:
                coords.add(x - sim[idx - 1])
                coords.add(sim[idx + 1] - x)
            sim[idx] = x
        vals = sorted(coords)
        rank = {v: i + 1 for i, v in enumerate(vals)}
        M = len(vals)
        cnt = Fenwick(M)
        sm = Fenwick(M)
        D = [A[i] - A[i - 1] for i in range(1, N)]
        m = N - 1
        D_sorted = sorted(D)
        weighted = 0
        for j, v in enumerate(D_sorted):
            weighted += v * (m - j)
        total_diff_sum = sum(D)
        for v in D:
            r = rank[v]
            cnt.add(r, 1)
            sm.add(r, v)
        def replace(old, new):
            nonlocal weighted
            if old == new:
                return
            ro = rank[old]
            less_cnt = cnt.sum(ro - 1)
            less_sum = sm.sum(ro - 1)
            weighted -= old * (m - less_cnt) + less_sum
            cnt.add(ro, -1)
            sm.add(ro, -old)
            rn = rank[new]
            less_cnt = cnt.sum(rn - 1)
            less_sum = sm.sum(rn - 1)
            weighted += new * (m - less_cnt) + less_sum
            cnt.add(rn, 1)
            sm.add(rn, new)
        for idx, x in queries:
            oldA = A[idx]
            if idx == 0:
                old_d = D[0]
                new_d = A[1] - x
                replace(old_d, new_d)
                D[0] = new_d
                A[0] = x
            elif idx == N - 1:
                old_d = D[N - 2]
                new_d = x - A[N - 2]
                replace(old_d, new_d)
                D[N - 2] = new_d
                A[N - 1] = x
            else:
                old_left = D[idx - 1]
                old_right = D[idx]
                new_left = x - A[idx - 1]
                new_right = A[idx + 1] - x
                replace(old_left, new_left)
                replace(old_right, new_right)
                D[idx - 1] = new_left
                D[idx] = new_right
                A[idx] = x
            ans = N * A[0] + weighted
            out.append(str(ans))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
