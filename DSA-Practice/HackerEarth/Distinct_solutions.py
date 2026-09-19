"""
Problem   : Distinct Solutions
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/distinct-solution-c638e2b0/
Date      : 2026-09-19
Difficulty: Medium
Topics    : Binary Search, Algorithms

Approach:
  For each test case (N, t1, t2), find the split point q (number of items
  assigned to the t1-side) that minimizes the maximum finish time between
  the two sides, using the ratio q ≈ N*t2/(t1+t2). Check the two nearest
  integer candidates (q and q+1) since the true optimum lies near this
  real-valued split, and take whichever gives the smaller max time D.
  Once D is fixed, compute how many ticks occur by time D on each side
  (m = D//t1 + D//t2), rounding D up (f) to the next multiple of t1/t2
  wherever D isn't already a clean multiple, since a tick only "counts"
  fully at the moment it completes.

Time complexity : O(1) per test case → O(T) overall
Space complexity: O(1)
"""


# ------------------------------------- Solution -----------------------------------------


import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N, t1, t2 = map(int, input().split())
    q = (N * t2) // (t1 + t2)
    d1 = max(q * t1, (N - q) * t2)
    q2 = q + 1
    if q2 <= N:
        d2 = max(q2 * t1, (N - q2) * t2)
        D = min(d1, d2)
    else:
        D = d1
    m = D // t1 + D // t2
    f = D
    if D % t1 != 0:
        m += 1
        f = max(f, (D // t1 + 1) * t1)
    if D % t2 != 0:
        m += 1
        f = max(f, (D // t2 + 1) * t2)
    print(m, f)
