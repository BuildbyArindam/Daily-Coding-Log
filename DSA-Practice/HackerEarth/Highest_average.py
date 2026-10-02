"""
Problem   : Highest average
Platform  : HackerEarth (Easy)
Link      : https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/highest-average-25400da7/
Date      : 2026-10-02
Topics    : Algorithms, Binary Search, Searching

Approach   : Sort the array and build prefix sums. The average of the m smallest
             elements never decreases as m grows, so "avg of m smallest < K"
             is monotonic in m. For each query K, binary search the largest m
             with prefix[m] < m * K (integer comparison, no floats).

Complexity : Time  O(N log N + Q log N)  -> sort + one binary search per query
             Space O(N)                  -> prefix sums array
"""


# ------------------------------------- Solution ---------------------------------------------


import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
A.sort()
prefix = [0] * (N + 1)
for i in range(N):
    prefix[i + 1] = prefix[i] + A[i]
Q = int(input())
out = []
for _ in range(Q):
    K = int(input())
    lo, hi = 0, N
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if prefix[mid] < mid * K:
            lo = mid
        else:
            hi = mid - 1
    out.append(str(lo))
sys.stdout.write("\n".join(out))
