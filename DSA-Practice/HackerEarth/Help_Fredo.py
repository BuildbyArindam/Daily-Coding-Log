"""
Problem   : Help Fredo
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/help-fredo/
Difficulty: Medium
Topics    : Algorithms, Searching, Binary Search
Date      : 2026-10-07

Approach:
    The answer is the smallest integer x with x^N > product(A), which is
    floor(N-th root of P) + 1.
    1. Estimate the N-th root (the geometric mean) in log space, using
       fsum of log2 to avoid overflow and accumulated float error.
    2. Compute the exact product P with a balanced pairwise product tree.
       This keeps the big-int operands similar in size, so Python's
       Karatsuba multiplication is used effectively.
    3. Correct the float estimate with exact big-int comparisons
       (pow(x, N) vs P) until x is the largest integer with x^N <= P.
    4. Print x + 1.

Complexity (B = total bits of P, about N * log2(max(A))):
    Time : O(M(B) * log N) for the product tree, plus O(M(B)) per exact
           pow check. The correction loops run only a few iterations
           because the log estimate is very close.
    Space: O(B) for the big-integer product.
"""


# -------------------------------------------- Solution -----------------------------------------------------------


import sys
import math

data = list(map(int, sys.stdin.buffer.read().split()))
N = data[0]
A = data[1:]
def product(arr):
    while len(arr) > 1:
        nxt = []
        for i in range(0, len(arr) - 1, 2):
            nxt.append(arr[i] * arr[i + 1])
        if len(arr) % 2:
            nxt.append(arr[-1])
        arr = nxt
    return arr[0]
log_sum = math.fsum(math.log2(x) for x in A)
g = 2.0 ** (log_sum / N)
x = max(1, int(round(g)))
P = product(A)
while pow(x, N) > P:
    x -= 1
while pow(x + 1, N) <= P:
    x += 1
print(x + 1)
