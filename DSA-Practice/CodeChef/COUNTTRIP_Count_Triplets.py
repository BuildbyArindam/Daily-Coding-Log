"""
Platform   : CodeChef
Problem    : Count Triplets (COUNTTRIP)
Link       : https://www.codechef.com/problems/COUNTTRIP
Difficulty : 2011
Topics     : Math, Observation, NumPy
Date       : 2026-10-23

Approach:
  - Iterate over the index gap g = j - i, capped at min(n - 1, 99).
  - For each g, vectorize over all pairs (i, i + g) with NumPy and compute
    diff = |A[i] - A[j]| - g.
  - diff == 0: the pair contributes (g + 1) valid choices.
  - diff > 0 and even: the third index sits at distance diff/2 on the left
    of i or the right of j, so count each side that stays within bounds.
  - Each pair is counted in both orientations (part << 1), and n is added
    as the base count for the degenerate single-index case.

Complexity:
  Time  : O(n * min(n, 99)) per test case, vectorized per gap
  Space : O(n)
"""


# ----------------------------------------- Solution --------------------------------------------------------------


import sys
import numpy as np

def solve_one(vals):
    size = len(vals)
    arr = np.array(vals, dtype=np.int64)
    ans = size
    for gap in range(1, min(size - 1, 99) + 1):
        left = np.arange(size - gap)
        diff = np.abs(arr[:size - gap] - arr[gap:]) - gap
        part = int((diff == 0).sum()) * (gap + 1)
        sel = (diff > 0) & ((diff & 1) == 0)
        if sel.any():
            step = diff[sel] >> 1
            base = left[sel]
            part += int((base >= step).sum())
            part += int((base + gap + step < size).sum())
        ans += part << 1
    return ans

def main():
    tokens = sys.stdin.buffer.read().split()
    cases = int(tokens[0])
    cur = 1
    res = []
    while cases:
        cases -= 1
        n = int(tokens[cur])
        chunk = list(map(int, tokens[cur + 1:cur + 1 + n]))
        cur += n + 1
        res.append(str(solve_one(chunk)))
    print("\n".join(res))

main()
