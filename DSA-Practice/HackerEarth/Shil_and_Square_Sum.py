"""
Problem   : Shil and Square Sum
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/shil-and-square-sum-qualifier2/
Date      : 2026-08-25
Difficulty: Medium
Topics    : Math, Implementation

Approach:
For each window of size K, we need sum(a[j] * (j - start + 1)^2) over the
window. Expanding (j - start + 1)^2 lets the windowed sum be expressed via
three running aggregates over the window: S1 = sum(a[j]), S2 = sum((pos)*a[j]),
S3 = sum((pos)^2 * a[j]), where pos is the 1-indexed position within the
window. When the window slides by one (dropping the leftmost element, adding
one new element on the right), S1, S2, S3 can each be updated in O(1) using
the algebraic relations between consecutive windows, avoiding recomputation
from scratch. All values are kept mod 1e9+7.

Time complexity : O(N)      -- O(K) to build the first window, O(1) per slide
Space complexity: O(N)      -- output list of size N-K+1 (O(1) extra otherwise)
"""


# ---------------------------- Solution -----------------------------


import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    MOD = 10**9 + 7
    N = int(input_data[0])
    K = int(input_data[1])
    A = [int(x) for x in input_data[2:N+2]]
    S1 = 0
    S2 = 0
    S3 = 0
    for j in range(K):
        val = A[j]
        S1 = (S1 + val) % MOD
        S2 = (S2 + (j + 1) * val) % MOD
        S3 = (S3 + (j + 1) * (j + 1) * val) % MOD
    results = [str(S3)]
    for i in range(1, N - K + 1):
        prev_elem = A[i - 1]
        next_elem = A[i + K - 1]
        new_S3 = (S3 - 2 * S2 + S1 + K * K * next_elem) % MOD
        new_S2 = (S2 - S1 + K * next_elem) % MOD
        new_S1 = (S1 - prev_elem + next_elem) % MOD
        S1, S2, S3 = new_S1, new_S2, new_S3
        results.append(str(S3))
    print(" ".join(results))

if __name__ == '__main__':
    solve()
