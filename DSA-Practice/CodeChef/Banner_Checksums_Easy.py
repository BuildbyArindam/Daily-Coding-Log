"""
Platform   : CodeChef (START261A)
Problem    : Banner Checksums (Easy), EXBANNER2
Link       : https://www.codechef.com/START261A/problems/EXBANNER2
Date       : 2026-10-21
Difficulty : Medium
Topics     : Constructive, Parity/XOR, Randomization, Matrix

Approach:
  - Quick infeasibility check: the XOR of all row parities must equal the XOR
    of all column parities, otherwise print -1.
  - Build a base (n-1) x (m-1) grid from a periodic pattern (i + j + shift) % 3,
    with a few random bit flips for variety.
  - Fill the last column so each row meets its parity, then fill the last row
    so each column meets its parity. The corner cell is fixed by the last row.
  - Validate that no row or column is all 0s or all 1s. If invalid, retry with
    a new shift/flips (up to 4000 attempts, seeded RNG so output is deterministic).

Complexity (per test case):
  Time : O(A * n * m), where A is the number of attempts (a few in practice, 4000 max)
  Space: O(n * m)
"""


# ---------------------------------------------- Solution -------------------------------------------------------------


import sys, random as _R

def _build(n, m, px, qx, shift, flips, gen):
    g = [[1 if (i + j + shift) % 3 == 0 else 0 for j in range(m - 1)] + [0]
         for i in range(n - 1)]
    g.append([0] * m)
    for _ in range(flips):
        a = gen.randrange(n - 1)
        b = gen.randrange(m - 1)
        g[a][b] ^= 1
    for i in range(n - 1):
        row = g[i]
        row[m - 1] = px[i] ^ (sum(row[:m - 1]) & 1)
    last = g[n - 1]
    for j in range(m - 1):
        acc = 0
        for i in range(n - 1):
            acc ^= g[i][j]
        last[j] = qx[j] ^ acc
    last[m - 1] = px[n - 1] ^ (sum(last[:m - 1]) & 1)
    return g

def _valid(g, n, m):
    for r in g:
        s = sum(r)
        if s == 0 or s == m:
            return False
    for c in zip(*g):
        s = sum(c)
        if s == 0 or s == n:
            return False
    return True

def _solve_case(n, m, px, qx, gen):
    for t in range(4000):
        k = 0 if t == 0 else gen.randrange(1, 4)
        g = _build(n, m, px, qx, t % 3, k, gen)
        if _valid(g, n, m):
            return g
    return None

def main():
    tok = sys.stdin.buffer.read().split()
    cur = 1
    total = int(tok[0])
    gen = _R.Random(20260921)
    res = []
    for _ in range(total):
        n = int(tok[cur]); m = int(tok[cur + 1]); cur += 2
        px = [int(tok[cur + 3 * i]) for i in range(n)]
        cur += 3 * n
        qx = [int(tok[cur + 3 * j]) for j in range(m)]
        cur += 3 * m
        if (sum(px) ^ sum(qx)) & 1:
            res.append("-1")
            continue
        g = _solve_case(n, m, px, qx, gen)
        if g is None:
            res.append("-1")
        else:
            res.extend(" ".join(map(str, r)) for r in g)
    sys.stdout.write("\n".join(res) + "\n")

main()
