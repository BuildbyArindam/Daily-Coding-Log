"""
Problem   : Accounting
Platform  : Codeforces
Link      : https://codeforces.com/problemset/problem/30/A
Difficulty: *1400
Topics    : Brute Force, Math
Date      : 2026-08-30

Approach:
Given A, B, n, find integer X such that A * X^n = B.
- If A == 0: answer is 0 if B == 0 too, else no solution exists.
- Otherwise brute-force X over a bounded range [-1000, 1000]
  (safe since |A * X^n| grows fast and inputs are small),
  checking A * X^n == B for each candidate.

Time complexity : O(R) where R = 2001 (brute-force range) -> effectively O(1)
Space complexity: O(1)
"""


# ---------------------- Solution --------------------------


A, B, n = map(int, input().split())
if A == 0:
    if B == 0:
        print(0)  
    else:
        print("No solution")
else:
    for X in range(-1000, 1001):
        if A * (X ** n) == B:
            print(X)
            break
    else:
        print("No solution")
