"""
Problem: Maximise Sum
Platform: CodeChef
Link: https://www.codechef.com/problems/MAXIMISESUM
Date: 2026-09-29
Difficulty: 1715
Topics: Prefix/Suffix Maximum

Approach:
- Build prefix maxima and suffix maxima.
- For each interior element A[i], the best value contributed is:
      max(A[i], min(max_left, max_right))
- Endpoints are added directly.

Time Complexity: O(N) per test case
Space Complexity: O(N) per test case
"""


# -------------------------------- Solution -------------------------------------------------


import sys

def solve():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        if N <= 2:
            print(sum(A))
            continue
        pref = [0] * N
        pref[0] = A[0]
        for i in range(1, N):
            pref[i] = max(pref[i - 1], A[i])
        suff = [0] * N
        suff[N - 1] = A[N - 1]
        for i in range(N - 2, -1, -1):
            suff[i] = max(suff[i + 1], A[i])
        ans = A[0] + A[N - 1]
        for i in range(1, N - 1):
            best = min(pref[i - 1], suff[i + 1])
            ans += max(A[i], best)
        print(ans)

if __name__ == "__main__":
    solve()
