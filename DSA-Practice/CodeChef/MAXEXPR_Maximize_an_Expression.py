"""
Platform   : CodeChef
Problem    : Maximize an Expression (MAXEXPR)
Link       : https://www.codechef.com/problems/MAXEXPR
Difficulty : 1809
Topics     : Math, Optimization
Date       : 2026-10-11

Approach:
    Closed-form solution, no search or iteration needed.
    1. Compute S = sum(k_i * c_i). If S < 0, no valid answer exists, so print -1.
    2. If S == 0 (within eps), the answer is F = 0 with x_i = -c_i.
    3. Otherwise let H = sum(1 / k_i), then
       F = sqrt(S * H) and A = S / H,
       with x_i = A / k_i^2 - c_i for each i.
    math.fsum is used to limit floating-point error, and eps = 1e-9
    guards the S == 0 comparison.

Complexity:
    Time  : O(N) per test case
    Space : O(N)
"""


# --------------------------------------- Solution ---------------------------------------------------


import sys
import math

def solve():
    input = sys.stdin.buffer.readline
    T = int(input())
    for _ in range(T):
        N = int(input())
        k = list(map(float, input().split()))
        c = list(map(float, input().split()))
        S = math.fsum(k[i] * c[i] for i in range(N))
        if S < -1e-9:
            print(-1)
            continue
        if abs(S) <= 1e-9:
            ans = [0.0] + [-c[i] for i in range(N)]
            print(" ".join(f"{v:.10f}" for v in ans))
            continue
        H = math.fsum(1.0 / ki for ki in k)
        F = math.sqrt(S * H)
        A = S / H
        x = [A / (ki * ki) - ci for ki, ci in zip(k, c)]
        ans = [F] + x
        print(" ".join(f"{v:.10f}" for v in ans))

if __name__ == "__main__":
    solve()
