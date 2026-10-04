"""
Problem   : Witua and Math (CodeChef - WITMATH)
Link      : https://www.codechef.com/problems/WITMATH
Difficulty: 1804
Date      : 2026-10-04
Topics    : Number Theory, Primality Checking, Miller-Rabin

Approach:
    For each N, the answer is the largest prime <= N. Prime gaps are small
    (about ln N on average), so I walk down from N (odd candidates only) and
    test each with a deterministic Miller-Rabin using the 7-base set
    {2, 325, 9375, 28178, 450775, 9780504, 1795265022}, which is exact for
    all n < 2^64. A small-prime trial division filters most composites
    before the modular exponentiation, and repeated N values are memoized.

Complexity (per test case):
    Time : O(G * k * log N), where G is the number of candidates checked
           (about ln N / 2 on average), k = 7 bases
    Space: O(T) for the memo dict, O(1) extra for the primality test
"""


# ------------------------------------- Solution ----------------------------------------------------


import sys

BASES = (2, 325, 9375, 28178, 450775, 9780504, 1795265022)
SMALL_PRIMES = (
    2, 3, 5, 7, 11, 13, 17, 19,
    23, 29, 31, 37, 41, 43, 47
)

def is_prime(n):
    """Deterministic primality test for n < 2^64."""
    if n < 2:
        return False
    for p in SMALL_PRIMES:
        if n % p == 0:
            return n == p
    d = n - 1
    s = 0
    while (d & 1) == 0:
        d >>= 1
        s += 1
    for a in BASES:
        if a % n == 0:
            continue
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return False
    return True

def largest_prime_at_most(n):
    if n <= 2:
        return 2
    if n % 2 == 0:
        n -= 1
    while not is_prime(n):
        n -= 2
    return n

def solve():
    input = sys.stdin.readline
    T = int(input())
    answers = {}
    out = []
    for _ in range(T):
        n = int(input())
        if n not in answers:
            answers[n] = largest_prime_at_most(n)
        out.append(str(answers[n]))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
