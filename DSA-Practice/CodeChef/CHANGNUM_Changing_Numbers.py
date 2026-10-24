"""
Problem   : Changing Numbers (CHANGNUM)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/CHANGNUM
Difficulty: 2013
Topics    : DSU, Graphs, Combinatorics
Date      : 2026-10-24

Approach:
  Treat each pair (X[i], Y[i]) as an edge and merge the endpoints with a
  Disjoint Set Union (path compression). For every component of size c made
  of values that actually appear in the pairs:
    - the minimum number of operations is c - 1, so the total is the sum of (c - 1)
    - the number of ways is c! per component, multiplied together
  If k == 1, print only the minimum operations. Otherwise also print
  (product of c!) * (total ops)! mod 1e9+7, which accounts for interleaving
  the operations across components. Factorials are precomputed once up to
  1e5+5 and fast input is read via sys.stdin.buffer.

Time  : O(P + N * alpha(N)) per test case, where P = 1e5 is the one-time
        factorial precompute
Space : O(N) per test case, plus O(P) for the factorial table
"""


# -------------------------------------------- Solution ------------------------------------------------------


import sys
def main():
    rd = sys.stdin.buffer.read().split()
    M = 10**9 + 7
    p = 0
    T = int(rd[p]); p += 1
    # factorials up to 1e5+5
    F = [1] * (100010)
    for q in range(1, 100010):
        F[q] = F[q - 1] * q % M
    out = []
    for _ in range(T):
        n = int(rd[p]); k = int(rd[p + 1]); p += 2
        X = rd[p:p + n]; p += n
        Y = rd[p:p + n]; p += n
        par = list(range(n + 1))
        seen = [False] * (n + 1)
        def root(v):
            r = v
            while par[r] != r:
                r = par[r]
            while par[v] != r:
                par[v], v = r, par[v]
            return r
        for i in range(n):
            u = int(X[i]); v = int(Y[i])
            seen[u] = True
            seen[v] = True
            ru = root(u); rv = root(v)
            if ru != rv:
                par[ru] = rv
        cnt = [0] * (n + 1)
        for v in range(1, n + 1):
            if seen[v]:
                cnt[root(v)] += 1
        ops = 0
        ways = 1
        for v in range(1, n + 1):
            c = cnt[v]
            if c:
                ops += c - 1
                ways = ways * F[c] % M
        if k == 1:
            out.append(str(ops))
        else:
            out.append("%d %d" % (ops, ways * F[ops] % M))
    print("\n".join(out))

main()
