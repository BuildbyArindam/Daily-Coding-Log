"""
Problem   : Buying Order (Easy)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/BUYORDEREZ
Difficulty: 1718
Topics    : Greedy, Observation 
Date      : 2026-10-01

Approach:
    The answer depends only on the first and last elements of B.
    If B[0] == 0 and B[-1] == 1, the answer is 2N - 2; otherwise it is 2N - 1.
    No simulation is needed; it is a constant-time check per test case.

Complexity:
    Time : O(N) per test case (reading input); O(1) for the decision itself
    Space: O(N) for the list B (O(1) if only the endpoints were stored)
"""


# ------------------------------------ Solution -----------------------------------------------


import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    B = list(map(int, input().split()))
    if B[0] == 0 and B[-1] == 1:
        print(2 * N - 2)
    else:
        print(2 * N - 1)
