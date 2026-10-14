"""
Problem   : Merging (Hard) - CodeChef MERGEHD
Link      : https://www.codechef.com/problems/MERGEHD
Date      : 2026-10-14
Difficulty: Hard
Topics    : Combinatorics, FFT/Polynomial Multiplication, Prefix Maxima, Heap Merging 

Approach:
  1. Scan the array and record the positions where a new prefix maximum
     appears. These split the array into segments with lengths l_1..l_m
     that sum to n.
  2. The answer for each k in 0..n is the number of subsets of segments
     whose lengths sum to k, i.e. the coefficients of
     prod(1 + x^{l_i}) mod 998244353.
  3. Small n (<= 256): build the polynomial with a big-integer
     shift-and-add trick, packing coefficients into fixed-width byte slots.
  4. Large n: group equal lengths. A group of c segments of length l
     contributes sum_k C(c,k) x^{lk}. Segment lengths sum to n, so there
     are only O(sqrt(n)) distinct lengths. Multiply the group polynomials
     with a smallest-first heap, using FFT multiplication (15-bit split
     for exact mod arithmetic) and a naive path for tiny polynomials.

Time  : O(n log n * log sqrt(n)) per test for the large case, with FFT
        merging; O(m * n / word) for the small case.
Space : O(n) per test, plus O(MAXN) factorial tables.
"""


# ------------------------------------------------- Solution ----------------------------------------------------------------


import sys
import heapq
import numpy as np

MOD = 998244353
TOP = 200005
_SH = pow(2, 30, MOD)

fz = [1] * TOP
for _k in range(1, TOP):
    fz[_k] = fz[_k - 1] * _k % MOD
iz = [1] * TOP
iz[TOP - 1] = pow(fz[TOP - 1], MOD - 2, MOD)
for _k in range(TOP - 1, 0, -1):
    iz[_k - 1] = iz[_k] * _k % MOD

def small_case(seg, n):
    w = ((len(seg) + 1) + 7) // 8
    bits = w * 8
    cur = 1
    for l in seg:
        cur += cur << (l * bits)
    raw = cur.to_bytes((n + 1) * w, 'little')
    fb = int.from_bytes
    return [fb(raw[i * w:(i + 1) * w], 'little') % MOD for i in range(n + 1)]

def combine(a, b):
    la, lb = a.shape[0], b.shape[0]
    tot = la + lb - 1
    if la > lb:
        a, b = b, a
        la, lb = lb, la
    if la <= 24:
        res = np.zeros(tot, dtype=np.int64)
        for i, v in enumerate(a.tolist()):
            if v:
                res[i:i + lb] += b * v % MOD
        return res % MOD
    sz = 1 << (tot - 1).bit_length()
    rf, irf = np.fft.rfft, np.fft.irfft
    x0 = rf(a & 32767, sz)
    x1 = rf(a >> 15, sz)
    y0 = rf(b & 32767, sz)
    y1 = rf(b >> 15, sz)
    lo = np.rint(irf(x0 * y0, sz)[:tot]).astype(np.int64) % MOD
    mid = np.rint(irf(x0 * y1 + x1 * y0, sz)[:tot]).astype(np.int64) % MOD
    hi = np.rint(irf(x1 * y1, sz)[:tot]).astype(np.int64) % MOD
    return (lo + (mid << 15) + hi * _SH) % MOD

def big_case(seg, n):
    cnt = {}
    for l in seg:
        cnt[l] = cnt.get(l, 0) + 1
    pile = []
    uid = 0
    for l, c in cnt.items():
        arr = np.zeros(l * c + 1, dtype=np.int64)
        fc = fz[c]
        arr[::l] = [fc * iz[k] % MOD * iz[c - k] % MOD for k in range(c + 1)]
        pile.append((arr.shape[0], uid, arr))
        uid += 1
    heapq.heapify(pile)
    while len(pile) > 1:
        _, _, p = heapq.heappop(pile)
        _, _, q = heapq.heappop(pile)
        r = combine(p, q)
        uid += 1
        heapq.heappush(pile, (r.shape[0], uid, r))
    return pile[0][2].tolist()

def main():
    tok = sys.stdin.buffer.read().split()
    t = int(tok[0])
    p = 1
    res_lines = []
    for _ in range(t):
        n = int(tok[p])
        p += 1
        marks = []
        best = 0
        for idx in range(n):
            v = int(tok[p + idx])
            if v > best:
                best = v
                marks.append(idx)
        p += n
        marks.append(n)
        seg = [marks[k + 1] - marks[k] for k in range(len(marks) - 1)]
        if n <= 256:
            ans = small_case(seg, n)
        else:
            ans = big_case(seg, n)
        res_lines.append(' '.join(map(str, ans)))
    sys.stdout.write('\n'.join(res_lines) + '\n')

main()
