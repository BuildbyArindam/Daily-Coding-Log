"""
Problem   : Greatest Dumpling Fight
Platform  : CodeChef (DUMPLING)
Link      : https://www.codechef.com/problems/DUMPLING
Difficulty: 1738
Topics    : Math, Number Theory (GCD / LCM)
Date      : 2026-10-09

Approach:
    Let g1 = gcd(A, B) and g2 = gcd(C, D). The valid positions for each side
    are the multiples of g1 and of g2 respectively, so the positions valid
    for both are the multiples of L = lcm(g1, g2).
    Counting multiples of L in [-K, K] gives 2 * floor(K / L) + 1
    (both signs, plus 0).
    lcm is computed as (g1 // gcd(g1, g2)) * g2 to keep numbers small.

Complexity:
    Time : O(T * log(max(A, B, C, D))) from the gcd calls
    Sp


# ---------------------------------- Solution ------------------------------------------------------


import math

T = int(input())

for _ in range(T):
    A, B, C, D, K = map(int, input().split())
    g1 = math.gcd(A, B)
    g2 = math.gcd(C, D)
    L = (g1 // math.gcd(g1, g2)) * g2
    ans = 2 * (K // L) + 1
    print(ans)
