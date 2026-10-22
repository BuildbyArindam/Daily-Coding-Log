"""
Problem   : Avoiding M (Easy) - CodeChef (AVOIDINGM)
Link      : https://www.codechef.com/problems/AVOIDINGM
Difficulty: 2048
Topics    : Combinatorics, Inclusion-Exclusion, DP 
Date      : 2026-10-22

Approach:
  1. Inclusion-exclusion: f[L] = sum_{j=1..m} (-1)^(j+1) * C(m, j) * (n - j)^L
     counts the length-L segments that satisfy the condition.
     Binomials come from precomputed factorials and inverse factorials mod p.
  2. Combine segments with the DP
     h[i] = f[i] + sum_{j<i} f[j] * h[i-1-j]   (mod 998244353)
     and the answer is h[n].
  3. The DP convolution uses numpy dot products. f is split into 15-bit
     halves (lo/hi) so every partial dot product stays inside int64.

Complexity (per test case):
  Time : O(n*m) for the f[] table + O(n^2) for the DP (vectorised with numpy)
  Space: O(n + m)
"""


# ---------------------------------------------- Solution -------------------------------------------------------------


import sys
import numpy as np

MD = 998244353

def main():
    tok = sys.stdin.read().split()
    t = int(tok[0])
    out = []
    for k in range(t):
        out.append(str(calc(int(tok[1 + 2 * k]), int(tok[2 + 2 * k]))))
    print("\n".join(out))

def calc(n, m):
    f = seg_counts(n, m)
    lo = f & 32767
    hi = f >> 15
    h = np.zeros(n + 1, dtype=np.int64)
    h[0] = 1
    for i in range(1, n + 1):
        r = h[i - 1::-1]
        a = int(np.dot(lo[:i], r)) % MD
        b = int(np.dot(hi[:i], r)) % MD
        h[i] = (int(f[i]) + a + (b << 15)) % MD
    return int(h[n])

def seg_counts(n, m):
    fac = [1] * (m + 1)
    for i in range(1, m + 1):
        fac[i] = fac[i - 1] * i % MD
    ifc = [1] * (m + 1)
    ifc[m] = pow(fac[m], MD - 2, MD)
    for i in range(m, 0, -1):
        ifc[i - 1] = ifc[i] * i % MD
    cf = np.array([fac[m] * ifc[j] % MD * ifc[m - j] % MD * (1 if j & 1 else MD - 1) % MD
                   for j in range(1, m + 1)], dtype=np.int64)
    bs = n - np.arange(1, m + 1, dtype=np.int64)
    pw = np.ones(m, dtype=np.int64)
    res = np.zeros(n + 1, dtype=np.int64)
    for L in range(n + 1):
        res[L] = int((cf * pw % MD).sum() % MD)
        pw = pw * bs % MD
    return res

main()
