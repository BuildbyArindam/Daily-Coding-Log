# Problem   : Sum Product Segments
# Platform  : CodeChef
# Link      : https://www.codechef.com/problems/SUMPRODSEG
# Date      : 2026-09-25
# Topics    : Math, Number Theory, Divisors, Constructive Algorithms, Interval Logic
#
# Approach:
# - For L + R = X, choose the smallest possible segment:
#       [X//2, X//2]          if X is even
#       [X//2, X//2 + 1]      if X is odd
#   Any other sum segment overlaps this one.
# - Factorize Y and generate its divisors to obtain candidate segments [a, b]
#   with a * b = Y.
# - If a candidate product segment lies completely to the left or right of
#   the chosen sum segment, the two segments are non-intersecting.
#
# Complexity:
# - Prime sieve preprocessing: O(N log log N), N = 10^6
# - Per test case: O(pi(sqrt(Y)) + tau(Y))
#   ≈ O(sqrt(Y)) in the usual bound
# - Auxiliary space per test case: O(tau(Y))


# ---------------------------------- Solution -------------------------------------------


import sys

def build_primes(limit):
    sieve = bytearray(b'\x01') * (limit + 1)
    sieve[0:2] = b'\x00\x00'
    for i in range(2, int(limit ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i: limit + 1: i] = b'\x00' * (
                (limit - i * i) // i + 1
            )
    return [i for i in range(2, limit + 1) if sieve[i]]

PRIMES = build_primes(10**6)

def factorize(n):
    factors = []
    for p in PRIMES:
        if p * p > n:
            break
        if n % p == 0:
            cnt = 0
            while n % p == 0:
                n //= p
                cnt += 1
            factors.append((p, cnt))
    if n > 1:
        factors.append((n, 1))
    return factors

def get_divisors(n):
    factors = factorize(n)
    divisors = [1]
    for p, cnt in factors:
        old = divisors[:]
        mul = 1
        for _ in range(cnt):
            mul *= p
            for d in old:
                divisors.append(d * mul)
    return divisors

def solve():
    input = sys.stdin.readline
    T = int(input())
    ans = []
    for _ in range(T):
        X, Y = map(int, input().split())
        mid_l = X // 2
        mid_r = X - mid_l
        divisors = get_divisors(Y)
        found = False
        for d in divisors:
            e = Y // d
            a = min(d, e)
            b = max(d, e)
            if b < mid_l:
                ans.append(f"{mid_l} {mid_r}")
                ans.append(f"{a} {b}")
                found = True
                break
            if a > mid_r:
                ans.append(f"{mid_l} {mid_r}")
                ans.append(f"{a} {b}")
                found = True
                break
        if not found:
            ans.append("-1")
    sys.stdout.write("\n".join(ans))

if __name__ == "__main__":
    solve()
