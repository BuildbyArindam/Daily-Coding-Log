"""
Problem   : Inversions II
Platform  : CodeChef
Link      : https://www.codechef.com/problems/INV2
Date      : 2026-09-04
Difficulty: Medium-Hard
Topics    : Combinatorics, Permutations, Inversion Counting,
            Factorials/Modular Inverse Factorial, Precomputation

Approach:
For each n, we count, over all n! permutations, how many produce a
strictly increasing final array after some inversion-based transform.
Precompute factorials and inverse factorials up to max_n (via Fermat's
little theorem, since MOD is prime) for O(1) nCr-style lookups.
Also precompute D[i] = i * (i-2) * (i-4) * ... (double-factorial-style
running product) to count arrangements for each inversion-count bucket
k in [0, 2n-2]. For k <= n, cnt = D[k-1]; for k > n, cnt uses
fact[n] * invfact[r] * D[r-1] with r = 2n-k (symmetric reduction).
Answer per n = sum over k of (total permutations - cnt) mod MOD.

Time Complexity : O(max_n + sum(n)) — factorial/invfact/D arrays built
                  once up to max_n, then O(n) per test case.
Space Complexity: O(max_n) for fact, invfact, and D arrays.
"""


# --------------------------- Solution -------------------------------


import sys
MOD = 998244353

def solve():
    input = sys.stdin.readline
    T = int(input())
    ns = [int(input()) for _ in range(T)]
    max_n = max(ns)
    fact = [1] * (max_n + 1)
    for i in range(1, max_n + 1):
        fact[i] = fact[i - 1] * i % MOD
    invfact = [1] * (max_n + 1)
    invfact[max_n] = pow(fact[max_n], MOD - 2, MOD)
    for i in range(max_n, 0, -1):
        invfact[i - 1] = invfact[i] * i % MOD
    D = [1] * (max_n + 1)
    for i in range(2, max_n + 1):
        D[i] = D[i - 2] * i % MOD
    out = []
    for n in ns:
        total = fact[n]
        ans = 0
        for k in range(2 * n - 1):
            if k == 0:
                cnt = 1
            elif k <= n:
                cnt = D[k - 1]
            else:
                r = 2 * n - k
                cnt = fact[n] * invfact[r] % MOD
                cnt = cnt * D[r - 1] % MOD
            ans = (ans + total - cnt) % MOD
        out.append(str(ans))
    print("\n".join(out))

if __name__ == "__main__":
    solve()
