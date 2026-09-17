"""
Problem: Special Shop
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/special-shop-69904c91/
Date: 2026-09-17
Difficulty: Medium
Topics: Algorithms, Searching, Ternary/Ternary-like optimization (ternary search on convex function)

Approach:
Cost(x) = A*x^2 + B*(N-x)^2 is a convex function of x (integer split point).
Instead of ternary searching, find the real-valued minimum by differentiating:
    d/dx [A*x^2 + B*(N-x)^2] = 0  =>  x = B*N / (A+B)
Since the true minimum may not be an integer, check the two integers surrounding it
(floor and floor+1) and take whichever gives the lower cost.

Time Complexity: O(1) per test case, O(T) overall
Space Complexity: O(1)
"""


# ------------------------------- Solution ------------------------------------------


import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N, A, B = map(int, input().split())
    numerator = B * N
    denominator = A + B
    x = numerator // denominator
    x1 = x
    x2 = x + 1
    cost1 = A * x1 * x1 + B * (N - x1) * (N - x1)
    cost2 = A * x2 * x2 + B * (N - x2) * (N - x2)
    print(min(cost1, cost2))
