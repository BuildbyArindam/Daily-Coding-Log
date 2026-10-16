"""
Problem   : Square String (SQING)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/SQING
Difficulty: 2002
Topics    : Math, Modular Arithmetic, Precomputation 
Date      : 2026-10-16

Approach:
    For each N, the answer is the sum over m = 1..N-1 of (N - m)^2 * m * 2^m (mod 1e9+7).
    Powers of 2 are precomputed once up to max(N) across all test cases,
    so each term costs O(1) with modular arithmetic.

Complexity:
    Time : O(max(N) + sum of N over all tests)
    Space: O(max(N)) for the powers-of-2 table
"""


# --------------------------------------------------- Solution ----------------------------------------------------


import sys

def main():
    MOD = 10**9 + 7
    tokens = sys.stdin.read().split()
    cases = [int(v) for v in tokens[1:1 + int(tokens[0])]]
    top = max(cases) + 1
    powers = [1] * (top + 1)
    for idx in range(1, top + 1):
        powers[idx] = (powers[idx - 1] << 1) % MOD
    results = []
    for n in cases:
        acc = 0
        for m in range(1, n):
            k = n - m
            acc = (acc + (k * k % MOD) * m % MOD * powers[m]) % MOD
        results.append(acc)
    sys.stdout.write("\n".join(map(str, results)) + "\n")

main()
