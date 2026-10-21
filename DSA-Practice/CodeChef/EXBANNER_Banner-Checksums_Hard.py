"""
Platform   : CodeChef (Starters 261, Div A)
Problem    : Banner Checksums (EXBANNER)
Link       : https://www.codechef.com/START261A/problems/EXBANNER
Date       : 2026-10-21
Difficulty : Hard
Topics     : Bit manipulation, Constructive, Greedy, Heap, Gale-Ryser-style matrix construction

Approach:
  Each bit is independent, so build the n x m grid one bit at a time.
  1. For every row/column, use its (XOR, OR, AND) bits to classify it:
       - all ones   (AND bit = 1)  -> needs XOR parity to match the line length
       - all zeros  (OR bit = 0)   -> needs XOR bit = 0
       - mixed                     -> needs at least 1 one and at least 1 zero,
                                      with a fixed parity of ones
     Reject on any contradiction (e.g. an all-ones row against an all-zeros column).
  2. Lines forced to all ones/zeros fix the border. For the mixed x mixed
     sub-grid, compute each line's minimum feasible count of ones, matching
     parity and clamped to the allowed range [lo, hi].
  3. Row and column totals must be equal. A min-heap bumps the smaller side
     by +2 (parity-preserving) until the sums match, or reports impossible.
  4. Realise the counts with the Gale-Ryser greedy: for each row, place its
     ones in the columns with the largest remaining demand.
  5. OR the per-bit results into the final values. If any bit fails, print -1.

Complexity (B = number of bits, about 30):
  Time  : O(B * (n + m + n * m log m)), where the n*m log m term is the
          per-row sort in the greedy fill
  Space : O(n * m) for the output grid, plus O(n + m) per-bit scratch
"""


# ------------------------------------------------ Solution ---------------------------------------------------------


import sys
from heapq import heapify as hfy, heappush as hpu, heappop as hpo

def raise_to(par, floor_, ceil_):
    w = par + 2 if par < floor_ else par
    return w if w <= ceil_ else None

def judge(xv, ov, av, bt, ln):
    px, po, pa = (xv >> bt) & 1, (ov >> bt) & 1, (av >> bt) & 1
    if pa:
        return (1, 0) if (po and px == (ln & 1)) else (-1, 0)
    if po == 0:
        return (0, 0) if px == 0 else (-1, 0)
    if ln < 2 or (px == 0 and ln < 3):
        return -1, 0
    return 2, px

def process_bit(bt, n, m, rows, cols, rbits, cbits, free):
    kinds_r, par_r = [], []
    for t in rows:
        k, p = judge(t[0], t[1], t[2], bt, m)
        if k < 0:
            return False
        kinds_r.append(k)
        par_r.append(p)
    kinds_c, par_c = [], []
    for t in cols:
        k, p = judge(t[0], t[1], t[2], bt, n)
        if k < 0:
            return False
        kinds_c.append(k)
        par_c.append(p)
    one_r, zero_r = kinds_r.count(1), kinds_r.count(0)
    one_c, zero_c = kinds_c.count(1), kinds_c.count(0)
    if (one_r and zero_c) or (zero_r and one_c):
        return False
    flag = 1 << bt
    for i, k in enumerate(kinds_r):
        if k == 1:
            rbits[i] |= flag
    for j, k in enumerate(kinds_c):
        if k == 1:
            cbits[j] |= flag
    mix_r = [i for i, k in enumerate(kinds_r) if k == 2]
    mix_c = [j for j, k in enumerate(kinds_c) if k == 2]
    a, b = len(mix_r), len(mix_c)
    r_lo = 0 if one_c else 1
    r_hi = b if zero_c else b - 1
    c_lo = 0 if one_r else 1
    c_hi = a if zero_r else a - 1
    need_r = []
    for i in mix_r:
        v = raise_to((par_r[i] - one_c) & 1, r_lo, r_hi)
        if v is None:
            return False
        need_r.append(v)
    need_c = []
    for j in mix_c:
        v = raise_to((par_c[j] - one_r) & 1, c_lo, c_hi)
        if v is None:
            return False
        need_c.append(v)
    s1, s2 = sum(need_r), sum(need_c)
    if s1 != s2:
        if s1 < s2:
            arr, lim, gap = need_r, r_hi, (s2 - s1) >> 1
        else:
            arr, lim, gap = need_c, c_hi, (s1 - s2) >> 1
        pq = [(val, idx) for idx, val in enumerate(arr) if val + 2 <= lim]
        hfy(pq)
        while gap > 0:
            if not pq:
                return False
            val, idx = hpo(pq)
            val += 2
            arr[idx] = val
            if val + 2 <= lim:
                hpu(pq, (val, idx))
            gap -= 1
    pool = [[need_c[q], mix_c[q]] for q in range(b)]
    for t in range(a):
        k = need_r[t]
        if not k:
            continue
        pool.sort(reverse=True)
        if k > b or pool[k - 1][0] <= 0:
            return False
        line = free[mix_r[t]]
        for q in range(k):
            pool[q][0] -= 1
            line[pool[q][1]] |= flag
    return all(p[0] == 0 for p in pool)

def main():
    tok = sys.stdin.buffer.read().split()
    ptr = 1
    res = []
    for _ in range(int(tok[0])):
        n, m = int(tok[ptr]), int(tok[ptr + 1])
        ptr += 2
        rows = [tuple(map(int, tok[ptr + 3 * i: ptr + 3 * i + 3])) for i in range(n)]
        ptr += 3 * n
        cols = [tuple(map(int, tok[ptr + 3 * j: ptr + 3 * j + 3])) for j in range(m)]
        ptr += 3 * m
        rbits, cbits = [0] * n, [0] * m
        free = [[0] * m for _ in range(n)]
        top = 0
        for t in rows + cols:
            top |= t[0] | t[1] | t[2]
        fine = True
        for bt in range(top.bit_length()):
            if not process_bit(bt, n, m, rows, cols, rbits, cbits, free):
                fine = False
                break
        if not fine:
            res.append("-1")
            continue
        for i in range(n):
            base, fr = rbits[i], free[i]
            res.append(" ".join(str(base | cbits[j] | fr[j]) for j in range(m)))
    sys.stdout.write("\n".join(res) + "\n")

main()
