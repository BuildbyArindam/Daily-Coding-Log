"""
Problem   : MEX Game (Hard) - MEXGAME2
Platform  : CodeChef (START258B)
Link      : https://www.codechef.com/START258B/problems/MEXGAME2
Solved on : 2026-09-30
Difficulty: Hard
Topics    : MEX, Prefix Sums, Parity/XOR, Counting Subarrays

Approach:
  - Precompute prefix parities of (A[i] & 1) and prefix counts of the
    resulting bits, so any range can be summed in O(1).
  - Fix the left endpoint L (iterating right to left) and maintain nxt[v],
    the next index of value v. For each MEX value m, the valid right
    endpoints form a contiguous range [lo, hi] derived from
    nxt[0..m-1] (all present) and nxt[m] (absent).
  - For odd m, the contribution is a direct prefix-count lookup. For even m,
    use the precomputed per-threshold (2k) parity/prefix tables.
  - Add up the counted subarrays over all (L, m) pairs.

Time      : O(n * C) per test, C ~ 100 (bounded by max value / MEX range)
Space     : O(n * C/2) for the per-threshold prefix tables
"""


# ----------------------------------- Solution --------------------------------------------------------


import sys

def main():
    raw = sys.stdin.buffer.read().split()
    ptr = 0
    tc = int(raw[ptr]); ptr += 1
    answers = []
    for _case in range(tc):
        n = int(raw[ptr]); ptr += 1
        vals = raw[ptr:ptr + n]; ptr += n
        A = [0] * (n + 1)
        for idx in range(1, n + 1):
            A[idx] = int(vals[idx - 1])
        par = [0] * (n + 1)
        onesCnt = [0] * (n + 1)
        acc = 0
        for idx in range(1, n + 1):
            acc += (par[idx - 1] ^ (A[idx] & 1))
            par[idx] = par[idx - 1] ^ (A[idx] & 1)
            onesCnt[idx] = onesCnt[idx - 1] + par[idx]
        HALF = 51
        cfByK = [None] * HALF
        hOnesByK = [None] * HALF
        for k in range(HALF):
            th = 2 * k
            cfRow = [0] * (n + 1)
            hRow = [0] * (n + 1)
            curCF = 0
            curH = 0
            for idx in range(1, n + 1):
                if A[idx] > th:
                    curCF ^= 1
                cfRow[idx] = curCF
                bit = par[idx] ^ curCF
                curH += bit
                hRow[idx] = curH
            cfByK[k] = cfRow
            hOnesByK[k] = hRow
        nxt = [n + 1] * 101
        grandTotal = 0
        for L in range(n, 0, -1):
            nxt[A[L]] = L
            ceil_ = L - 1
            for m in range(0, 102):
                if m:
                    prev = nxt[m - 1] if m - 1 <= 100 else n + 1
                    if prev > ceil_:
                        ceil_ = prev
                lo = ceil_ if ceil_ > L else L
                if lo > n:
                    break
                if m == 101:
                    hi = n
                else:
                    hi = nxt[m] - 1
                    if hi > n:
                        hi = n
                if lo > hi:
                    continue
                constBit = (m * (m - 1) // 2) & 1
                base = par[L - 1] ^ constBit
                segLen = hi - lo + 1
                if m & 1:
                    wantOne = base ^ 1
                    onesHere = onesCnt[hi] - onesCnt[lo - 1]
                    grandTotal += onesHere if wantOne else (segLen - onesHere)
                else:
                    k = m >> 1
                    cfPoint = cfByK[k][L - 1]
                    wantOne = base ^ cfPoint ^ 1
                    onesHere = hOnesByK[k][hi] - hOnesByK[k][lo - 1]
                    grandTotal += onesHere if wantOne else (segLen - onesHere)
        answers.append(grandTotal)
    sys.stdout.write('\n'.join(map(str, answers)) + '\n')

main()
