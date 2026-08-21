"""
Problem   : Even Grid
Platform  : HackerEarth
Link      : https://www.hackerearth.com/problem/algorithm/chocolates-39/
Difficulty: Easy
Topic     : Combinatorics (Binomial Coefficients / Modular Inverse)
Date      : 2026-08-21

Approach:
    For each test case with grid dimensions n x m, let k = n * m.
    The answer is C(2k, k) - 1 (mod 1e9+7) — the central binomial
    coefficient counting arrangements over 2k cells, minus 1 to
    exclude a degenerate/invalid case.

    Precompute factorials and modular inverse factorials up to
    MAX_VAL (2,000,000) once using Fermat's little theorem, so each
    nCr(n, r) query resolves in O(1).

Complexity:
    Precompute : O(MAX_VAL) time, O(MAX_VAL) space
    Per query  : O(1) time (after precompute)
    Overall    : O(MAX_VAL + T) time, O(MAX_VAL) space, where T = test cases
"""


# ---------------------- Solution -------------------------


import sys

MOD = 10**9 + 7
MAX_VAL = 2000000
fact = [1] * (MAX_VAL + 1)
inv = [1] * (MAX_VAL + 1)
for i in range(1, MAX_VAL + 1):
    fact[i] = (fact[i - 1] * i) % MOD
inv[MAX_VAL] = pow(fact[MAX_VAL], MOD - 2, MOD)
for i in range(MAX_VAL - 1, -1, -1):
    inv[i] = (inv[i + 1] * (i + 1)) % MOD

def nCr(n, r):
    if r < 0 or r > n:
        return 0
    return fact[n] * inv[r] % MOD * inv[n - r] % MOD

def main():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return
    t = int(lines[0].strip())
    out = []
    for line in lines[1:t+1]:
        if not line.strip():
            continue
        n, m = map(int, line.split())
        k = n * m
        ans = (nCr(2 * k, k) - 1 + MOD) % MOD
        out.append(str(ans))
        if len(out) >= 50000:
            sys.stdout.write('\n'.join(out) + '\n')
            out.clear()
    if out:
        sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    main()
