"""
Problem   : No Two Alike (CPYD)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/CPYD
Difficulty: 1801
Topics    : Arrays, Hashing, Interval Merging
Date      : 2026-10-04

Approach:
  Record the first and last index of every value. Each value that
  appears more than once gives an interval [first, last]. Intervals are
  built in order of first occurrence, so they are already sorted by left
  endpoint. Merge overlapping intervals in one sweep, and for each merged
  segment add the number of distinct values inside it.

Time : O(N) per test case. Merged segments are disjoint, so the
       total work of the set() calls is bounded by N.
Space: O(N) for the first/last maps, the interval list and the sets.
"""


# -------------------------------------- Solution ------------------------------------------------


import sys
input = sys.stdin.readline

def solve():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        first = {}
        last = {}
        for i, x in enumerate(A):
            if x not in first:
                first[x] = i
            last[x] = i
        intervals = []
        for x in first:
            if first[x] != last[x]:
                intervals.append((first[x], last[x]))
        if not intervals:
            print(0)
            continue
        ans = 0
        L, R = intervals[0]
        for l, r in intervals[1:]:
            if l <= R:
                R = max(R, r)
            else:
                ans += len(set(A[L:R + 1]))
                L, R = l, r
        ans += len(set(A[L:R + 1]))
        print(ans)

if __name__ == "__main__":
    solve()
