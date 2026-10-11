"""
Problem   : Chef and Modulo Game (MGAME)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/MGAME
Difficulty: 1813
Topics    : Permutations & Combinations, Mathematics, Combinatorics
Date      : 2026-10-11

Approach:
    The answer is a closed-form formula in N and P, so there is no
    iteration over values. For N <= 2 the answer is P^3. For N > 2, let
    m = (N - 1) // 2 and evaluate
        (P - m)^2 + (P - N) * (2P - N - m)
    directly.

Complexity:
    Time : O(1) per test case, O(T) overall
    Space: O(1)
"""


# ------------------------------------------ Solution ----------------------------------------------


import sys
input = sys.stdin.buffer.readline

t = int(input())
for _ in range(t):
    n, p = map(int, input().split())
    if n <= 2:
        print(p ** 3)
    else:
        m = (n - 1) // 2
        ans = (p - m) ** 2 + (p - n) * (2 * p - n - m)
        print(ans)
