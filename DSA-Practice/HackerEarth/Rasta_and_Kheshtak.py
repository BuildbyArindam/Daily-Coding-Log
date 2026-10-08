"""
Problem   : Rasta and Kheshtak
Platform  : HackerEarth 
Link      : https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/rasta-and-kheshtak/
Date      : 2026-10-08
Difficulty: Medium
Topics    : Binary Search, Hashing, Hash Maps, Sorting

Approach:
    Find the largest k such that a k x k square of matrix A is identical
    to a k x k square of matrix B.
    - If a common k x k square exists, a common (k-1) x (k-1) one exists too,
      so the answer is monotonic and we can binary search on k.
    - For each k, hash every k x k square in O(1) using a 2D prefix sum of
      value * BASE^(i*STRIDE + j) (mod 2^64), then multiply by
      BASE^(MAX_EXP - top-left offset) to normalize the position.
    - Store all hashes of A in a set, then check the squares of B against it.

Complexity (n x m and x x y matrices, K = min(n, m, x, y)):
    Time  : O((n*m + x*y) * log K)
    Space : O(n*m + x*y) for prefix tables and the hash set, plus
            O(MAX_EXP) for the precomputed powers
"""


# -------------------------------------- Solution --------------------------------------------------


import sys
import random

input = sys.stdin.buffer.readline
MASK = (1 << 64) - 1
STRIDE = 701
MAX_EXP = 700 * STRIDE + 700
BASE = random.randrange(1 << 32, 1 << 63) | 1
powers = [1] * (MAX_EXP + 1)
for i in range(1, MAX_EXP + 1):
    powers[i] = (powers[i - 1] * BASE) & MASK

def build_prefix(n, m):
    pref = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n):
        row = list(map(int, input().split()))
        prev = pref[i]
        cur = pref[i + 1]
        row_sum = 0
        offset = i * STRIDE
        for j in range(m):
            row_sum = (
                row_sum + row[j] * powers[offset + j]
            ) & MASK
            cur[j + 1] = (prev[j + 1] + row_sum) & MASK
    return pref

def square_hash(pref, top, left, k):
    bottom = top + k
    right = left + k
    raw = (
        pref[bottom][right]
        - pref[top][right]
        - pref[bottom][left]
        + pref[top][left]
    ) & MASK
    return (
        raw * powers[MAX_EXP - (top * STRIDE + left)]
    ) & MASK

n, m = map(int, input().split())
values_a = 0
pref_a = build_prefix(n, m)
x, y = map(int, input().split())
pref_b = build_prefix(x, y)
max_k = min(n, m, x, y)

def possible(k):
    hashes = set()
    rows_a = n - k + 1
    cols_a = m - k + 1
    for i in range(rows_a):
        for j in range(cols_a):
            hashes.add(square_hash(pref_a, i, j, k))
    rows_b = x - k + 1
    cols_b = y - k + 1
    for i in range(rows_b):
        for j in range(cols_b):
            if square_hash(pref_b, i, j, k) in hashes:
                return True
    return False

lo = 0
hi = max_k
while lo < hi:
    mid = (lo + hi + 1) // 2
    if possible(mid):
        lo = mid
    else:
        hi = mid - 1
print(lo)
