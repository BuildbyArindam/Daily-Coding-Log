"""
Problem   : Chefina and Swap (CHFNSWAP)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/CHFNSWAP
Difficulty: 1735
Topics    : Math, Combinatorics, Integer Sqrt 
Date      : 2026-10-09

Approach:
    Let S = N(N+1)/2. If S is odd, no valid swap exists, so the answer is 0.
    Otherwise the target is half = S/2, and a swap must leave some prefix
    with sum == half.
      1. If a prefix of 1..r already sums to half (r(r+1)/2 == half), any swap
         within the left part or within the right part keeps the split valid:
         C(r, 2) + C(N-r, 2) swaps.
      2. Otherwise, for a split after position m, the prefix sum 1..m is short
         by d = half - m(m+1)/2. A swap of i <= m with j > m changes it by
         (j - i), so we need j - i = d. Count valid i in [max(1, m-d+1),
         min(m, N-d)].
      3. Only 1 <= d < N is feasible, so m is bounded below by an isqrt
         solve of m(m+1)/2 > half - N. This leaves a tiny window of m values
         up to r = floor of the root of m(m+1)/2 <= half.

Time  : O(1) per test (a few isqrt calls and a very small loop window)
Space : O(1)
"""


# ------------------------------------------------- Solution -----------------------------------------------------


import sys
from math import isqrt

def solve():
    input = sys.stdin.buffer.readline
    T = int(input())
    for _ in range(T):
        N = int(input())
        total = N * (N + 1) // 2
        if total % 2 != 0:
            print(0)
            continue
        half = total // 2
        r = (isqrt(8 * half + 1) - 1) // 2
        ans = 0
        if r * (r + 1) // 2 == half:
            ans += r * (r - 1) // 2
            ans += (N - r) * (N - r - 1) // 2
        low = (isqrt(8 * (half - N) + 1) - 1) // 2 + 1
        for m in range(low, r + 1):
            d = half - m * (m + 1) // 2
            if 1 <= d < N:
                left = max(1, m - d + 1)
                right = min(m, N - d)
                ans += max(0, right - left + 1)
        print(ans)

if __name__ == "__main__":
    solve()
