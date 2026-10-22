"""
Problem   : Avoiding M (Hard) - CodeChef AVOIDINGM2
Link      : https://www.codechef.com/problems/AVOIDINGM2
Platform  : CodeChef 
Difficulty: 2322
Date      : 2026-10-22
Topics    : Combinatorics, Inclusion-Exclusion, FFT/NTT-style Convolution,
            Divide & Conquer, Formal Power Series (Inverse)

Approach  :
  - Inclusion-exclusion over the m restricted values gives a closed form
    s_k = sum_j (-1)^(j+1) * C(m, j) * (n - j)^k.
  - Its generating function S(x) = sum_j c_j / (1 - a_j x) is built as a
    single fraction P/Q with a divide-and-conquer product tree.
  - The answer is [x^n] of P / (Q - x*P), computed with a Newton-iteration
    power-series inverse.
  - Convolutions mod 998244353 use numpy: a 15-bit split with direct
    np.convolve for small inputs, and a 3-way 10-bit split with float FFT
    (rfft/irfft) for large ones, to stay within double precision.

Complexity (per test):
  Time  : O(m log^2 m) for the product tree + O(n log n) for the inverse
  Space : O(n + m)
"""


# --------------------------------------------- Solution -----------------------------------------------------


import sys
import numpy as np

PR = 998244353

def conv(u, v):
    lu, lv = len(u), len(v)
    need = lu + lv - 1
    if min(lu, lv) <= 48:
        ul, uh = u & 32767, u >> 15
        vl, vh = v & 32767, v >> 15
        lo = np.convolve(ul, vl) % PR
        mid = (np.convolve(ul, vh) + np.convolve(uh, vl)) % PR
        hi = np.convolve(uh, vh) % PR
        return (lo + (mid << 15) + ((hi << 15) % PR << 15)) % PR
    sz = 1
    while sz < need:
        sz <<= 1
    fu = [np.fft.rfft((u >> s) & 1023, sz) for s in (0, 10, 20)]
    fv = [np.fft.rfft((v >> s) & 1023, sz) for s in (0, 10, 20)]
    comb = [
        fu[0] * fv[0],
        fu[0] * fv[1] + fu[1] * fv[0],
        fu[0] * fv[2] + fu[1] * fv[1] + fu[2] * fv[0],
        fu[1] * fv[2] + fu[2] * fv[1],
        fu[2] * fv[2],
    ]
    acc = None
    for t in reversed(comb):
        piece = np.rint(np.fft.irfft(t, sz)[:need]).astype(np.int64) % PR
        acc = piece if acc is None else (acc * 1024 + piece) % PR
    return acc

def series_inverse(d, cnt):
    g = np.array([pow(int(d[0]), PR - 2, PR)], dtype=np.int64)
    ln = 1
    while ln < cnt:
        ln *= 2
        t = conv(d[:ln], g)[:ln]
        t = (-t) % PR
        t[0] = (t[0] + 2) % PR
        g = conv(g, t)[:ln]
    return g[:cnt]

def build(n, m, fact, ifact):
    items = []
    for j in range(1, m + 1):
        c = fact[m] * ifact[j] % PR * ifact[m - j] % PR
        if j % 2 == 0:
            c = (PR - c) % PR
        a = (n - j) % PR
        items.append((np.array([c], dtype=np.int64),
                      np.array([1, (PR - a) % PR], dtype=np.int64)))
    while len(items) > 1:
        nxt = []
        for i in range(0, len(items) - 1, 2):
            p1, q1 = items[i]
            p2, q2 = items[i + 1]
            a1 = conv(p1, q2)
            a2 = conv(p2, q1)
            L = max(len(a1), len(a2))
            s = np.zeros(L, dtype=np.int64)
            s[:len(a1)] += a1
            s[:len(a2)] += a2
            nxt.append((s % PR, conv(q1, q2)))
        if len(items) & 1:
            nxt.append(items[-1])
        items = nxt
    return items[0]

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    top = 100005
    fact = [1] * top
    for i in range(1, top):
        fact[i] = fact[i - 1] * i % PR
    ifact = [1] * top
    ifact[-1] = pow(fact[-1], PR - 2, PR)
    for i in range(top - 1, 0, -1):
        ifact[i - 1] = ifact[i] * i % PR
    out = []
    for k in range(t):
        n = int(data[1 + 2 * k])
        m = int(data[2 + 2 * k])
        P, Q = build(n, m, fact, ifact)
        D = Q.copy()
        D[1:len(P) + 1] = (D[1:len(P) + 1] - P) % PR
        inv = series_inverse(D, n + 1)
        res = 0
        for i in range(min(len(P), n + 1)):
            res += int(P[i]) * int(inv[n - i])
        out.append(res % PR)
    print("\n".join(map(str, out)))

main()
