"""
Problem   : Glass Measurement (GLASS)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/GLASS
Difficulty: 2004
Solved    : 2026-10-16
Topics    : Number Theory, Frobenius / Coin Problem, Residue-Class Shortest Path

Approach:
  A volume is measurable if it is a non-negative combination of the glass sizes.
  Let m = the smallest size. For each residue r mod m, compute least[r], the
  smallest constructible volume with that residue, using the round-robin
  algorithm. For each other size g, walk the cycles of r -> (r + g) % m twice,
  relaxing least[next] = min(least[next], least[cur] + g).
  - Largest non-measurable volume (Frobenius number) = max(least) - m,
    or -1 if some residue is unreachable (gcd > 1) or no volume is impossible.
  - Query value v is measurable iff least[v % m] <= v. The values
    v_i = (i*a + b) % c are generated and checked in bulk with NumPy.

Complexity:
  Time  : O(n * m) to build the table + O(q) for the queries (vectorised)
  Space : O(m + q), where m = smallest glass size
"""


# ----------------------------------------- Solution ------------------------------------------------------


import sys
from math import gcd
import numpy as np

BIG = 1 << 60

def read_tokens():
    return sys.stdin.buffer.read().split()

def build_table(sizes):
    """least[r] = smallest constructible volume with remainder r modulo min size."""
    base = sizes[0]
    least = [BIG] * base
    least[0] = 0
    for g in sizes[1:]:
        step = g % base
        span = gcd(base, step) if step else base
        if step == 0:
            continue
        ring = base // span
        for start in range(span):
            pos = start
            for _ in range(2 * ring):
                nxt = pos + step
                if nxt >= base:
                    nxt -= base
                cand = least[pos] + g
                if cand < least[nxt]:
                    least[nxt] = cand
                pos = nxt
    return least

def answer_queries(least, base, q, a, b, c):
    idx = np.arange(1, q + 1, dtype=np.int64)
    vals = (idx * a + b) % c
    table = np.array(least, dtype=np.int64)
    ok = table[vals % base] <= vals
    good = int(ok.sum())
    return q - good, good

def main():
    tok = read_tokens()
    p = 0
    t = int(tok[p]); p += 1
    out = []
    for _ in range(t):
        n = int(tok[p]); p += 1
        sizes = sorted(set(int(x) for x in tok[p:p + n]))
        p += n
        q = int(tok[p]); p += 1
        a, b, c = int(tok[p]), int(tok[p + 1]), int(tok[p + 2])
        p += 3
        base = sizes[0]
        least = build_table(sizes)
        worst = max(least)
        if worst >= BIG:     
            top = -1
        else:
            top = worst - base
            if top <= 0:
                top = -1
        bad, good = answer_queries(least, base, q, a, b, c)
        out.append(str(top))
        out.append(f"{bad} {good}")
    print("\n".join(out))

main()
