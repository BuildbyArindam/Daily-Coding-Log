"""
Platform   : CodeChef
Problem    : Find an integer (SUMDIV2)
Link       : https://www.codechef.com/problems/SUMDIV2
Difficulty : 1714
Topics     : Mathematics
Date       : 2026-09-29

Approach:
    Let L = lcm(X, Y). The answer N makes X + Y + N a multiple of L,
    so X + Y + N = k * L. To keep N positive and minimal, take the
    smallest k with k * L > X + Y, i.e. k = (X + Y) // L + 1.
    Then N = k * L - X - Y.

Complexity:
    Time  : O(T * log(min(X, Y)))  -- dominated by the gcd per test case
    Space : O(1)
"""


# -------------------------------- Solution ----------------------------------------------


import sys
from math import gcd

def solve():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        X, Y = map(int, input().split())
        L = (X // gcd(X, Y)) * Y
        k = (X + Y) // L + 1
        N = k * L - X - Y
        print(N)

if __name__ == "__main__":
    solve()
