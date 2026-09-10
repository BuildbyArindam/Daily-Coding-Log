"""
Problem   : Monotone Median (MONMED)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/MONMED
Difficulty: Medium 
Topics    : Permutations, Two Pointers, Greedy, Constructive Algorithms, Median/Order Statistics
Date      : 2026-09-10

Approach  :
    - Given a permutation P of odd length N, need N.B. (N+1)//2 nested subarrays
      of lengths 1,3,5,...,N with strictly increasing medians.
    - The i-th subarray (length 2i-1) has median i  <=>  it contains exactly
      the values {1,...,i}. So track pos[i] = index of value i, and maintain
      running min/max of positions seen so far to get the tightest window
      [lo_i, hi_i] of valid left endpoints for that subarray length.
    - Left endpoints across consecutive subarrays must satisfy
      L_{i+1} in [L_i - 2, L_i], so propagate this constraint forward to
      build [lo, hi] per i, then reconstruct L_i backward from L_K = 1.
    - If at any point the interval becomes empty, answer is -1.

Time complexity  : O(N) per test case
Space complexity : O(N) per test case
"""


# ----------------------------- Solution -----------------------------------


import sys

def solve():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N = int(input())
        P = list(map(int, input().split()))
        K = (N + 1) // 2
        pos = [0] * (N + 1)
        for i, x in enumerate(P, 1):
            pos[x] = i
        mn = mx = pos[1]
        lo = [0] * (K + 1)
        hi = [0] * (K + 1)
        lo[1] = hi[1] = pos[1]
        possible = True
        for i in range(2, K + 1):
            mn = min(mn, pos[i])
            mx = max(mx, pos[i])
            length = 2 * i - 1
            A = max(1, mx - length + 1)
            B = min(mn, N - length + 1)
            new_lo = max(A, lo[i - 1] - 2)
            new_hi = min(B, hi[i - 1])
            if new_lo > new_hi:
                possible = False
                break
            lo[i] = new_lo
            hi[i] = new_hi
        if not possible:
            print(-1)
            continue
        if not (lo[K] <= 1 <= hi[K]):
            print(-1)
            continue
        L = [0] * (K + 1)
        R = [0] * (K + 1)
        L[K] = 1
        R[K] = N
        for i in range(K, 1, -1):
            left = max(lo[i - 1], L[i])
            right = min(hi[i - 1], L[i] + 2)
            L[i - 1] = right
            R[i - 1] = L[i - 1] + (2 * (i - 1) - 2)
        L[1] = L[1]
        R[1] = L[1]
        for i in range(1, K + 1):
            print(L[i], R[i])

if __name__ == "__main__":
    solve()
