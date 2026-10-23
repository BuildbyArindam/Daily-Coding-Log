"""
Platform   : CodeChef
Problem    : Permutation Counting (Easy), PERMCNTEZ
Link       : https://www.codechef.com/problems/PERMCNTEZ
Difficulty : 2011
Date       : 2026-10-23
Topics     : Combinatorics, Stars and Bars, Modular Arithmetic

Approach:
  Group the numbers 1..N by residue mod 3 (K = 3), giving counts
  z (residue 0), a (residue 1) and b (residue 2).
  The residue-0 elements act as separators, and the gaps between them
  (plus optionally one or both ends) must be non-empty blocks.
  - e = number of ends used (0, 1 or 2), with multiplicity 1, 2, 1.
  - m = z - 1 + e blocks in total.
  - Pick j of the m blocks to hold residue-1 elements; the other m - j
    hold residue-2 elements.
  - Split a into j non-empty parts and b into m - j non-empty parts
    (stars and bars: C(a-1, j-1) and C(b-1, m-j-1)).
  - Multiply the total by z! * a! * b! to assign the actual values.
  All answers are taken mod 998244353, using precomputed factorials
  and inverse factorials.

Time  : O(LIM) precomputation + O(N) per test, so O(sum of N) overall
Space : O(LIM) for the factorial tables
"""


# ------------------------------------------ Solution ----------------------------------------------------------


import sys
MD = 998244353
LIM = 200010

def build():
    f = [1] * LIM
    for i in range(2, LIM):
        f[i] = f[i - 1] * i % MD
    g = [1] * LIM
    g[LIM - 1] = pow(f[LIM - 1], MD - 2, MD)
    for i in range(LIM - 1, 1, -1):
        g[i - 1] = g[i] * i % MD
    return f, g

FACT, IFACT = build()

def nCr(n, r):
    if r < 0 or n < 0 or r > n:
        return 0
    return FACT[n] * IFACT[r] % MD * IFACT[n - r] % MD

def parts(total, k):
    if total == 0:
        return 1 if k == 0 else 0
    if k <= 0:
        return 0
    return nCr(total - 1, k - 1)

def solve(n):
    zeros = n // 3
    ones = (n + 2) // 3
    twos = (n + 1) // 3
    if zeros == 0:
        return 0
    acc = 0
    for e, mult in ((0, 1), (1, 2), (2, 1)):
        m = zeros - 1 + e
        sub = 0
        lo = max(0, m - twos)
        hi = min(m, ones)
        for j in range(lo, hi + 1):
            w = parts(ones, j)
            if w == 0:
                continue
            w2 = parts(twos, m - j)
            if w2 == 0:
                continue
            sub = (sub + nCr(m, j) * w % MD * w2) % MD
        acc = (acc + mult * sub) % MD
    return acc * FACT[zeros] % MD * FACT[ones] % MD * FACT[twos] % MD

def main():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    p = 1
    for _ in range(t):
        n = int(data[p])
        p += 2  # skip K (always 3)
        out.append(solve(n))
    sys.stdout.write("\n".join(map(str, out)) + "\n")

main()
