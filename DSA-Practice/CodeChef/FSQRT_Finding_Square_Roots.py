"""
Problem: Finding Square Roots
Platform: CodeChef
Link: https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/FSQRT
Difficulty: 668
Date Solved: 2026-09-19
Topics: Math, Number Theory, Basic Programming

Approach:
    For each test case, read N and print floor(sqrt(N)) using Python's
    math.sqrt(). Since math.sqrt returns a float, int() truncates it to
    give the integer square root.

Time Complexity: O(1) per query -> O(T) overall
Space Complexity: O(1)
"""


# ------------------------------------ Solution ----------------------------------------


import math

T = int(input())

for _ in range(T):
    N = int(input())
    print(int(math.sqrt(N)))
