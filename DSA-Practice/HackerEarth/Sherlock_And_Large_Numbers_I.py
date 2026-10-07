"""
Problem   : Sherlock And Large Numbers - I
Platform  : HackerEarth
Link      : https://www.hackerearth.com/problem/algorithm/sherlock-and-large-numbers-i-59d689d3/
Difficulty: Medium
Topics    : Prime Factorization, Number Theory
Date      : 2026-10-07

Approach:
  - Precompute the smallest prime factor (SPF) for every value up to 10^6
    with a sieve, so any number can be factorized in O(log x).
  - For each test case, factorize every number in the numerator list and
    add its prime exponents to a dict; factorize every number in the
    denominator list and subtract its exponents.
  - Primes with a positive net exponent form the reduced numerator P;
    primes with a negative net exponent form the reduced denominator Q.
    Each is built with modular exponentiation (mod 1e9+7).

Complexity:
  Time  : O(V log log V) for the sieve, plus O((n + m) log V) per test case
          (V = 10^6), plus O(k log E) for the pow() calls (k = distinct primes).
  Space : O(V) for the SPF array, plus O(k) for the exponent dict per test.
"""


# -------------------------------------- Solution -------------------------------------------------


import sys
from array import array

MOD = 1000000007
MAXV = 1000000

def build_spf(limit):
    spf = array('I', range(limit + 1))
    if limit >= 1:
        spf[1] = 1
    i = 2
    while i * i <= limit:
        if spf[i] == i: 
            j = i * i
            while j <= limit:
                if spf[j] == j:
                    spf[j] = i
                j += i
        i += 1
    return spf
spf = build_spf(MAXV)

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    T = data[idx]
    idx += 1
    output = []
    for _ in range(T):
        n = data[idx]
        m = data[idx + 1]
        idx += 2
        diff = {}
        for _ in range(n):
            x = data[idx]
            idx += 1
            while x > 1:
                p = spf[x]
                cnt = 0
                while x % p == 0:
                    x //= p
                    cnt += 1
                diff[p] = diff.get(p, 0) + cnt
        for _ in range(m):
            x = data[idx]
            idx += 1
            while x > 1:
                p = spf[x]
                cnt = 0
                while x % p == 0:
                    x //= p
                    cnt += 1
                diff[p] = diff.get(p, 0) - cnt
        ans_p = 1
        ans_q = 1
        for prime, d in diff.items():
            if d > 0:
                ans_p = (ans_p * pow(prime, d, MOD)) % MOD
            elif d < 0:
                ans_q = (ans_q * pow(prime, -d, MOD)) % MOD
        output.append(f"{ans_p} {ans_q}")
    sys.stdout.write("\n".join(output))

if __name__ == "__main__":
    solve()
