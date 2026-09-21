"""
Problem   : Highways
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/highways-8b2d55fe/
Date      : 2026-09-21
Difficulty: Medium
Topics    : Binary Search, Implementation, Pointer

Approach:
  Binary search on the answer d (max distance from a chosen highway point
  to its city, along either axis — Chebyshev-style). For a candidate d,
  the covering window has width 2d. Sort cities by x, then for each
  window [left, right] (two-pointer over sorted x) check whether the
  y-range of cities OUTSIDE the window (using prefix/suffix min/max of y)
  fits within width 2d — meaning a single highway segment of length d
  can be placed to cover everything. Binary search lo..hi on d for the
  minimal feasible value.

Complexity:
  Time : O(K log K) for the sort + O(N log K) for binary search over d,
         where each feasibility check is O(K) via two-pointer + prefix/
         suffix arrays  ->  overall O(K log K + K log N)
  Space: O(K) for xs, ys, prefix/suffix min-max arrays
"""


# ------------------------------------ Solution -----------------------------------------


import sys

def solve():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    cities = [tuple(map(int, input().split())) for _ in range(K)]
    cities.sort()
    xs = [0] * K
    ys = [0] * K
    for i, (x, y) in enumerate(cities):
        xs[i] = x
        ys[i] = y
    pref_min = [0] * K
    pref_max = [0] * K
    mn = mx = ys[0]
    for i in range(K):
        mn = min(mn, ys[i])
        mx = max(mx, ys[i])
        pref_min[i] = mn
        pref_max[i] = mx
    suff_min = [0] * K
    suff_max = [0] * K
    mn = mx = ys[K - 1]
    for i in range(K - 1, -1, -1):
        mn = min(mn, ys[i])
        mx = max(mx, ys[i])
        suff_min[i] = mn
        suff_max[i] = mx
    def feasible(d):
        width = 2 * d
        left = 0
        for right in range(K):
            while xs[right] - xs[left] > width:
                left += 1
            if left == 0:
                if right == K - 1:
                    return True
                min_y = suff_min[right + 1]
                max_y = suff_max[right + 1]
            elif right == K - 1:
                min_y = pref_min[left - 1]
                max_y = pref_max[left - 1]
            else:
                min_y = min(pref_min[left - 1], suff_min[right + 1])
                max_y = max(pref_max[left - 1], suff_max[right + 1])
            if max_y - min_y <= width:
                return True
        return False
    lo = 0
    hi = N
    while lo < hi:
        mid = (lo + hi) // 2
        if feasible(mid):
            hi = mid
        else:
            lo = mid + 1
    print(lo)

if __name__ == "__main__":
    solve()
