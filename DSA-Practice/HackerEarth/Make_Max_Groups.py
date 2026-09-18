"""
Problem: Make Max Groups
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/make-max-groups-8ed37369/
Date: 2026-09-18
Difficulty: Medium
Topics: Math, Algorithms, Binary Search

Approach:
Binary search on the answer (number of groups). For a candidate group count `g`,
check feasibility greedily: each group can use at most K//2 blocks of any single
type (to keep groups balanced/valid), so cap every pile's contribution at
`g * (K // 2)`. Using a sorted prefix-sum array, piles below that cap contribute
their full value, piles at/above it contribute the capped value. If total usable
blocks >= g * K, `g` groups are feasible. Binary search over g in [0, total_blocks // K].

Time Complexity: O(N log N) for sort + O(log(total_blocks/K)) binary search steps,
                  each O(log N) via bisect -> O(N log N + log(maxG) * log N)
Space Complexity: O(N) for prefix sum array
"""


# --------------------------------- Solution ------------------------------------


import sys
from bisect import bisect_left

def solve():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N, K = map(int, input().split())
        A = list(map(int, input().split()))
        A.sort()
        pref = [0] * (N + 1)
        for i in range(N):
            pref[i + 1] = pref[i] + A[i]
        total_blocks = pref[N]
        per_group_type_limit = K // 2
        hi = total_blocks // K
        lo = 0
        ans = 0
        def possible(groups):
            if groups == 0:
                return True
            limit = groups * per_group_type_limit
            pos = bisect_left(A, limit)
            usable = pref[pos] + (N - pos) * limit
            return usable >= groups * K
        while lo <= hi:
            mid = (lo + hi) // 2
            if possible(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        print(ans)

if __name__ == "__main__":
    solve()
