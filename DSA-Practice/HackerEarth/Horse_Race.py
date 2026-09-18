"""
Problem: Horse Race
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/horse-race-122f4ccc/
Date: 2026-09-18
Difficulty: Medium
Topics: Algorithms, Binary Search

Approach:
    For each track, count how many "tracked" wins it already has. Any race
    win outside the tracked range M can be freely assigned to boost any
    track's count (bounded by X extra assignable wins). Binary search on the
    answer k = "can every track reach at least k wins?" — feasibility check
    sums the deficit needed to bring every track up to k and compares it
    against X (and against the total wins available, M*k <= max_total).

Complexity:
    Time:  O((N + M) * log(max_total / M)) per test case
           — building counts is O(N), each binary search step is O(M),
             and there are O(log(max_total/M)) steps.
    Space: O(M) for the count array B.
"""


# --------------------------------- Solution --------------------------------------------


import sys

def solve():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N, M, X = map(int, input().split())
        A = list(map(int, input().split()))
        B = [0] * M
        for winner in A:
            if 1 <= winner <= M:
                B[winner - 1] += 1
        total_tracked = sum(B)
        outside = N - total_tracked
        max_total = total_tracked + min(X, outside)
        def possible(k):
            if M * k > max_total:
                return False
            need = 0
            for cnt in B:
                if cnt < k:
                    need += k - cnt
                    if need > X:
                        return False
            return True
        lo = 0
        hi = max_total // M
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if possible(mid):
                lo = mid
            else:
                hi = mid - 1
        print(lo)

if __name__ == "__main__":
    solve()
