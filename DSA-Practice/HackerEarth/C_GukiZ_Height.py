"""
Problem   : C - GukiZ Height
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/c-gukiz-height/
Date      : 2026-10-08
Difficulty: Medium
Topics    : Binary Search, Sorting, Prefix Sums, Math

Approach:
    Write the answer as d = q*N + r (q full cycles plus r extra days).
    For each fixed remainder r in [0, N-1], the accumulated height is a
    quadratic in q, so the smallest valid q comes from the quadratic formula
    (exact integer sqrt via math.isqrt, then a +1 correction for floor error)
    instead of a binary search over q. Prefix sums give each r's constant
    terms in O(1). The answer is the minimum d >= 1 over all r.

Complexity:
    Time : O(N)  - one pass with O(1) work per remainder
    Space: O(N)  - prefix sum array
"""


# ---------------------------------------- Solution ------------------------------------------


import sys
from math import isqrt

def main():
    input = sys.stdin.readline
    N, H = map(int, input().split())
    A = list(map(int, input().split()))
    pref = [0] * (N + 1)
    for r in range(N):
        pref[r + 1] = pref[r] + A[r]
    total = pref[N]
    answer = None
    for r in range(N):
        a = N * N
        b = 2 * N * r + N + 2 * total
        c = 2 * pref[r] + r * (r + 1) - 2 * H
        if c >= 0:
            q = 0
        else:
            discriminant = b * b - 4 * a * c
            root_sqrt = isqrt(discriminant)
            denominator = 2 * a
            q = (-b + root_sqrt) // denominator
            value = a * q * q + b * q + c
            if value < 0:
                q += 1
        days = q * N + r
        if days >= 1:
            if answer is None or days < answer:
                answer = days
    print(answer)

if __name__ == "__main__":
    main()
