"""
Problem   : Car-pal Tunnel (CARPTUN)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/CARPTUN
Difficulty: 1714
Topics    : Basic Math, Mathematics
Date      : 2026-09-29

Approach:
    The result depends only on the maximum value in A. The answer is
    (C - 1) * max(A), printed with 9 decimal places. D and S are read
    but not needed for the final formula.

Complexity:
    Time  : O(N) per test case (one pass to find max(A))
    Space : O(N) to store A
"""


# ------------------------------------- Solution ----------------------------------------------


import sys

def solve():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        C, D, S = map(int, input().split())
        answer = (C - 1) * max(A)
        print(f"{answer:.9f}")

if __name__ == "__main__":
    solve()
