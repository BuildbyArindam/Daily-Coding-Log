"""
Problem: Hexadecimal Numbers
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/yet-another-easy-problem-1f3273a0/
Date: 2026-09-15
Difficulty: Easy
Topic: Algorithms, Brute Force, Searching

Approach:
    For each x in [1, max_r], compute the sum of its base-16 digits and check
    if gcd(x, digit_sum) > 1. Build a prefix-count array over this boolean
    condition so each query (L, R) can be answered in O(1) via
    prefix[R] - prefix[L-1], instead of recomputing per query.

Time complexity:  O(max_r * log16(max_r) + T)   -- precompute once, O(1) per query
Space complexity: O(max_r)                      -- prefix sum array
"""


# ------------------------------ Solution ------------------------------------


import math

T = int(input())
queries = []
max_r = 0
for _ in range(T):
    L, R = map(int, input().split())
    queries.append((L, R))
    max_r = max(max_r, R)
prefix = [0] * (max_r + 1)
for x in range(1, max_r + 1):
    n = x
    digit_sum = 0
    while n > 0:
        digit_sum += n % 16
        n //= 16
    if math.gcd(x, digit_sum) > 1:
        prefix[x] = 1
    prefix[x] += prefix[x - 1]
for L, R in queries:
    print(prefix[R] - prefix[L - 1])
