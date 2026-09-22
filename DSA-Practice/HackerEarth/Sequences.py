"""
Problem: Sequences
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/your-own-sequence-113bf172/
Date Solved: 2026-09-22
Difficulty: Medium
Topics: Algorithms, Binary Search, Math, Searching

Approach:
Given X and Y, find the minimum n such that X can be split into n
positive integers whose product is Y (n * ceil-style partition of X
into a sum of n parts, maximizing the product close to Y). The
product of n numbers summing to X is maximized when the numbers are
as equal as possible (~X/n each), giving an upper bound of
(X/n)^n. This bound is unimodal in n and peaks near n = X/e (from
calculus: maximize n*ln(X/n)). So:
  1. Locate the peak of f(n) = n*(ln X - ln n) near floor(X/e).
  2. If even the peak's max achievable product < Y, answer is -1.
  3. Otherwise binary search on n in [2, peak] using a `possible(n)`
     check: is the maximum product achievable by splitting X into n
     parts >= Y? Since f(n) is monotonically increasing up to the
     peak, this is safe to binary search directly for the smallest
     valid n.

Time Complexity: O(log X) per test case (binary search over n, O(1)
    work per check using math.log)
Space Complexity: O(1)
"""


# ----------------------------------------- Solution ----------------------------------------------


import math

def possible(x, y, n):
    if x % n == 0:
        q = x // n
        if n <= 30 and q ** n == y:
            return True
    left = n * (math.log(x) - math.log(n))
    right = math.log(y)
    return left >= right - 1e-12

def solve(x, y):
    if x == y:
        return 1
    k = math.floor(x / math.e)
    candidates = [max(2, k), max(2, k + 1)]
    peak = candidates[0]
    for n in candidates[1:]:
        if n * (math.log(x) - math.log(n)) > \
           peak * (math.log(x) - math.log(peak)):
            peak = n
    if not possible(x, y, peak):
        return -1
    lo = 2
    hi = peak
    while lo < hi:
        mid = (lo + hi) // 2
        if possible(x, y, mid):
            hi = mid
        else:
            lo = mid + 1
    return lo

t = int(input())
for _ in range(t):
    X, Y = map(int, input().split())
    print(solve(X, Y))
