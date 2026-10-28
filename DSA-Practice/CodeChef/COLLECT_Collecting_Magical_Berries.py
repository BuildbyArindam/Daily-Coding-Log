"""
Problem   : Collecting Magical Berries (COLLECT)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/COLLECT
Difficulty: 2017
Date      : 2026-10-28
Topics    : Fenwick Tree, Combinatorics, Range Sum Queries, Modular Arithmetic

Approach:
  - Keep a Fenwick tree (BIT) over the array for point updates and range sums.
  - For a query on [a, b], let s = range sum and k = b - a + 1. The answer is
    the number of ways to split s as evenly as possible over k slots:
    q = s // k, r = s % k, so (k - r) slots get q and r slots get q + 1.
        answer = s! * k! / ( (q!)^(k-r) * ((q+1)!)^r * r! * (k-r)! )  (mod MD)
  - MD = 3046201 is used as the prime modulus. Factorials are precomputed up to
    min(max(a) * n + 5, MD - 1), and division uses a modular inverse.
  - Factorial table is built with numpy: a row-wise cumulative product mod MD,
    then a prefix-product carry across rows.

Complexity:
  - Precompute: O(L), where L = min(max(a) * n, MD), vectorised with numpy
  - Update    : O(log n)
  - Query     : O(log n + log MD) (BIT sums plus modular exponentiation)
  - Space     : O(n + L)
"""


# -------------------------------------------- Solution ---------------------------------------------------------------


import sys
import numpy as np

MD = 3046201

def build_factorials(limit):
    width = 2048
    rows = (limit + 1 + width - 1) // width
    total = rows * width
    seq = np.arange(total, dtype=np.int64)
    seq[0] = 1
    seq %= MD
    grid = seq.reshape(rows, width)
    for col in range(1, width):
        grid[:, col] = grid[:, col] * grid[:, col - 1] % MD
    ends = grid[:, width - 1].tolist()
    carry = [1] * rows
    run = 1
    for i in range(rows):
        carry[i] = run
        run = run * ends[i] % MD
    mult = np.array(carry, dtype=np.int64).reshape(rows, 1)
    grid = grid * mult % MD
    return grid.reshape(-1).tolist()

def main():
    tok = sys.stdin.buffer.read().split()
    n = int(tok[0])
    vals = [0] + [int(x) for x in tok[1:1 + n]]
    q = int(tok[1 + n])
    pos = 2 + n
    bit = [0] * (n + 1)
    for i in range(1, n + 1):
        bit[i] += vals[i]
        j = i + (i & -i)
        if j <= n:
            bit[j] += bit[i]
    peak = max(max(vals), 30)
    lim = min(peak * n + 5, MD - 1)
    fact = build_factorials(lim)
    out = []
    for _ in range(q):
        cmd = tok[pos]
        a = int(tok[pos + 1])
        b = int(tok[pos + 2])
        pos += 3
        if cmd[0] == 99: 
            delta = b - vals[a]
            vals[a] = b
            i = a
            while i <= n:
                bit[i] += delta
                i += i & -i
        else:
            i = b
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & -i
            i = a - 1
            while i > 0:
                s -= bit[i]
                i -= i & -i
            k = b - a + 1
            qt, r = divmod(s, k)
            den = pow(fact[qt], k - r, MD) * pow(fact[qt + 1], r, MD) % MD
            den = den * fact[r] % MD * fact[k - r] % MD
            res = fact[s] * fact[k] % MD * pow(den, -1, MD) % MD
            out.append(res)
    sys.stdout.write("\n".join(map(str, out)) + ("\n" if out else ""))

main()
