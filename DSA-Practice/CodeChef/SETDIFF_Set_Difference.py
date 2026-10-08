"""
Problem   : Set Difference
Platform  : CodeChef
Link      : https://www.codechef.com/problems/SETDIFF
Difficulty: 1729
Date      : 2026-10-08
Topics    : Math, Combinatorics, Sorting

Approach:
    Sort the array. For each A[i] in sorted order:
      - It is the maximum of 2^i subsets (any subset of the i smaller elements).
      - It is the minimum of 2^(N-i-1) subsets (any subset of the larger elements).
    The single-element subset is counted in both and contributes 0 to
    (max - min), so it cancels out. Each A[i] therefore adds:
        A[i] * ((2^i - 1) - (2^(N-i-1) - 1))
    Powers of 2 are precomputed modulo 10^9 + 7.

Complexity:
    Time : O(N log N) per test case (sorting dominates)
    Space: O(N) for the powers-of-2 table
"""


# ---------------------------------- Solution ---------------------------------------------------


MOD = 10**9 + 7

T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    pow2 = [1] * N
    for i in range(1, N):
        pow2[i] = (pow2[i - 1] * 2) % MOD
    for i in range(N):
        max_count = pow2[i] - 1
        min_count = pow2[N - i - 1] - 1
        ans = (ans + A[i] * (max_count - min_count)) % MOD
    print(ans)
