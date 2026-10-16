"""
Platform   : CodeChef
Problem    : Maximum Factors Problem (MXFACS)
Link       : https://www.codechef.com/problems/MXFACS
Difficulty : 2006
Date       : 2026-10-16
Topics     : Number Theory, Sieve of Eratosthenes, Divisors

Approach:
    For each N, find the proper divisor M (M != N) with the most divisors,
    breaking ties by the largest M, and print N // M.
    1. Sieve all primes up to 31623 (~sqrt(1e9)) once.
    2. Factorize N by testing only the primes that divide it. A NumPy mask
       finds them in one vectorized pass, and any leftover > 1 is a single
       prime factor.
    3. Expand the prime factorization into every divisor, tracking each
       divisor's own divisor count as the product of (exponent + 1).
    4. Pick the best divisor by (max count, then max value), skipping N itself.

Complexity (assuming N <= 1e9):
    Time  : O(sqrt(Nmax) log log sqrt(Nmax)) for the sieve, plus per test
            O(pi(sqrt(N)) + d(N)), where d(N) <= 1344
    Space : O(sqrt(Nmax) + d(N))
"""


# ---------------------------------------------- Solution ----------------------------------------------------


import sys
import numpy as np

def build_primes(limit):
    flags = bytearray([1]) * (limit + 1)
    flags[0] = flags[1] = 0
    i = 2
    while i * i <= limit:
        if flags[i]:
            flags[i * i::i] = bytearray(len(range(i * i, limit + 1, i)))
        i += 1
    return np.array([x for x in range(limit + 1) if flags[x]], dtype=np.int64)

def expand(factors):
    combos = [(1, 1)]
    for prime, power in factors:
        grown = []
        for val, cnt in combos:
            cur = val
            for e in range(power + 1):
                grown.append((cur, cnt * (e + 1)))
                cur *= prime
        combos = grown
    return combos

def factorize(num, primes):
    left = num
    result = []
    for p in primes[(left % primes) == 0].tolist():
        power = 0
        while left % p == 0:
            left //= p
            power += 1
        result.append((p, power))
    if left > 1:
        result.append((left, 1))
    return result

def solve_one(num, primes):
    best_cnt, best_m = 0, 1
    for val, cnt in expand(factorize(num, primes)):
        if val == num:
            continue
        if cnt > best_cnt or (cnt == best_cnt and val > best_m):
            best_cnt, best_m = cnt, val
    return num // best_m

def main():
    tokens = sys.stdin.read().split()
    primes = build_primes(31623)
    tests = int(tokens[0])
    answers = [str(solve_one(int(tokens[i]), primes)) for i in range(1, tests + 1)]
    sys.stdout.write("\n".join(answers) + "\n")

main()
