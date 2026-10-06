"""
Problem   : Two Arrays
Platform  : HackerEarth 
Link      : https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/two-arrays-2-0f24abf0/
Date      : 2026-10-06
Difficulty: Medium
Topics    : Binary Search, Prefix Sum, Two Pointer, Searching

Approach  :
  - Build a match matrix E[i][j] = (A[i] == B[j]) and its 2D prefix sum P,
    so the number of matching pairs in any L x L block starting at (i, j)
    is answered in O(1).
  - The score of a block is non-decreasing in L, so for each start (i, j)
    there is a minimal length L* where score >= K. Every length from L* up
    to the maximum possible length is also valid, contributing max_len - L* + 1.
  - An L x L block holds at most L^2 matches, so L* >= ceil(sqrt(K)). This is
    the lower bound for the binary search, and starts that fail at max length
    are pruned first.
  - For each row i, the binary search runs over all columns j at once using
    NumPy vectorization.

Complexity:
  Time  : O(N * M * log(min(N, M)))
  Space : O(N * M) for E and P
"""


# ----------------------------------------------- Solution --------------------------------------------------


import sys
import math
import numpy as np

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    N, M, K = data[0], data[1], data[2]
    A = np.array(data[3:3 + N], dtype=np.int64)
    B = np.array(data[3 + N:3 + N + M], dtype=np.int64)
    T = K
    E = (A[:, None] == B[None, :]).astype(np.int32)
    P = np.zeros((N + 1, M + 1), dtype=np.int32)
    P[1:, 1:] = E.cumsum(axis=0, dtype=np.int32).cumsum(axis=1, dtype=np.int32)
    min_len = math.isqrt(T)
    if min_len * min_len < T:
        min_len += 1
    js = np.arange(M, dtype=np.int32)
    answer = 0
    for i in range(N):
        lengths = np.minimum(N - i, M - js)
        valid = lengths >= min_len
        if not valid.any():
            continue
        idx = np.nonzero(valid)[0]
        L = lengths[idx]
        r = i + L
        c = idx + L
        score = (
            P[r, c]
            - P[i, c]
            - P[r, idx]
            + P[i, idx]
        )
        good = score >= T
        idx = idx[good]
        if idx.size == 0:
            continue
        L = lengths[idx]
        lo = np.full(idx.size, min_len, dtype=np.int32)
        hi = L.copy()
        while True:
            active = lo < hi
            if not active.any():
                break
            pos = np.nonzero(active)[0]
            mid = (lo[pos] + hi[pos]) // 2
            j = idx[pos]
            r = i + mid
            c = j + mid
            score = (
                P[r, c]
                - P[i, c]
                - P[r, j]
                + P[i, j]
            )
            reached = score >= T
            hi[pos[reached]] = mid[reached]
            lo[pos[~reached]] = mid[~reached] + 1
        answer += int(np.sum(L - lo + 1, dtype=np.int64))
    print(answer)

if __name__ == "__main__":
    main()
