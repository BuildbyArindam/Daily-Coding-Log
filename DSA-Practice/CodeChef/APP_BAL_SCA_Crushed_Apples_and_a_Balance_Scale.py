"""
Problem   : Crushed Apples and a Balance Scale
Platform  : CodeChef
Link      : https://www.codechef.com/problems/APP_BAL_SCA
Difficulty: 1736
Topics    : Math, Number Theory 
Date      : 2026-10-09

Approach:
    Strip all factors of 2 from M to get its odd part. The answer is YES
    iff N <= M and N is a multiple of that odd part.

Complexity:
    Time  : O(log M) per test case (repeated halving), O(T log M) overall
    Space : O(1)
"""


# ----------------------------------------------------- Solution ------------------------------------------------------------------


import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    M, N = map(int, input().split())
    original = M
    while original % 2 == 0:
        original //= 2
    if N <= M and N % original == 0:
        print("YES")
    else:
        print("NO")
