"""
Problem   : Distinct Numbers (DISTNUMS)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/DISTNUMS
Difficulty: 2015
Topics    : Mathematics, Prime Divisors, Number Theory, Integer Factorisation, Divisors
Date      : 2026-10-27

Approach:
  - Sieve primes up to 3200 once. Since 3200^2 > 10^7, trial division by these
    primes factorises n, and any leftover n > 1 is a single prime.
  - The answer is multiplicative over n = prod p^a. Each prime power contributes
    the geometric series sum_{i=a}^{a*2^k} p^i = (p^(a*2^k + 1) - p^a) / (p - 1)  (mod 1e9+7).
  - The exponent a*2^k + 1 is huge, so reduce it mod (M-1) using Fermat's little
    theorem (p is coprime to M). 2^k mod (M-1) is computed once per test case.
  - Divide by (p - 1) using the modular inverse (Fermat again).

Complexity:
  Time : O(T * (pi(3200) + w(n) * log M)), where pi(3200) is about 446 and w(n) is the
         number of distinct prime factors of n
  Space: O(T) for input/output, O(sqrt(max n)) for the sieve
"""


# --------------------------------------------- Solution ----------------------------------------------------


import sys

def main():
    M = 10**9 + 7
    PHI = M - 1
    lim = 3200
    flags = bytearray([1]) * (lim + 1)
    flags[0] = flags[1] = 0
    for i in range(2, int(lim ** 0.5) + 1):
        if flags[i]:
            flags[i * i::i] = bytearray(len(flags[i * i::i]))
    small = [i for i in range(lim + 1) if flags[i]]
    data = sys.stdin.read().split()
    t = int(data[0])
    out = []
    pos = 1

    def term(p, a, big):
        top = (a * big + 1) % PHI
        num = (pow(p, top, M) - pow(p, a, M)) % M
        return num * pow(p - 1, M - 2, M) % M

    for _ in range(t):
        n = int(data[pos]); k = int(data[pos + 1]); pos += 2
        big = pow(2, k, PHI)
        res = 1
        for q in small:
            if q * q > n:
                break
            if n % q == 0:
                c = 0
                while n % q == 0:
                    n //= q
                    c += 1
                res = res * term(q, c, big) % M
        if n > 1:
            res = res * term(n, 1, big) % M
        out.append(res)
    print("\n".join(map(str, out)))

main()
