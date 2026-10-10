"""
Problem   : Station Allocation (STATALLOC)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/STATALLOC
Difficulty: 1807
Topics    : Sorting, Binary Search, Greedy 
Date      : 2026-10-10

Approach:
  Sort the capacities and precompute their total. For each query (X, Y),
  only two crews can be optimal:
    1. The smallest crew with capacity >= X (found via bisect_left). It
       needs no upgrade, and being the smallest, it takes the least
       capacity out of storage.
    2. The largest crew with capacity < X. It needs X - c extra for the
       crew, and being the largest, it minimizes the shortfall.
  For each candidate, cost = crew_extra + max(0, Y - (total - c)).
  The answer is the minimum of the two candidates.

Complexity:
  Time  : O(N log N + Q log N) per test case (sort + one binary search per query)
  Space : O(N)
"""


# ---------------------------------------- Solution -------------------------------------------------------


import bisect

def solve():
    T = int(input())
    for _ in range(T):
        N = int(input())
        C = list(map(int, input().split()))
        C.sort()
        total = sum(C)
        Q = int(input())
        ans = []
        for _ in range(Q):
            X, Y = map(int, input().split())
            idx = bisect.bisect_left(C, X)
            best = float('inf')
            if idx < N:
                crew_capacity = C[idx]
                storage_capacity = total - crew_capacity
                extra = max(0, Y - storage_capacity)
                best = extra
            if idx > 0:
                crew_capacity = C[idx - 1]
                crew_extra = X - crew_capacity
                storage_capacity = total - crew_capacity
                storage_extra = max(0, Y - storage_capacity)
                best = min(best, crew_extra + storage_extra)
            ans.append(best)
        print(*ans)

if __name__ == "__main__":
    solve()
