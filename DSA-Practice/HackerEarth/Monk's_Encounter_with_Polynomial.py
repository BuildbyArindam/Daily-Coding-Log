"""
Problem   : Monk's Encounter with Polynomial
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/monks-encounter-with-polynomial/
Difficulty: Easy
Topics    : Binary Search, Math, Sorting
Date      : 2026-10-03

Approach  : Find the smallest non-negative integer x such that
            A*x^2 + B*x + C >= K. For non-negative A, B, C the polynomial is
            non-decreasing for x >= 0, so binary search applies.
            1. Exponential search: double `hi` until f(hi) >= K to get an
               upper bound without overflow-style guesswork.
            2. Binary search on [0, hi] for the first x with f(x) >= K.

Time      : O(log X) per test case, where X is the answer (doubling phase
            + binary search phase); O(T log X) overall.
Space     : O(1)
"""


# ------------------------------------- Solution ----------------------------------------------------


T = int(input())
for _ in range(T):
    A, B, C, K = map(int, input().split())
    lo = 0
    hi = 1
    while A * hi * hi + B * hi + C < K:
        hi *= 2
    while lo < hi:
        mid = (lo + hi) // 2
        value = A * mid * mid + B * mid + C
        if value >= K:
            hi = mid
        else:
            lo = mid + 1
    print(lo)
