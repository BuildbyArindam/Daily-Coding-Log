"""
Problem: Maximum work
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/maximum-work-11cfd424/
Date: 2026-09-19
Difficulty: Medium
Topics: Binary Search, Algorithms

Approach:
Binary search on the answer x = number of tasks that can be completed.
For a candidate x, greedily pair the x strongest workers (sorted ascending,
take the top x) against the x easiest tasks (sorted ascending): W[N-x:] vs S[:x].
For each pair, if the worker's strength is short of the task, the shortfall
is covered using pills, each pill adding B strength; ceil(diff / B) pills per
pair. If total pills used across all x pairs stays within budget K, x is
feasible. Since feasibility is monotonic in x, binary search over
[0, min(N, M)] for the largest feasible x.

Time Complexity: O(T * (N log N + M log M + min(N,M) log(min(N,M))))
  - sorting W and S: O(N log N + M log M)
  - binary search over x: O(log(min(N,M))) iterations
  - each feasibility check (can_do): O(x) <= O(min(N,M))
Space Complexity: O(N + M) for storing W and S (sort is in-place)
"""


# ----------------------------------- Solution -----------------------------------------------


def solve(K, B, N, W, M, S):
    W.sort()
    S.sort()
    def can_do(x):
        if x == 0:
            return True
        start_worker = N - x
        pills_used = 0
        for i in range(x):
            worker = W[start_worker + i]
            task = S[i]
            if worker < task:
                diff = task - worker
                pills_used += (diff + B - 1) // B
                if pills_used > K:
                    return False
        return True
    low = 0
    high = min(N, M)
    while low < high:
        mid = (low + high + 1) // 2
        if can_do(mid):
            low = mid
        else:
            high = mid - 1
    return low

T = int(input())
for _ in range(T):
    K, B = map(int, input().split())
    N = int(input())
    W = list(map(int, input().split()))
    M = int(input())
    S = list(map(int, input().split()))
    out_ = solve(K, B, N, W, M, S)
    print(out_)
