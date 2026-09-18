"""
Problem   : Test Score
Platform  : CodeChef
Link      : https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/CHEFSCORE
Difficulty: 800 (rated ~610)
Topics    : Math, Basic Programming
Date      : 2026-09-18

Approach:
    For each test case, check if a total score Y is achievable using N
    questions worth X points each. Y is achievable iff:
      1. Y is a multiple of X (Y % X == 0), and
      2. Y does not exceed the maximum possible score (Y <= N * X).
    Print "YES" if both conditions hold, else "NO".

Time complexity : O(T) — O(1) work per test case
Space complexity: O(1) — no extra data structures used
"""


# ----------------------------- Solution ------------------------------------------


T = int(input())

for _ in range(T):
    N, X, Y = map(int, input().split())

    if Y % X == 0 and Y <= N * X:
        print("YES")
    else:
        print("NO")
