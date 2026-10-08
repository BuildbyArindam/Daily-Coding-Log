"""
Problem   : New World
Platform  : HackerEarth 
Link      : https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/new-world-11/
Date      : 2026-10-08
Difficulty: Medium
Topics    : Binary Search, Greedy, Sorting

Approach:
    Binary search on the answer (the minimized maximum jump length).
    - Lower bound: the largest gap between adjacent stones (any smaller
      value makes some gap impossible to cross).
    - Upper bound: stones[-1] - stones[0] (reach the end in one jump).
    For a candidate max_jump, a greedy check walks the stones and always
    jumps to the farthest stone still within max_jump, counting jumps.
    If the count is <= K the candidate is feasible, so search lower;
    otherwise search higher.

Complexity:
    Time  : O(N * log(stones[-1] - stones[0])) per test case
    Space : O(1) extra (besides storing the input array)
"""


# ------------------------------------------ Solution -----------------------------------------------------


import sys

def can_reach(stones, k, max_jump):
    n = len(stones)
    last = 0
    jumps = 0
    for i in range(1, n):
        if stones[i] - stones[last] > max_jump:
            if i - 1 == last:
                return False
            last = i - 1
            jumps += 1
            if jumps > k:
                return False
    if last != n - 1:
        if stones[-1] - stones[last] > max_jump:
            return False
        jumps += 1
    return jumps <= k

def solve():
    input = sys.stdin.buffer.readline
    T = int(input())
    for _ in range(T):
        N, K = map(int, input().split())
        stones = list(map(int, input().split()))
        low = max(
            stones[i] - stones[i - 1]
            for i in range(1, N)
        )
        high = stones[-1] - stones[0]
        while low < high:
            mid = (low + high) // 2
            if can_reach(stones, K, mid):
                high = mid
            else:
                low = mid + 1
        print(low)

solve()
