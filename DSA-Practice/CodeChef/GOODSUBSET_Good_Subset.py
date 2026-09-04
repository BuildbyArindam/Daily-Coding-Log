"""
Problem   : Good Subset (GOODSUBSET)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/GOODSUBSET
Date      : 2026-09-04
Difficulty: Hard
Topics    : Combinatorics, Prefix Sums, Modular Arithmetic, Inclusion-Exclusion,
            Bit Manipulation (power-of-two grouping)

Approach:
    For a set to be "good", every pair x < y must satisfy x XOR y < x AND y,
    which restricts valid pairs to elements lying in the same
    "power-of-two block" [2^k, 2^(k+1) - 1] (same highest set bit).
    So elements from different blocks can never coexist in a good subset
    unless we're picking at most one such crossing structure — the counting
    is done via complementary counting per subset size k:
        answer(N) = sum over k of [ 2^N - (# size-k subsets that are "bad") ]
    where "bad" subsets of size k are built from a running product of
    per-block combinatorial contributions (pref[]), using precomputed
    factorials / inverse factorials / powers of two mod 998244353.

Time complexity : O(N log N) per test (dominated by factorial precompute
                   up to max_n, plus O(log N) groups each processed in O(1)
                   amortized per k), O(sum N log N) overall.
Space complexity: O(max_n) for factorial / inverse factorial / power-of-two
                   tables.
"""


# -------------------------- Solution -------------------------------


import sys
MOD = 998244353
def solve():
    input = sys.stdin.readline
    T = int(input())
    tests = [int(input()) for _ in range(T)]
    max_n = max(tests)
    fact = [1] * (max_n + 1)
    for i in range(1, max_n + 1):
        fact[i] = fact[i - 1] * i % MOD
    inv_fact = [1] * (max_n + 1)
    inv_fact[max_n] = pow(fact[max_n], MOD - 2, MOD)
    for i in range(max_n, 0, -1):
        inv_fact[i - 1] = inv_fact[i] * i % MOD
    pow2 = [1] * (max_n + 1)
    for i in range(1, max_n + 1):
        pow2[i] = pow2[i - 1] * 2 % MOD
    def comb(n, r):
        if r < 0 or r > n:
            return 0
        return fact[n] * inv_fact[r] % MOD * inv_fact[n - r] % MOD
    def solve_one(N):
        groups = []
        left = 1
        while left <= N:
            right = min(2 * left - 1, N)
            groups.append(right - left + 1)
            left *= 2
        max_group = max(groups)
        pref = [1] * len(groups)
        total_subsets = pow2[N]
        ans = 0
        for k in range(1, max_group + 1):
            if k > 1:
                r = k - 1
                for i, c in enumerate(groups):
                    if r <= c:
                        pref[i] += comb(c, r)
                        if pref[i] >= MOD:
                            pref[i] -= MOD
            bad = 1
            for value in pref:
                bad = bad * value % MOD
            ans += total_subsets - bad
            ans %= MOD
        return ans
    out = []
    for N in tests:
        out.append(str(solve_one(N)))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
