"""
Problem   : Segmentation Fault
Platform  : CodeChef
Link      : https://www.codechef.com/problems/SEGFAULT
Difficulty: 1815
Topics    : Difference Array, Prefix Sum
Date      : 2026-10-13

Approach:
    Each index i has an interval [L[i], R[i]]. Index x is valid when every
    other interval covers it and its own interval does not.
    1. Build a difference array over all intervals, then take prefix sums
       to get count[x], the number of intervals covering x.
    2. Keep x only if its own interval excludes it (not L[x] <= x <= R[x])
       and count[x] == N - 1, meaning all other N - 1 intervals cover it.

Complexity:
    Time : O(N) per test case
    Space: O(N)
"""


# --------------------------------------------------- Solution ----------------------------------------------------


import sys

def solve():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N = int(input())
        L = [0] * (N + 1)
        R = [0] * (N + 1)
        diff = [0] * (N + 2)
        for i in range(1, N + 1):
            L[i], R[i] = map(int, input().split())
            diff[L[i]] += 1
            diff[R[i] + 1] -= 1
        count = [0] * (N + 1)
        current = 0
        for i in range(1, N + 1):
            current += diff[i]
            count[i] = current
        ans = []
        for x in range(1, N + 1):
            if L[x] <= x <= R[x]:
                continue
            if count[x] == N - 1:
                ans.append(x)
        print(len(ans))
        for x in ans:
            print(x)

if __name__ == "__main__":
    solve()
