"""
Problem   : N-th Term Of GP
Platform  : Code360 (Naukri)
Link      : https://www.naukri.com/code360/guided-paths/data-structures-algorithms/content/118522/offering/1380915
Difficulty: Easy
Date      : 2026-09-12
Topics    : Math, Number Theory, Modular Exponentiation

Approach:
    The N-th term of a Geometric Progression is given by:
        T(n) = A * R^(n-1)
    Since R^(n-1) can be huge, we compute it under modulo (1e9+7)
    using Python's built-in fast modular exponentiation pow(r, n-1, MOD),
    which runs in O(log n) instead of a naive O(n) loop multiplication.

Time Complexity : O(log n) per test case  (due to fast pow)
Space Complexity: O(1) extra space
"""


# ---------------------------- Solution -----------------------------------


import sys
from sys import stdin

def nthTermOfGP(n, a, r):
    MOD = 10**9 + 7
    return (a * pow(r, n - 1, MOD)) % MOD
t = int(sys.stdin.readline().strip())
while(t > 0):
    n, a, r = map(int,input().split())
    print(nthTermOfGP(n,a,r))
    t = t - 1
