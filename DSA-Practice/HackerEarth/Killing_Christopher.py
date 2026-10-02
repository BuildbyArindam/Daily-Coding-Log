"""
Problem   : Killing Christopher
Platform  : HackerEarth
Link      : https://www.hackerearth.com/problem/algorithm/killing-cristopher/
Difficulty: Easy
Topics    : Number Theory, Sieve of Eratosthenes, Sum of Two Squares
Date      : 2026-10-02

Approach:
    Count the unordered ways to write n as a^2 + b^2 (0 <= a <= b).
    1. Sieve primes up to 10^6 once.
    2. Factorize n by trial division over the primes. By the sum-of-two-squares
       theorem, if any prime p ≡ 3 (mod 4) has an odd exponent, the answer is 0.
       Otherwise r2(n) = 4 * prod(e + 1) over primes p ≡ 1 (mod 4), where r2
       counts ordered signed pairs (a, b).
    3. Convert r2 to unordered non-negative pairs with Burnside's lemma:
       (r2 + 4*[n is a perfect square] + 4*[n/2 is a perfect square]) / 8.
       The correction terms cover the points on the axes and the diagonals.

Complexity:
    Time : O(L log log L) for the sieve (L = 10^6), then about
           O(sqrt(n) / ln(sqrt(n))) per query (trial division by primes only).
    Space: O(L) for the sieve and the prime list.
"""


# ------------------------------------ Solution -----------------------------------------------------


import sys
import math

LIMIT = 10**6
sieve = bytearray(b'\x01') * (LIMIT + 1)
sieve[0] = sieve[1] = 0
for i in range(2, math.isqrt(LIMIT) + 1):
    if sieve[i]:
        sieve[i * i:LIMIT + 1:i] = b'\x00' * (
            ((LIMIT - i * i) // i) + 1
        )
primes = [i for i in range(2, LIMIT + 1) if sieve[i]]

def count_ways(n):
    if n == 0:
        return 1
    x = n
    product = 1
    while x % 2 == 0:
        x //= 2
    for p in primes:
        if p == 2:
            continue
        if p * p > x:
            break
        if x % p == 0:
            exp = 0
            while x % p == 0:
                x //= p
                exp += 1
            if p % 4 == 3:
                if exp & 1:
                    return 0
            elif p % 4 == 1:
                product *= (exp + 1)
    if x > 1:
        if x % 4 == 3:
            return 0
        elif x % 4 == 1:
            product *= 2
    r2 = 4 * product
    root = math.isqrt(n)
    axis = 1 if root * root == n else 0
    if n % 2 == 0:
        half_root = math.isqrt(n // 2)
        diagonal = 1 if half_root * half_root == n // 2 else 0
    else:
        diagonal = 0
    return (r2 + 4 * axis + 4 * diagonal) // 8

def main():
    input = sys.stdin.readline
    T = int(input())
    ans = []
    for _ in range(T):
        n = int(input())
        ans.append(str(count_ways(n)))
    sys.stdout.write("\n".join(ans))

if __name__ == "__main__":
    main()
