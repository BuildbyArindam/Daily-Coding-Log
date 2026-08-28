"""
Problem   : Number With The Given Amount Of Divisors
Link      : https://codeforces.com/problemset/problem/27/E
Date      : 2026-08-28
Difficulty: *2000 (Codeforces)
Topics    : Brute Force, DP, Number Theory

Approach:
    Find the smallest positive integer with exactly n divisors.
    Since 2*3*5*...*53 (first 16 primes) already exceeds 10^18, at most 15-16
    distinct primes can appear in the factorization. We DFS over primes in
    increasing order, trying exponents from 1 upward (exponents must be
    non-increasing across primes in the optimal answer, enforced via max_exp),
    and prune whenever the partial product exceeds LIMIT or already exceeds
    the current best answer. A branch is only explored when the remaining
    divisor count is evenly divisible by (exp + 1), since divisor count is
    multiplicative: d(n) = product(exp_i + 1).

Time complexity : Bounded search tree over ~15 primes with exponents up to
                   ~59 (for base 2), heavily pruned by the LIMIT and
                   "remaining % (exp+1) == 0" checks. Effectively runs in a
                   small fraction of a second for n up to 10^9.
Space complexity : O(depth) = O(number of primes tried) for the recursion
                   stack, i.e. O(16).
"""


# ----------------------------------- Solution ---------------------------------------


import sys
LIMIT = 10**18
PRIMES = [
    2, 3, 5, 7, 11, 13, 17, 19,
    23, 29, 31, 37, 41, 43, 47, 53
]
n = int(sys.stdin.readline())
if n == 1:
    print(1)
    sys.exit()
answer = LIMIT

def dfs(pos, remaining, max_exp, current):
    global answer
    if remaining == 1:
        answer = min(answer, current)
        return
    if pos >= len(PRIMES):
        return
    p = PRIMES[pos]
    value = current
    for exp in range(1, max_exp + 1):
        if value > LIMIT // p:
            break
        value *= p
        if remaining % (exp + 1) == 0:
            if value < answer:
                dfs(
                    pos + 1,
                    remaining // (exp + 1),
                    exp,
                    value
                )
dfs(0, n, 59, 1)

print(answer)
