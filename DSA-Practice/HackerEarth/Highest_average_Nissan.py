"""
Problem : Highest average
Platform: HackerEarth (Easy)
Link    : https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/highest-average-64bdd761/
Date    : 2026-10-02
Topics  : Algorithms, Binary Search, Math, Searching

Approach:
  Sort the array and build prefix sums. The average of the m smallest
  elements never decreases as m grows, so "average of first m elements < K"
  is monotonic in m. For each query K, binary search the largest m with
  prefix[m] < K * m. Multiplying avoids floating-point division.

Complexity:
  Time  : O(N log N + Q log N)   (sort + one binary search per query)
  Space : O(N)                   (prefix sums)
"""


# ---------------------------------------- Solution -------------------------------------------------


import sys

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    it = iter(data)
    N = next(it)
    A = [next(it) for _ in range(N)]
    A.sort()
    prefix = [0] * (N + 1)
    for i in range(1, N + 1):
        prefix[i] = prefix[i - 1] + A[i - 1]
    Q = next(it)
    ans = []
    for _ in range(Q):
        K = next(it)
        lo, hi = 0, N
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if prefix[mid] < K * mid:
                lo = mid
            else:
                hi = mid - 1
        ans.append(str(lo))
    sys.stdout.write("\n".join(ans))

if __name__ == "__main__":
    solve()
