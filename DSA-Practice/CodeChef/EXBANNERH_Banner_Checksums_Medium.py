"""
Problem   : Banner Checksums (EXBANNERH), CodeChef Starters 261A
Link      : https://www.codechef.com/START261A/problems/EXBANNERH
Solved on : 2026-10-21
Difficulty: Medium
Topics    : Combinatorics, Inclusion-Exclusion, Modular Arithmetic

Approach:
  - Check parity feasibility first: (sum of row targets - sum of column
    targets) must be even, otherwise the answer is 0.
  - Count valid grids with inclusion-exclusion over the number of
    constrained rows (a) and columns (b) that violate their condition.
    Each term is a signed product of binomials (nCk) and a power of 2
    for the freely choosable cells.
  - Handle parity cases (n, m odd/even) and the boundary cases where all
    rows or all columns are forced, as separate correction terms.
  - Factorials, inverse factorials and powers of 2 are precomputed once,
    so every nCk and 2^k lookup is O(1).

Complexity (per test case):
  Time : O(n * m), dominated by the double loop over (a, b) for v in {0, 1}
  Space: O(n + m) for the inputs, plus O(MAX) one-time precomputation
         for factorial, inverse factorial and power-of-2 tables
"""


# --------------------------------------------- Solution ---------------------------------------------------------


import sys
def main():
    MOD = 10**9 + 7
    LIM = 100005
    P2 = [1] * LIM
    for i in range(1, LIM):
        P2[i] = P2[i - 1] * 2 % MOD
    FA = [1] * 25010
    for i in range(1, 25010):
        FA[i] = FA[i - 1] * i % MOD
    IV = [1] * 25010
    IV[-1] = pow(FA[-1], MOD - 2, MOD)
    for i in range(25009, 0, -1):
        IV[i - 1] = IV[i] * i % MOD
    def nck(a, b):
        if b < 0 or b > a:
            return 0
        return FA[a] * IV[b] % MOD * IV[a - b] % MOD
    data = sys.stdin.buffer.read().split()
    pos = 0
    t = int(data[pos]); pos += 1
    out = []
    for _ in range(t):
        n = int(data[pos]); m = int(data[pos + 1]); pos += 2
        R = []
        for i in range(n):
            R.append(int(data[pos])); pos += 3
        C = []
        for j in range(m):
            C.append(int(data[pos])); pos += 3
        r1 = sum(R); c1 = sum(C)
        if (r1 - c1) % 2:
            out.append(0); continue
        r0 = n - r1; c0 = m - c1
        mo = m & 1; no = n & 1
        sg = lambda k: -1 if k & 1 else 1
        ans = 0
        for a in range(n):
            g = nck(n, a) if mo else nck(r0, a) * P2[a] % MOD
            ans += sg(a) * g * P2[(n - a - 1) * (m - 1)]
        for b in range(1, m):
            g = nck(m, b) if no else nck(c0, b) * P2[b] % MOD
            ans += sg(b) * g * P2[(n - 1) * (m - b - 1)]
        if mo:
            if c1 in (0, m) and (c1 and 1) == r1 % 2:
                ans += sg(n)
        elif r0 == n and c1 in (0, m):
            ans += sg(n) * P2[n - 1]
        if no:
            if r1 in (0, n) and (r1 and 1) == c1 % 2:
                ans += sg(m)
        elif c0 == m and r1 in (0, n):
            ans += sg(m) * P2[m - 1]
        for v in (0, 1):
            Nv = (r1 if v else r0) if mo else r0
            Mv = (c1 if v else c0) if no else c0
            for a in range(1, n):
                ca = nck(Nv, a) * sg(a)
                if not ca:
                    continue
                s = 0
                for b in range(1, m):
                    s += nck(Mv, b) * sg(b) % MOD * P2[(n - a - 1) * (m - b - 1)]
                ans += ca * (s % MOD)
            rowsok = (Nv == n)
            colsok = (Mv == m)
            w = v if no else 0
            wr = v if mo else 0
            colsw = (c1 if w else c0) == m
            rowsw = (r1 if wr else r0) == n
            if rowsok and colsw:
                ans -= sg(n)
            if colsok and rowsw:
                ans += sg(m) * (-1 - sg(n))
        out.append(ans % MOD)
    print("\n".join(map(str, out)))
main()
